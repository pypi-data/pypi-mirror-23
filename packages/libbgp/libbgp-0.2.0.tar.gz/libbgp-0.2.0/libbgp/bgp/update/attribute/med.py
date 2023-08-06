# Copyright 2015-2017 Cisco Systems, Inc.
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import struct

from libbgp.exception import BGPNotification
from .attribute import Attribute, AttributeID, AttributeFlag
from .attributes import Attributes


@Attributes.register()
class MED(Attribute):
    """
    This is an optional non-transitive attribute that is a
    four-octet unsigned integer. The value of this attribute
    MAY be used by a BGP speaker's Decision Process to
    discriminate among multiple entry points to a neighboring
    autonomous system.
    """

    TYPE = AttributeID.MULTI_EXIT_DISC
    FLAG = AttributeFlag.OPTIONAL

    @classmethod
    def unpack(cls, data, capability):

        if len(data) != 4:
            raise BGPNotification(3, 5)
        return cls(value=struct.unpack('!I', data)[0])

    @classmethod
    def pack(cls, data, capability):
        if data not in range(0, 65536):
            raise BGPNotification(3, 5)
        return cls(value=data, hex_value=struct.pack('!I', data))
