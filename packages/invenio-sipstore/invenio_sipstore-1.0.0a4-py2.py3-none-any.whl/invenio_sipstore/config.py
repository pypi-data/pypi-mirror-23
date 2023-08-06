# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2016 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Default configuration of Invenio-SIPStore module."""

SIPSTORE_DEFAULT_AGENT_JSONSCHEMA = 'sipstore/agent-v1.0.0.json'
"""Default JSON schema for extra SIP agent information.

For more examples, you can have a look at Zenodo's config:
https://github.com/zenodo/zenodo/tree/master/zenodo/modules/sipstore/jsonschemas/sipstore
"""

SIPSTORE_DEFAULT_BAGIT_JSONSCHEMA = 'sipstore/bagit-v1.0.0.json'
"""Default JSON schema for BagIt archiver."""

SIPSTORE_AGENT_JSONSCHEMA_ENABLED = True
"""Enable SIP agent validation by default."""

SIPSTORE_AGENT_FACTORY = 'invenio_sipstore.api.SIP._build_agent_info'
"""Factory to build the agent, stored for the information about the SIP."""

SIPSTORE_FILEPATH_MAX_LEN = 1024
"""Max filepath length."""
