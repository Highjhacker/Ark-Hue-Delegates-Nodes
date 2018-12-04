# [inital value when first run, last value, new value]
import time
import sys
import atexit
from phue import Bridge
from helpers import get_from_config, get_delegate_blocks_activity


LOOP_TIME = int(get_from_config("loop_time"))
TRANSITION_TIME = int(get_from_config("transition_time"))
UP_COLOR = int(get_from_config("node_is_up_color"))
DOWN_COLOR = int(get_from_config("node_is_down_color"))
MISSED_BLOCK_COLOR = int(get_from_config("node_missed_block_color"))


def set_brightness(_bridge):
    if int(get_from_config("brightness")) > 254:
        print("Brightness can't be greater than 254.")
        _bridge.set_light(1, 'bri', 254, transitiontime=4)
    else:
        _bridge.set_light(1, 'bri', int(get_from_config("brightness")), transitiontime=4)


def set_color(_bridge, _up_color, _missed_block_color,  _down_color, _transition_time):
    if blocks_activity[-1] == initial_blocks_activity:
        _bridge.set_light(1, 'hue', _up_color, transitiontime=_transition_time)
    elif blocks_activity[-1] == initial_blocks_activity + 1 or blocks_activity[-1] == initial_blocks_activity + 2:
        _bridge.set_light(1, 'hue', _missed_block_color, transitiontime=_transition_time)
    elif blocks_activity[-1] == initial_blocks_activity + 3:
        _bridge.set_light(1, 'hue', _down_color, transitiontime=_transition_time)


def on_exit(_initial_color):
    bridge.set_light(1, "hue", _initial_color)
    bridge.set_light(1, "on", False)


if __name__ == '__main__':
    bridge = Bridge(get_from_config("bridge_ip"))
    bridge.connect()
    print(bridge.get_api())
    bridge.set_light(get_from_config("light_id"), "on", True)
    set_brightness(bridge)

    initial_color = bridge.get_api()["lights"]["1"]["state"]["hue"]
    initial_blocks_activity = get_delegate_blocks_activity()
    blocks_activity = (get_delegate_blocks_activity(), get_delegate_blocks_activity())

    atexit.register(on_exit, _initial_color=initial_color)

    while True:
        try:
            set_color(bridge, UP_COLOR, MISSED_BLOCK_COLOR,DOWN_COLOR, TRANSITION_TIME)
            blocks_activity = (blocks_activity[-1], get_delegate_blocks_activity())
            print(blocks_activity)
            time.sleep(LOOP_TIME)
        except KeyboardInterrupt:
            print("Program exiting")
            sys.exit(0)
