import argparse
from BusinessLogic.example_logic.interfaces import *
from BusinessLogic.vwappiercing_options.interfaces import *
from Utility.nse_utility import *
from BrokerUtility.pal.utility_manager import *
from Utility.quotes_utility import *

LOGIC_REGISTRY = {
    "example": LogicExampleInterface,
    "vwap_piercing_options": LogicVwapPiercingOptionsInterface,
}

def validate_arguments(args=None):
    parser = argparse.ArgumentParser(description="Demo script with named args")

    parser.add_argument("--userinterface", type=str, required=True, help="User Interface Supported [gsheet]")
    parser.add_argument("--key", type=str, help="Provide the json file")
    parser.add_argument("--logic", type=str, default="example",
                        help=f"Business logic to run {list(LOGIC_REGISTRY.keys())}")
    args = parser.parse_args()
    print(args.userinterface, args.key, args.logic)
    return args

if __name__ == "__main__":

    args = validate_arguments()
    obj_logic_interface = LOGIC_REGISTRY[args.logic]()

    #construct nse utility
    obj_nse_utility = nse_utitlity()
    obj_broker_utitility_manager:utility_manager = utility_manager()
    obj_quotes_utility: QuoteUtility = QuoteUtility()
    obj_logic_interface.create(args, obj_broker_utitility_manager, obj_quotes_utility)

    #set the broker utility of quotes utility - this is must
    #use broker utility of any business logic and set it
    obj_quotes_utility.set_trade_utility(obj_logic_interface.get_broker_utility())

    print("Calling wait for completion")
    obj_logic_interface.wait_for_completion()
    print("Exiting from main")

