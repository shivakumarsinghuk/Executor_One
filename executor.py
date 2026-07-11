import argparse
from BusinessLogic.example_logic.interfaces import *
from Utility.nse_utility import *
from BrokerUtility.pal.utility_manager import *
from Utility.quotes_utility import *

def validate_arguments(args=None):
    parser = argparse.ArgumentParser(description="Demo script with named args")

    parser.add_argument("--userinterface", type=str, required=True, help="User Interface Supported [gsheet]")
    parser.add_argument("--key", type=str, help="Provide the json file")
    args = parser.parse_args()
    print(args.userinterface, args.key)
    return args

if __name__ == "__main__":

    args = validate_arguments()
    obj_example_logic_interface = LogicExampleInterface()

    #construct nse utility
    obj_nse_utility = nse_utitlity()
    obj_broker_utitility_manager:utility_manager = utility_manager()
    obj_quotes_utility: QuoteUtility = QuoteUtility()
    obj_example_logic_interface.create(args, obj_broker_utitility_manager, obj_quotes_utility)

    #set the broker utility of quotes utility - this is must
    #use broker utility of any business logic and set it
    obj_quotes_utility.set_trade_utility(obj_example_logic_interface.get_broker_utility())

    print("Calling wait for completion")
    obj_example_logic_interface.wait_for_completion()
    print("Exiting from main")

