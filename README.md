# shroomosphereIoT


## Installation

### Install Raspian

1. Download Raspberry Pi Imager here: ```https://www.raspberrypi.com/software/``` or use package manager
2. Install and run the imager
3. Click the settings icon first to Enable SSH
4. Mount a micro SD card to install the Raspian OS on and select that in the storage dropdown
5. Move SD to Raspberry PI and you're done

### Install  SCD4x Sensors

*setup the raspberry pi to use ssh and use vscode and terminal to edit code and run pip/commands.

Reference: ```https://sensirion.github.io/python-i2c-scd/quickstart.html```

1. Enable I2C ```https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c```
    a. sudo raspi-config
    b. Interface Options -> I2C
2. ```pip install sensirion-i2c-scd```
3. ```pip install sensirion-shdlc-sensorbridge```
4. ```python examples/example_usage_sensorbridge_scd4x.py --i2c-port <your I2Cport>``` if you have a different I2C port add the flag: ```--i2c-port <your I2Cport>```


### install the  7-segment LED display
Reference Link: ```https://raspberrytips.nl/tm1637-4-digit-led-display-raspberry-pi/```

1. Install the python (not micropython) TM1637 library ```pip3 install raspberrypi-tm1637```
2. Add the code as outlined in the reference link. 


### Set Up Auto-Startup Script 

Run your code automatically when the Pi boots up. Refernce: ```https://www.instructables.com/Raspberry-Pi-Launch-Python-script-on-startup/```

1. Adjust the launcher.sh to match your file structure, and also change the username ```sudo su``` command so that the script runs as the ssh user
2. run ```chmod 755 launcher.sh```
3. 