#!/usr/bin/python
# Code to update the cron
# Joseph E. Rener
# NCAR/RAL
# Boulder, CO USA
# Email: jrener@ucar.edu
# Copyright (c) 2022 UCAR
# Developed at COMET at University Corporation for Atmospheric Research and the Research Applications Laboratory at the National Center for Atmospheric Research (NCAR)

import os
from crontab import CronTab
cron = CronTab(user='root')

print("Setting up cron...")
cron.remove_all()

report = cron.new(command='python3 /home/pi/3d-paws/scripts/report.py >> /tmp/report.log 2>&1')
report.minute.every(1)

bm = cron.new(command='python3 /home/pi/3d-paws/scripts/bmp_bme.py >> /tmp/bmp.log 2>&1')
bm.minute.every(1)
bm.set_comment("BMP/BME")
bm.enable(False)

htu = cron.new(command='python3 /home/pi/3d-paws/scripts/htu21d.py >> /tmp/htu21d.log 2>&1')
htu.minute.every(1)
htu.set_comment("HTU21D")
htu.enable(False)

mcp = cron.new(command='python3 /home/pi/3d-paws/scripts/mcp9808.py >> /tmp/mcp9808.log 2>&1')
mcp.minute.every(1)
mcp.set_comment("MCP9808")
mcp.enable(False)

si = cron.new(command='python3 /home/pi/3d-paws/scripts/si1145.py >> /tmp/si1145.log')
si.minute.every(1)
si.set_comment("SI1145")
si.enable(False)

rain = cron.new(command='python3 /home/pi/3d-paws/scripts/rain.py >> /tmp/rain.log 2>&1')
rain.every_reboot()
rain.set_comment("Tipping Bucket")
rain.enable(False)

wind_dir = cron.new(command='python3 /home/pi/3d-paws/scripts/wind_direction.py >> /tmp/wind_direction.log 2>&1')
wind_dir.every_reboot()
wind_dir.set_comment("Wind Direction")
wind_dir.enable(False)

wind_spd = cron.new(command='python3 /home/pi/3d-paws/scripts/wind_speed.py >> /tmp/wind_speed.log 2>&1')
wind_spd.every_reboot()
wind_spd.set_comment("Wind Speed")
wind_spd.enable(False)


link = cron.new(command='ln -s /dev/i2c-1 /dev/i2c-0')
link.every_reboot()
link.set_comment("Resets device link")

backup = cron.new(command='lftp -f /home/pi/3d-paws/scripts/comms/mirror-to-ral-ftp >> /tmp/mirror-to-ral-ftp.log 2>&1')
backup.minute.every(5)
backup.set_comment("RAL-FTP")
backup.enable(False)


cron.write()
print("Done! Printing results now...")
print()
cron = CronTab(user='root')
for job in cron:
    print(job)
    print()


print("Checking for variables.txt...")
variable_path = "/home/pi/Desktop/variables.txt" 
if not os.path.exists(variable_path):
    print("Creating variables.txt...")
    with open(variable_path, 'w') as file:
        file.write("1,1,false,0,3d.chordsrt.com,1013.25,false,100000.0")
    os.chmod(variable_path, 0o777)
print("Done! Envionment has been successfully setup.")
print()