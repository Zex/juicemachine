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
#from juicemachine_pb2 import *
#from timer import *

class DumpCtrl:

    def dump(self):

        print('dumping ...')
        return True

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

        obj = connection.get_object(
            JM_SERVICE_NAME, JM_CONFIG_PATH)

        obj.connect_to_signal(
            'set_comment', self.signal_cb,
            dbus_interface = JM_PROFILE_IFACE)

        dump_ctrl = DumpCtrl()
        gobject.timeout_add(10, dump_ctrl.dump)

    def signal_cb(self):

        print 'signal_cb ...'
    
    def get_buffer(self):
        """
        Get raw data from source
        """
        buf = ""
        try:
            with open(JSON_PATH, 'rw') as fd:
                buf = fd.read()
        except Exception as e:
            buf = str(e)

        return buf

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
        return self.get_buffer()

    @dbus.service.method(JM_NAME_IFACE,
            in_signature = '', out_signature = 's')
    def get_name(self):
        """
        TODO: Return goods list
        """
        buf = self.get_buffer()

        dc = json.JSONDecoder().decode(buf)
        
        if dc.has_key("name"):
            return dc["name"]

        return ""

    @dbus.service.method(JM_ID_IFACE,
            in_signature = '', out_signature = 's')
    def get_id(self):
        """
        TODO: Return goods list
        """
        buf = self.get_buffer()

        dc = json.JSONDecoder().decode(buf)
        
        if dc.has_key("id"):
            return dc["id"]

        return ""

    @dbus.service.method(JM_PROFILE_IFACE,
            out_signature = 'as')
    def get_comment(self):

        ret = [ 
                'great!',
                'not so good.',
                'one more',
              ]

        return ret

    @dbus.service.method(JM_PROFILE_IFACE)
    def set_comment(self):

        ret = [ 
                'great!',
                'not so good.',
                'one more',
              ]


def start_server():
    """
    Stadrt juicemachine server
    """
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    dbus.mainloop.glib.threads_init()

    global loop

    obj = JuiceMachine()
    loop = gobject.MainLoop()

    connection = dbus.StarterBus()

    print('looping ...')
    loop.run()

try:
    start_server()

except KeyboardInterrupt:

    print('keyboard int')

    global loop
    loop.quit()

