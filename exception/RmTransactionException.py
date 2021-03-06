#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author jsbxyyx
# @since 1.0
from exception.TransactionException import TransactionException


class RmTransactionException(TransactionException):

    def __init__(self, code, message=None, cause=None):
        self.code = code
        self.message = message
        self.cause = cause
