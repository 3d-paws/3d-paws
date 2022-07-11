# 3D-PAWS

3D-PAWS is a Python3 library used to run the various sensors of a 3D-PAWS station. This library supports the following sensors: BMP280, BME280, HTU21d, MCP9808, AS5600, 55300-00-02-A, and SS451A. Note that you need to install this software on a raspberry pi in order for it to work.

## Installation
### Step 1 - Download the software
Use [github](https://github.com/) to install 3D-PAWS. Install git with the following in the command line:

```bash
cd /home/pi/
git clone https://github.com/3d-paws/3d-paws
cd 3d-paws/
sudo python3 setup.py install
```

Note: if you're not using one of our images, you might need to install git before running the above commands. If that's the case, you can do so with:
```bash
sudo apt-get install git
```

### Step 2 - Setup the Environment
Once the 3D-PAWS library is installed, run the following commands:
```bash
sudo python3 environment.py
```
Note: this step will delete anything already in the cron (this is to ensure no issues occur when updating the 3D-PAWS software). If the pi is only used for 3d-paws (which is recommended) then this won't be an issue. 

### Step 3 - Set Variables
You'll want to change your station vairables in order for accurate readings, specific recording intervals, and to activate CHORDS. There are two ways of doing this: 

The first is the recommended way. Launch the GUI (it has a shortcut on the desktop). In the GUI, there is a Settings button in the top left. It contains 3 options. Click through each of them, changing any variables you need to. Descriptions for these variables are noted in the GUI.  

The second option is to update the variables.txt file directly, which is on located your Desktop (/home/pi/Desktop). It is formatted as follows: recording_interval,chords_interval,chords_on/off,chords_id,chords_site,pressure_level,test_mode,altitude.

In either case, the software will run without any changes made during this step. However, we recommend at least changing pressure level and altitude to ensure the data is accurate. 

## Usage
You can either launch the GUI from the desktop by double clicking the icon, or from the terminal.
```python
cd /home/pi/3d-paws/scripts
sudo python3 main.py
```

If for some reason you don't have a desktop shortcut, you can make one. First, in the File manager -> Edit -> Preferences -> General -> "Do not ask option on executable launch"

Then right click the desktop, and make a file called 3d-paws.desktop
Open it, and paste the following in:
[Desktop Entry]
Version=1.1
Type=Application
Encoding=UTF-8
Name=3D-PAWS
Comment=3d paws gui
Icon=/home/pi/3d-paws/3d-paws-icon.png
Exec=sudo python3 /home/pi/3d-paws/scripts/main.py
Terminal=false
Categories=Graphics

## Updates
To update the software, you'll need to delete the 3d-paws/ folder and reclone it by following the below steps. This will NOT change your variables.txt file.
```python
cd /home/pi/
sudo rm -rf 3d-paws
git clone https://github.com/3d-paws/3d-paws
cd 3d-paws/
sudo python3 setup.py install
sudo python3 environment.py
```

## License
[MIT](https://choosealicense.com/licenses/mit/)