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

    def get_broker(self):
        print("Parent IUserInterfaceLogin get broker function")
