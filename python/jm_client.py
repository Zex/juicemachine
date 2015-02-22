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

    print obj.Introspect()

#    dev_iface = dbus.Interface(obj,
#        JM_DEV_IFACE)
#    print dev_iface.list()

    json_iface = dbus.Interface(obj, JM_JSON_IFACE)
    print json_iface.list()

    print dbus.Interface(obj, JM_NAME_IFACE).get_name()
    print dbus.Interface(obj, JM_ID_IFACE).get_id()

start_request()
