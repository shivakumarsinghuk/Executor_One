# -*- coding: utf-8 -*-
"""
login_types.py
"""
import sys
from BrokerUtility.pal.utility_manager import *
from Utility.quotes_utility import *


class ILogic:
    def __init__(self, args, broker_utility_manager:utility_manager, quotes_utility:QuoteUtility):
        print("In ILogic Init")

    def get_broker_utility(self):
        print("Get broker utility")