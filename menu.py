#!/usr/bin/env python
# sudo service flotillad stop

import sys
import time
import flotilla
from itertools import cycle

def establishConnection(dock):
    print("Client connected...")
    while not dock.ready:
        pass
    return dock

def printImage(matrix,image):
    for x in range(0,8):
      for y in range(0,8):
          matrix.set_pixel(x, y, image[y][x])
    matrix.update()

def printAnimation(matrix,animation):
    for image in animation:
        printImage(matrix,image)
        time.sleep(1)

def print_animation_cogen(matrix, animation):
    image_roll = cycle(animation)
    while True:
        image = next(image_roll)
        printImage(matrix, image)
        time.sleep(1)
        next_animation = yield
        if next_animation != animation:
            animation = next_animation
            image_roll = cycle(animation)

def clearScreen():
    return (
        [ [0,0,0,0,0,0,0,0]
        , [0,0,0,0,0,0,0,0]
        , [0,0,0,0,0,0,0,0]
        , [0,0,0,0,0,0,0,0]
        , [0,0,0,0,0,0,0,0]
        , [0,0,0,0,0,0,0,0]
        , [0,0,0,0,0,0,0,0]
        , [0,0,0,0,0,0,0,0]
        ])

def bootScreen(matrix):
    smiley =(
        [ [0,1,1,0,0,1,1,0]
        , [0,1,1,0,0,1,1,0]
        , [0,1,1,0,0,1,1,0]
        , [0,0,0,0,0,0,0,0]
        , [1,1,1,1,1,1,1,1]
        , [1,0,0,0,0,0,0,1]
        , [0,1,0,0,0,0,1,0]
        , [0,0,1,1,1,1,0,0]
        ])
    printImage(matrix,smiley)

def getMatrix(dock):
    matrix = dock.first(flotilla.Matrix)
    if not matrix:
        print("no Matrix module found...")
        dock.stop()
        sys.exit(1)
    else:
        print("Found. Running...")
        bootScreen(matrix)
    return matrix

def getJoystick(dock):
    joystick = dock.first(flotilla.Joystick)
    while not dock.first(flotilla.Joystick):
        error = (
            [   [ [0,0,0,1,1,0,0,0]
                , [0,0,1,0,1,1,0,0]
                , [0,0,1,1,1,1,0,0]
                , [0,0,0,1,1,0,0,0]
                , [0,0,0,1,1,0,0,0]
                , [0,0,0,1,1,0,0,0]
                , [0,0,1,1,1,1,0,0]
                , [0,1,1,1,1,1,1,0]
                ]
            ,   [ [0,0,1,1,1,1,0,0]
                , [0,0,1,1,1,1,1,0]
                , [0,0,0,0,0,1,1,0]
                , [0,0,0,0,1,1,1,0]
                , [0,0,0,1,1,1,0,0]
                , [0,0,0,1,1,0,0,0]
                , [0,0,0,0,0,0,0,0]
                , [0,0,0,1,1,0,0,0]
                ]
            ])
        printAnimation(error)
    return joystick

dancingAnimation = (
    [   [ [0,0,0,1,1,0,0,0]
        , [0,0,0,1,1,0,0,0]
        , [0,0,0,0,1,0,0,0]
        , [0,0,1,1,0,0,0,0]
        , [0,1,0,1,0,1,0,0]
        , [0,0,0,1,1,0,1,0]
        , [0,0,0,1,1,0,0,0]
        , [0,0,1,0,1,0,0,0]
    ]
    ,   [ [0,0,0,1,1,0,0,0]
        , [0,0,0,1,1,0,0,0]
        , [0,0,0,1,0,0,0,0]
        , [0,0,0,0,1,1,0,0]
        , [0,0,1,0,1,0,1,0]
        , [0,1,0,1,1,0,0,0]
        , [0,0,0,1,1,0,0,0]
        , [0,0,0,1,0,1,0,0]
        ]
    ])

duckAnimation = (
    [   [ [0,0,1,1,1,1,0,0]
        , [0,1,0,0,0,1,0,0]
        , [1,0,0,1,0,1,0,0]
        , [1,0,0,0,0,1,1,1]
        , [0,1,0,0,0,0,0,1]
        , [0,1,0,0,0,0,0,1]
        , [0,1,1,1,1,1,1,1]
        , [0,0,0,0,1,0,0,0]
        ]
    ,   [ [0,0,1,1,1,1,0,0]
        , [0,1,0,0,0,1,0,0]
        , [1,0,0,1,0,1,0,0]
        , [0,1,0,0,0,1,1,1]
        , [1,1,0,0,0,0,0,1]
        , [0,1,0,0,0,0,0,1]
        , [0,1,1,1,1,1,1,1]
        , [0,0,0,0,1,0,0,0]
        ]
    ]
    )

def joystickX(joystick):
    x = joystick.y/1023-0.5
    print('joystickX', x)
    if x > 0.2:
        return x
    elif x < -0.2:
        return x
    else:
        return 0
        
def main ():
    print("""
    Game Selection Screen

    Press CTRL+C to exit.
    """)
    dock = establishConnection(flotilla.Client())
    matrix = getMatrix(dock)
    joystick = getJoystick(dock)
    time.sleep(1)
    matrix.clear()

    if matrix is None:
        print("no Matrix module found...")
        dock.stop()
        sys.exit(1)
    else:
        print("Found. Running...")


    select = 1

    animationList = (
        [ dancingAnimation
        , duckAnimation
        ])

    print_animation_cogenerator = print_animation_cogen(matrix, animationList[select])
    next(print_animation_cogenerator)
    try:
        while True:
            print_animation_cogenerator.send(animationList[select])
            if joystickX(joystick) < 0:
                select = (select - 1) % len(animationList)
            elif joystickX(joystick) > 0:
                select = (select + 1) % len(animationList)

    except KeyboardInterrupt:
        print("Stopping Flotilla...")
        dock.stop()

main()
