#!/usr/bin/python
#
# jm_server.py
#
# Author: Zex <top_zlynch@yahoo.com>
#

import dbus 
import dbus.service
import dbus.mainloop.glib
import gobject

import json
from basic import * 

class JuiceMachine(dbus.service.FallbackObject):
    """
    JuiceMachine server
    """
    def __init__(self):

        connection = dbus.SessionBus()
        connection_name = dbus.service.BusName(
            JM_SERVICE_NAME, bus = connection)

        dbus.service.Object.__init__(self, connection_name,
            JM_CONFIG_PATH)

    @dbus.service.method(JM_DEV_IFACE,
            in_signature = '', out_signature = 's',
            path_keyword = 'path')
    def list(self, path = JM_CONFIG_PATH):
        """
        TODO: Return goods list
        """
        buf = ""
        try:
            with open(NVRAM_DEV, 'rw') as fd:
                buf = fd.read()
        except Exception as e:
            buf = str(e)

        return buf

    @dbus.service.method(JM_JSON_IFACE,
            in_signature = '', out_signature = 's',
            path_keyword = 'path')
    def list(self, path = JM_CONFIG_PATH):
        """
        TODO: Return goods list
        """
        buf = ""
        try:
            with open(JSON_PATH, 'rw') as fd:
                buf = fd.read()
        except Exception as e:
            buf = str(e)

        return buf


def start_server():
    """
    Stadrt juicemachine server
    """
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    global loop

    obj = JuiceMachine()
    loop = gobject.MainLoop()
    connection = dbus.StarterBus()

    loop.run()


start_server()
