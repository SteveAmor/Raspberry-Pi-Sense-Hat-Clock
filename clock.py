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

hours_minutes = [
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0
]

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

	hours_minutes[0]  = number[int(hour/10)*16]
	hours_minutes[1]  = number[int(hour/10)*16+1]
	hours_minutes[2]  = number[int(hour/10)*16+2]
	hours_minutes[3]  = number[int(hour/10)*16+3]
	hours_minutes[8]  = number[int(hour/10)*16+4]
	hours_minutes[9]  = number[int(hour/10)*16+5]
	hours_minutes[10] = number[int(hour/10)*16+6]
	hours_minutes[11] = number[int(hour/10)*16+7]
	hours_minutes[16] = number[int(hour/10)*16+8]
	hours_minutes[17] = number[int(hour/10)*16+9]
	hours_minutes[18] = number[int(hour/10)*16+10]
	hours_minutes[19] = number[int(hour/10)*16+11]
	hours_minutes[24] = number[int(hour/10)*16+12]
	hours_minutes[25] = number[int(hour/10)*16+13]
	hours_minutes[26] = number[int(hour/10)*16+14]
	hours_minutes[27] = number[int(hour/10)*16+15]

# Units of hours

	hours_minutes[4]  = number[int(hour%10)*16]
	hours_minutes[5]  = number[int(hour%10)*16+1]
	hours_minutes[6]  = number[int(hour%10)*16+2]
	hours_minutes[7]  = number[int(hour%10)*16+3]
	hours_minutes[12] = number[int(hour%10)*16+4]
	hours_minutes[13] = number[int(hour%10)*16+5]
	hours_minutes[14] = number[int(hour%10)*16+6]
	hours_minutes[15] = number[int(hour%10)*16+7]
	hours_minutes[20] = number[int(hour%10)*16+8]
	hours_minutes[21] = number[int(hour%10)*16+9]
	hours_minutes[22] = number[int(hour%10)*16+10]
	hours_minutes[23] = number[int(hour%10)*16+11]
	hours_minutes[28] = number[int(hour%10)*16+12]
	hours_minutes[29] = number[int(hour%10)*16+13]
	hours_minutes[30] = number[int(hour%10)*16+14]
	hours_minutes[31] = number[int(hour%10)*16+15]

# Tens of minutes

	hours_minutes[32] = number[int(minute/10)*16]
	hours_minutes[33] = number[int(minute/10)*16+1]
	hours_minutes[34] = number[int(minute/10)*16+2]
	hours_minutes[35] = number[int(minute/10)*16+3]
	hours_minutes[40] = number[int(minute/10)*16+4]
	hours_minutes[41] = number[int(minute/10)*16+5]
	hours_minutes[42] = number[int(minute/10)*16+6]
	hours_minutes[43] = number[int(minute/10)*16+7]
	hours_minutes[48] = number[int(minute/10)*16+8]
	hours_minutes[49] = number[int(minute/10)*16+9]
	hours_minutes[50] = number[int(minute/10)*16+10]
	hours_minutes[51] = number[int(minute/10)*16+11]
	hours_minutes[56] = number[int(minute/10)*16+12]
	hours_minutes[57] = number[int(minute/10)*16+13]
	hours_minutes[58] = number[int(minute/10)*16+14]
	hours_minutes[59] = number[int(minute/10)*16+15]

# Units of minutes

	hours_minutes[36] = number[int(minute%10)*16]
	hours_minutes[37] = number[int(minute%10)*16+1]
	hours_minutes[38] = number[int(minute%10)*16+2]
	hours_minutes[39] = number[int(minute%10)*16+3]
	hours_minutes[44] = number[int(minute%10)*16+4]
	hours_minutes[45] = number[int(minute%10)*16+5]
	hours_minutes[46] = number[int(minute%10)*16+6]
	hours_minutes[47] = number[int(minute%10)*16+7]
	hours_minutes[52] = number[int(minute%10)*16+8]
	hours_minutes[53] = number[int(minute%10)*16+9]
	hours_minutes[54] = number[int(minute%10)*16+10]
	hours_minutes[55] = number[int(minute%10)*16+11]
	hours_minutes[60] = number[int(minute%10)*16+12]
	hours_minutes[61] = number[int(minute%10)*16+13]
	hours_minutes[62] = number[int(minute%10)*16+14]
	hours_minutes[63] = number[int(minute%10)*16+15]

# Colour the hours

for index in range(0, 32):
	if (hours_minutes[index]):
		clockImage[index] = hourColour
	else:
		clockImage[index] = empty

# Colour the minutes

for index in range(32, 64):
	if (hours_minutes[index]):
		clockImage[index] = minuteColour
	else:
		clockImage[index] = empty

# Display the time

sense.set_rotation(90) # Optional
sense.set_pixels(clockImage)
