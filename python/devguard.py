#!/usr/bin/python
# devguard.py
#
# Device monitoring
#
# Author: Zex <top_zlynch@yahoo.com>
#
import pyudev
#from pyudev import MonitorObserver
#from gi.overrides import GObject as gobject
import gobject
from pyudev.glib import GUDevMonitorObserver

def on_dev_changed(action, device):

    with open('/tmp/device-changed', 'a') as fd:

        fd.write(str(action)+'\n')
        [fd.write(str(item)+'\n') for item in device.items()]

context = pyudev.Context()

for dev in context.list_devices(DEVTYPE='disk'):
    for attr in ['device_node', 'device_number', 
        'device_path', 'device_type', 'driver']:
        print(attr, getattr(dev, attr))
    print('device_links', [l for l in dev.device_links])
    print('-------------------------------------')

monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('block')

observer = GUDevMonitorObserver(monitor)
observer.connect('device-changed', on_dev_changed)
monitor.start()
gobject.MainLoop().run()


