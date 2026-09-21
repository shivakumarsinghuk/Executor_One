# -*- coding: utf-8 -*-
"""
login_types.py
"""
import sys
from BrokerUtility.pal.utility_manager import *


class ILogicInterface:
    def create(self, args, broker_utility_manager:utility_manager):
        print("Parent IUserInterfaceLogin get function")

    def wait_for_completion(self):
        print("Parent IUserInterfaceLogin set function")

    def force_close_open_trade(self):
        # Default no-op: executor.py calls this on every logic after its threads join, but only
        # logics that hold live positions across shutdown need to override it.
        pass

    def get_broker(self):
        print("Parent IUserInterfaceLogin get broker function")

    def get_broker_utility(self):
        print("Parent IUserInterfaceLogin get broker function")