# -*- coding: utf-8 -*-
"""
login_types.py
"""
import sys


class IUserInterface:

    def get_data(self):
        print("Parent IUserInterfaceLogin get function")

    def set_data(self):
        print("Parent IUserInterfaceLogin set function")


class ILogicInterface:

    def create(self, p_nse_utility):
        print("Parent IUserInterfaceLogin get function")

    def wait_for_completion(self):
        print("Parent IUserInterfaceLogin set function")
