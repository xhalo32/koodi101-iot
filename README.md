# Koodi101  Internet of Things (IoT)

### Raspberry pi – first time setup
1. Open raspi-config with `sudo raspi-config`
2. Under interfacing options, enable **SPI** and **I2C**
3. Exit the raspi-config

If you want to use ssh to connect to your RPI, you can do it by writing
```
sudo systemctl enable ssh
sudo systemctl start ssh
```

Now you can connect from your own machine with ```ssh pi@<ip>``` if you are in the same network.

### Run the project
Let's update our system and install some needed libraries and tools.
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3-requests python3-envirophat python3-smbus rpi.gpio
```

You can now try our app by starting it with
```
./run.sh
```

### Starting the app automatically

Then you can create a cronjob to run `run.sh` periodically
For example add the following line to `/etc/crontab` to execute the script every minute
```
*  *	* * *	root	bash /home/pi/koodi101-iot/iot/run.sh
```

