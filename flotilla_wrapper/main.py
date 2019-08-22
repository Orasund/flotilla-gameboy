import time

import flotilla


def get_flotilla():
    print("connecting client...")
    dock = flotilla.Client()
    while not dock.ready:
        time.sleep(0.1)
    print("client connected!")
    return dock


def get_touch(dock):
    print('connecting touch module:')
    for _ in range(10):
        touch = dock.first(flotilla.Touch)
        if not isinstance(touch, flotilla.module.NoModule):
            print('found touch', touch)
            return touch
        time.sleep(1)
    print('touch not found')