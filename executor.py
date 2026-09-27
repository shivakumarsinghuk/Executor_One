import argparse
from BusinessLogic.example_logic.interfaces import *
# Both modules name their entry class LogicVwapPiercingOptionsInterface, so a star import of the
# second silently rebinds the first -- which is how "vwap_piercing_options" ended up resolving to
# the _buy class, leaving the VWAPPiercingOptions sheet with nothing to write. Import explicitly
# under distinct aliases so each --logic name maps to its own strategy.
from BusinessLogic.vwappiercing_options.interfaces import (
    LogicVwapPiercingOptionsInterface as LogicVwapPiercingOptionsSellInterface)
from BusinessLogic.vwap_piercing_option_buy.interfaces import (
    LogicVwapPiercingOptionsInterface as LogicVwapPiercingOptionsBuyInterface)
from Utility.nse_utility import *
from BrokerUtility.pal.utility_manager import *
from Utility.quotes_utility import *

LOGIC_REGISTRY = {
    "example": LogicExampleInterface,
    "vwap_piercing_options": LogicVwapPiercingOptionsSellInterface,
    "vwap_piercing_options_buy": LogicVwapPiercingOptionsBuyInterface
}

def str_to_bool(value):
    if value.lower() in ("true", "1", "yes"):
        return True
    if value.lower() in ("false", "0", "no"):
        return False
    raise argparse.ArgumentTypeError(f"expected true or false, got '{value}'")

def valid_date(value):
    from datetime import datetime
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        raise argparse.ArgumentTypeError(f"expected date as YYYY-MM-DD, got '{value}'")
    return value

def validate_arguments(args=None):
    parser = argparse.ArgumentParser(description="Demo script with named args")

    parser.add_argument("--userinterface", type=str, required=True, help="User Interface Supported [gsheet]")
    parser.add_argument("--key", type=str, help="Provide the json file")
    parser.add_argument("--logic", type=str, nargs="+", default=["example"], choices=LOGIC_REGISTRY,
                        help=f"Business logic to run {list(LOGIC_REGISTRY.keys())}")
    parser.add_argument("--test_mode", type=str_to_bool, default=False,
                        help="true/false (default false). When true, --date is required and the logic "
                             "runs against that date's candles instead of today's")
    parser.add_argument("--date", type=valid_date,
                        help="Trading date YYYY-MM-DD to use when --test_mode is true")
    args = parser.parse_args()
    if args.test_mode and not args.date:
        parser.error("--date YYYY-MM-DD is required when --test_mode is true")
    if not args.test_mode:
        args.date = None
    print(args.userinterface, args.key, args.logic, "test_mode:", args.test_mode, "date:", args.date)
    return args

if __name__ == "__main__":

    args = validate_arguments()
    #construct nse utility
    obj_nse_utility = nse_utitlity()
    obj_broker_utitility_manager:utility_manager = utility_manager()

    logic_interfaces = []
    logic_types = set()
    obj_quotes_utility: QuoteUtility = QuoteUtility()
    for logic_name in args.logic:
        logic_type = LOGIC_REGISTRY[logic_name]
        if logic_type in logic_types:
            print(f"Skipping duplicate logic alias: {logic_name}")
            continue
        logic_types.add(logic_type)
        obj_logic_interface = logic_type()
        obj_logic_interface.create(args, obj_broker_utitility_manager, obj_quotes_utility)

        logic_interfaces.append(obj_logic_interface)

    # All logics share one quote poller and broker utility.
    if logic_interfaces:
        obj_quotes_utility.set_trade_utility(logic_interfaces[0].get_broker_utility())

    print("Calling wait for completion")
    for obj_logic_interface in logic_interfaces:
        obj_logic_interface.wait_for_completion()
        obj_logic_interface.force_close_open_trade()
    print("Exiting from main")

