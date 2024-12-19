#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# (c) Copyright 2023 Sensirion AG, Switzerland

import time
import datetime
import tm1637
import argparse
from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection
from sensirion_i2c_scd import Scd4xI2cDevice

############ SCD41 SENSOR SETUP CODE

parser = argparse.ArgumentParser()
parser.add_argument('--i2c-port', '-p', default='/dev/i2c-1')
args = parser.parse_args()


############ TM1637 DISPLAY SETUP CODE

ppmDisplay = tm1637.TM1637(17,4)
co2Display = tm1637.TM1637(18,23)

with LinuxI2cTransceiver(args.i2c_port) as i2c_transceiver:
 
    ############ TM1637 DISPLAY LOOP CODE

    ppmDisplay.show('PPnn')
    


    ############ SCD41 SENSOR LOOP CODE


    # Create SCD4x device
    scd4x = Scd4xI2cDevice(I2cConnection(i2c_transceiver))

    # Make sure measurement is stopped, else we can't read serial number or
    # start a new measurement
    scd4x.stop_periodic_measurement()

    print("scd4x Serial Number: {}".format(scd4x.read_serial_number()))

    scd4x.start_periodic_measurement()

    # Measure every 5 seconds for 5 minute
    for _ in range(60):
        time.sleep(5)
        co2, temperature, humidity = scd4x.read_measurement()
        co2Display.number(co2.co2)
        # use default formatting for printing output:
        print("{}, {}, {}".format(co2, temperature, humidity))


   


