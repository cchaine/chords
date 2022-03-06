#!/usr/bin/env python3

import time
from random import randint
import matplotlib.pyplot as plt
from numpy import linspace

notes = [
    ["A"], 
    ["A#", "Bb"], 
    ["B", "Cb"], 
    ["C", "B#"], 
    ["C#", "Db"],
    ["D"],
    ["D#", "Eb"],
    ["E", "Fb"],
    ["F", "E#"],
    ["F#", "Gb"],
    ["G"],
    ["G#", "Ab"]
]

MAJ=[""]
MIN=["m", "-"]
DIM=["dim", "o"]
AUG=["aug", "+", "#5"]
SUS2=["sus2"]
SUS4=["sus4"]
DOM7=["7"]
MAJ7=["maj7", "M7", "Δ7"]
MIN7=["m7", "-7"]
DIM7=["dim7", "o7"]
HDIM7=["m7b5", "Ø7"]

flavors = [MAJ, MIN, DIM, AUG, SUS2, SUS4, DOM7, MAJ7, MIN7, DIM7, HDIM7]

def find_root(root):
    # Find the root in notes
    found = False
    index = 0
    while not found and index < len(notes):
        if root in notes[index]:
            found = True
        else:
            index += 1
    return index

def invertion(chord, inv):
    return chord[inv:] + chord[:inv]

def chord(root, intervals):
    root_index = find_root(root)
    chord = [root]
    for i in intervals:
        note = notes[(root_index + i) % len(notes)]
        chord += [note[0]]
    return chord


def maj(root):
    return chord(root, [4, 7])

def min(root):
    return chord(root, [3, 7])

def dim(root):
    return chord(root, [3, 6])

def aug(root):
    return chord(root, [4, 8])

def sus2(root):
    return chord(root, [2, 7])

def sus4(root):
    return chord(root, [5, 7])

def dom7(root):
    return chord(root, [4, 7, 10])

def maj7(root):
    return chord(root, [4, 7, 11])

def min7(root):
    return chord(root, [3, 7, 10])

def dim7(root):
    return chord(root, [3, 6, 9])

def hdim7(root):
    return chord(root, [3, 6, 10])

if __name__ == "__main__":
    x = []
    y = []
    plt.plot(x, y)
    plt.pause(0.05)

    while True:
        # Random root note
        root = notes[randint(0, len(notes)-1)]
        root = root[randint(0, len(root)-1)]

        # Random chord flavor
        flavor = flavors[randint(0, len(flavors)-1)]
        flavor = flavor[randint(0, len(flavor)-1)]

        # Generate the chord
        answer = []
        if flavor in MAJ:
           answer = maj(root)
        elif flavor in MIN:
           answer = min(root)
        elif flavor in DIM:
           answer = dim(root)
        elif flavor in AUG:
           answer = aug(root)
        elif flavor in SUS2:
           answer = sus2(root)
        elif flavor in SUS4:
           answer = sus4(root)
        elif flavor in DOM7:
           answer = dom7(root)
        elif flavor in MAJ7:
           answer = maj7(root)
        elif flavor in MIN7:
           answer = min7(root)
        elif flavor in DIM7:
           answer = dim7(root)
        elif flavor in HDIM7:
            answer = hdim7(root)

        # Print the chord
        print("{}{}".format(root, flavor))
        start = time.time()

        # Wait for input
        input()

        # Print the answer
        end = time.time()
        print("{} : {}".format(end - start, answer))

        # Display time
        x = range(0, len(x)+1)
        y += [end - start]
        plt.gca().lines[0].set_xdata(x)
        plt.gca().lines[0].set_ydata(y)
        plt.gca().relim()
        plt.gca().autoscale_view()
        plt.pause(0.05)

        # Wait for input
        input()
