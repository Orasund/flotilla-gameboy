import time

import flotilla


def get_joystick(dock):
    print('connecting joystick module:')
    for _ in range(10):
        joystick = dock.first(flotilla.Joystick)
        if not isinstance(joystick, flotilla.module.NoModule):
            print('found joystick', joystick)
            return MyJoystick(joystick)
        time.sleep(1)
    print('joystick not found')
    dock.stop()
    sys.exit(1)


class MyJoystick:
    def __init__(self, joystick):
        self.joystick = joystick
        
    @property
    def x(self):
        x = joystick.y/1023-0.5
        if x > 0.2:
            return x
        elif x < -0.2:
            return x
        else:
            return 0
    
    @property
    def y(self):
        x = joystick.x/1023-0.5
        if x > 0.2:
            return x
        elif x < -0.2:
            return x
        else:
            return 0
    
