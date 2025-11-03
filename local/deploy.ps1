ssh root@192.168.1.11 "rm -rf /data/apps/dbus-serialbattery/; mkdir -p /data/apps/"
scp -r $PSScriptRoot\..\dbus-serialbattery\ root@192.168.1.11:/data/apps/
scp $PSScriptRoot\..\local\config.ini root@192.168.1.11:/data/apps/dbus-serialbattery/config.ini
ssh root@192.168.1.11 "chmod +x /data/apps/dbus-serialbattery/*.sh; chmod +x /data/apps/dbus-serialbattery/*.py; chmod +x /data/apps/dbus-serialbattery/service/run; chmod +x /data/apps/dbus-serialbattery/service/log/run; chown -R root:root /data/apps/dbus-serialbattery"
ssh root@192.168.1.11 "/data/apps/dbus-serialbattery/enable.sh"
powershell $PSScriptRoot\log.ps1



