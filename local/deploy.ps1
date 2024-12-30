ssh root@192.168.2.112 "rm -rf /data/apps/dbus-serialbattery/; mkdir -p /data/apps/"
scp -r .\dbus-serialbattery\ root@192.168.2.112:/data/apps/
scp .\local\config.ini root@192.168.2.112:/data/apps/dbus-serialbattery/config.ini
ssh root@192.168.2.112 "chmod +x /data/apps/dbus-serialbattery/*.sh; chmod +x /data/apps/dbus-serialbattery/*.py; chmod +x /data/apps/dbus-serialbattery/service/run; chmod +x /data/apps/dbus-serialbattery/service/log/run; chown -R root:root /data/apps/dbus-serialbattery"
ssh root@192.168.2.112 "/data/apps/dbus-serialbattery/enable.sh"
powershell $PSScriptRoot\log.ps1



