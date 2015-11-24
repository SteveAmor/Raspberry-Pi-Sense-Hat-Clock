#!/usr/bin/env python3

from sense_hat import SenseHat
import time

sense = SenseHat()

number = [
0,1,1,1, #zero
0,1,0,1,
0,1,0,1,
0,1,1,1,
0,0,1,0, #one
0,1,1,0,
0,0,1,0,
0,1,1,1,
0,1,1,1, #two
0,0,1,1,
0,1,1,0,
0,1,1,1,
0,1,1,1, #three
0,0,1,1,
0,0,1,1,
0,1,1,1,
0,1,0,1, #four
0,1,1,1,
0,0,0,1,
0,0,0,1,
0,1,1,1, #five
0,1,1,0,
0,0,1,1,
0,1,1,1,
0,1,0,0, #six
0,1,1,1,
0,1,0,1,
0,1,1,1,
0,1,1,1, #seven
0,0,0,1,
0,0,1,0,
0,1,0,0,
0,1,1,1, #eight
0,1,1,1,
0,1,1,1,
0,1,1,1,
0,1,1,1, #nine
0,1,0,1,
0,1,1,1,
0,0,0,1
]

hourColour   = [255,0,0] # red
minuteColour = [0,255,255] # cyan
empty        = [0,0,0] # off / black

clockImage = [
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0
]

hour = time.localtime().tm_hour
minute = time.localtime().tm_min

# Tens of hours

if (hour >= 10):
	pixelOffset = 0
	index = -4
	for indexLoop in range(0, 4):
		index = index + 4
		for counterLoop in range(0, 4):
			clockImage[index] = number[int(hour/10)*16+pixelOffset]
			pixelOffset = pixelOffset + 1
			index = index + 1

# Units of hours

pixelOffset = 0
index = 0
for indexLoop in range(0, 4):
	index = index + 4
	for counterLoop in range(0, 4):
		clockImage[index] = number[int(hour%10)*16+pixelOffset]
		pixelOffset = pixelOffset + 1
		index = index + 1

# Tens of minutes

pixelOffset = 0
index = 28
for indexLoop in range(0, 4):
	index = index + 4
	for counterLoop in range(0, 4):
		clockImage[index] = number[int(minute/10)*16+pixelOffset]
		pixelOffset = pixelOffset + 1
		index = index + 1

# Units of minutes

pixelOffset = 0
index = 32
for indexLoop in range(0, 4):
	index = index + 4
	for counterLoop in range(0, 4):
		clockImage[index] = number[int(minute%10)*16+pixelOffset]
		pixelOffset = pixelOffset + 1
		index = index + 1

# Colour the hours

for index in range(0, 32):
	if (clockImage[index]):
		clockImage[index] = hourColour
	else:
		clockImage[index] = empty

# Colour the minutes

for index in range(32, 64):
	if (clockImage[index]):
		clockImage[index] = minuteColour
	else:
		clockImage[index] = empty

# Display the time

sense.set_rotation(90) # Optional
sense.low_light = True # Optional
sense.set_pixels(clockImage)
