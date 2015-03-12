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
import threading

def start_request():
    """
    Start sending requests to server
    """
    connection = dbus.SessionBus()

    obj = connection.get_object(
        JM_SERVICE_NAME,
        JM_CONFIG_PATH)

    print obj.Introspect()

    prof_iface = dbus.Interface(obj, JM_PROFILE_IFACE)
    print(prof_iface.get_comment())

start_request()
