import time

import flotilla


def get_slider(dock):
    print('connecting slider module:')
    for _ in range(10):
        slider = dock.first(flotilla.Slider)
        if not isinstance(slider, flotilla.module.NoModule):
            print('found slider', slider)
            return MySlider(slider)
        time.sleep(1)
    print('slider not found')
    dock.stop()
    sys.exit(1)


class MySlider:
    def __init__(self, slider):
        self.slider = slider
        
    @property
    def position(self):
        return self.slider.position / 1023
    