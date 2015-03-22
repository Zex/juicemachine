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
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('block')

observer = GUDevMonitorObserver(monitor)
observer.connect('device-changed', on_dev_changed)
monitor.start()

gobject.MainLoop().run()


