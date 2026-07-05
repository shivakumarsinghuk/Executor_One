# -*- coding: utf-8 -*-
"""
login_types.py
"""
import sys
from BrokerUtility.pal.utility_manager import *


class ILogic:
    def __init__(self, args, broker_utility_manager:utility_manager):
        print("In ILogic Init")
