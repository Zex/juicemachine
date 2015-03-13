import pyudev
from pyudev import MonitorObserver
from gi.overrides import GObject as gobject

def device_changed():

    from os import mkdir

    mkdir('/tmp/device-changed')

context = pyudev.Context()
monitor = pyudev.Monitor.from_netlink(context)
monitor.filter_by('block')
observer = MonitorObserver(monitor, device_changed)

#observer.connect('device-changed', device_changed)
#observer.start()

#monitor.enable_receiving()
#gobject.MainLoop().run()


