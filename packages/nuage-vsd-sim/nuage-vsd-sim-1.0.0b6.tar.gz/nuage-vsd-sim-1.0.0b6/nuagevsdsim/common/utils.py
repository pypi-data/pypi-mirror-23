# BSD 3-Clause License
#
# Copyright (c) 2017, Philippe Dellaert
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of source code must retain the above copyright notice, this
#   list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
#
# * Neither the name of the copyright holder nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
Nuage VSD Sim utils
"""

import ConfigParser
import logging
import re
import sys
import uuid

from vspk import v5_0 as vsdk

NUAGE_API_DATA = {
    'ROOT_UUIDS': {
        'csproot_user': '',
        'csp_enterprise': ''
    },
    'enterprise': {},
    'enterprise_user': {'_TYPE': 'child'},
    'enterprise_group': {'_TYPE': 'child'},
    'group': {},
    'group_user': {'_TYPE': 'member'},
    'user': {},
}

INVARIANT_RESOURCES = [
    'brconnections',
    'cms',
    'licensestatus',
    'ltestatistics',
    'qos',
    'statistics',
    'vrsmetrics'
]


def parse_config(config_file):
    """
    Parses configuration file
    """
    cfg = ConfigParser.ConfigParser()
    cfg.read(config_file)

    # Checking the LOG options
    if not cfg.has_option('LOG', 'directory') or \
            not cfg.has_option('LOG', 'file') or \
            not cfg.has_option('LOG', 'level'):
        print 'Missing options in the LOG section of configuration file {0:s}, please check the sample configuration'.format(config_file)
        sys.exit(1)

    return cfg


def configure_logging(level, path):
    """
    Configures the logging environment
    """
    logging.basicConfig(filename=path, format='%(asctime)s %(levelname)s %(message)s', level=level)
    logger = logging.getLogger(__name__)

    return logger


def init_base_entities():
    """
    Sets up basic entities for use
    """
    global NUAGE_API_DATA

    csproot = vsdk.NUUser(
        id=str(uuid.uuid1()),
        user_name='csproot',
        password='csproot',
        first_name='csproot',
        last_name='csproot',
        email='csproot@CSP.com',
        parent_type='ENTERPRISE'
    )
    csp = vsdk.NUEnterprise(
        id=str(uuid.uuid1()),
        name='CSP',
        description='Enterprise that contains all the CSP users',
        allowed_forwarding_classes=['E', 'F', 'G', 'H'],
        allow_gateway_management=True,
        allow_advanced_qos_configuration=True,
        allow_trusted_forwarding_class=True,
        bgp_enabled=True,
        creation_date=1383734246000,
        customer_id=10002,
        dictionary_version=2,
        enable_application_performance_management=False,
        entity_scope='ENTERPRISE',
        floating_ips_quota=0,
        floating_ips_used=0,
        ldap_authorization_enabled=False,
        ldap_enabled=False,
        last_updated_by=csproot.id,
        last_updated_date=1499101329000
    )
    csproot.parent_id = csp.id

    NUAGE_API_DATA['enterprise_user'][csp.id] = {csproot.id: csproot}
    NUAGE_API_DATA['ROOT_UUIDS']['csp_enterprise'] = csp.id
    NUAGE_API_DATA['enterprise'][csp.id] = csp
    NUAGE_API_DATA['ROOT_UUIDS']['csproot_user'] = csproot.id
    NUAGE_API_DATA['user'][csproot.id] = csproot

    logging.info('Created base entities')
    logging.debug(NUAGE_API_DATA)


def _string_clean(string):
    rep = {
        "IPID": "IpID",
        "VCenter": "Vcenter",
        "vCenter": "Vcenter",
        "VPort": "Vport",
        "IPv6": "Ipv6",
        "IPv4": "Ipv4"
    }

    rep = dict((re.escape(k), v) for k, v in rep.items())
    pattern = re.compile("|".join(list(rep.keys())))

    return pattern.sub(lambda m: rep[re.escape(m.group(0))], string)


def get_idiomatic_name(name):
    first_cap_re = re.compile("(.)([A-Z](?!s([A-Z])*)[a-z]+)")
    all_cap_re = re.compile("([a-z0-9])([A-Z])")

    s1 = first_cap_re.sub(r"\1_\2", _string_clean(name))

    return all_cap_re.sub(r"\1_\2", s1).lower()


def get_singular_name(plural_name):
    if plural_name in INVARIANT_RESOURCES:
        return plural_name

    if plural_name[-3:] == 'ies':
        return plural_name[:-3] + 'y'

    if plural_name[-1:] == 's':
        return plural_name[:-1]
