#!/usr/bin/env python
#
# https://www.dexterindustries.com/GoPiGo/
# https://github.com/DexterInd/GoPiGo3
#
# Copyright (c) 2017 Dexter Industries
# Released under the MIT license
# (http://choosealicense.com/licenses/mit/).
#
# For more information see
# https://github.com/DexterInd/GoPiGo3/blob/master/LICENSE.md
#
# This code is an example for controlling the GoPiGo3 LED.
#
# Results:  When you run this program, the GoPiGo3 will take
# readings from a Grove light sensor connected to its
# port Analog/Digital 1
#


# import the time library for the sleep function
import time

# import the GoPiGo3 drivers
import easygopigo3 as easy

# Create an instance of the GoPiGo3 class.
# GPG will be the GoPiGo3 object.
GPG = easy.EasyGoPiGo3()

# Create an instance of the Light sensor
my_light_sensor = easy.LightSensor("AD1", GPG)

# loop forever while polling the sensor
while(True):
    reading = my_light_sensor.read()
    # scale the reading to a 0-100 scale
    percent_reading = my_light_sensor.percent_read()
    print("{}, {:.1f}%".format(reading, percent_reading))
    time.sleep(0.05)

