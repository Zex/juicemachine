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

    dev_iface = dbus.Interface(obj,
        JM_DEV_IFACE)

    json_iface = dbus.Interface(obj,
        JM_JSON_IFACE)

    print obj.Introspect()
    print dev_iface.list()
    print json_iface.list()

start_request()
