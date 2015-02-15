#!/usr/bin/python
#
# jm_client.py
#
# Author: Zex <top_zlynch@yahoo.com>
#

import dbus 
import dbus.service
import dbus.mainloop.glib
import gobject

from basic import * 

def start_request():
    """
    Start sending requests to server
    """
    connection = dbus.SessionBus()
    obj = connection.get_object(
        JM_SERVICE_NAME,
        JM_CONFIG_PATH)

    conf_iface = dbus.Interface(obj,
        JM_CONFIG_IFACE)

    print obj.Introspect()
    print conf_iface.list()

start_request()
