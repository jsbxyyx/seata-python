#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from core.protocol import Version
from core.protocol.MessageType import MessageType
from core.protocol.MessageTypeAware import MessageTypeAware


class RegisterTMRequest(MessageTypeAware):
    UDATA_VGROUP = "vgroup"
    UDATA_AK = "ak"
    UDATA_DIGEST = "digest"
    UDATA_IP = "ip"
    UDATA_TIMESTAMP = "timestamp"

    def __init__(self, application_id, transaction_service_group, extra_data):
        self.version = Version.CURRENT
        self.application_id = application_id
        self.transaction_service_group = transaction_service_group
        self.extra_data = extra_data

    def get_type_code(self):
        return MessageType.TYPE_REG_CLT


class RegisterTMResponse(MessageTypeAware):

    def __init__(self, result=True):
        self.result = result

        self.version = Version.CURRENT
        self.identified = result
        self.extra_data = None

    def get_type_code(self):
        return MessageType.TYPE_REG_CLT_RESULT
