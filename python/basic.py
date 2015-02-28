#!/usr/bin/python
# basic.py
# Common definition
#
# Author: Zex <top_zlynch@yahoo.com>
#
JM_SERVICE_NAME     = "org.juicemachine"
JM_DEV_IFACE        = "org.juicemachine.dev.iface"
JM_JSON_IFACE       = "org.juicemachine.json.iface"
JM_CONFIG_PATH      = "/org/juicemachine/config"

JM_NAME_IFACE       = "org.juicemachine.name.iface"
JM_ID_IFACE         = "org.juicemachine.id.iface"

NVRAM_DEV   = "/dev/nvram"
JSON_PATH   = "/tmp/juicemachine.json"

LOG_PREF    = "LOG>"

def LOG(*msg):

    print(LOG_PREF, *msg)


class Settings:
    """
    Settings

    'auto'      => boolean
    'name'      => string
    'url'       => string
    'allows'    => list of string
    """

    __slots__ = [
        'auto',
        'name',
        'url',
        'allows'
        ]

    def __init__(self):

        self.auto = True
        self.name = ""
        self.url = ""
        self.allows = []

    def __call__(self, *args):

        try:
            
            [LOG(getattr(self, x)) for x in self.__all__]

        except Exception as e:

            LOG("ERR!", e)


class SelftestAbc:
    """
    Common selftest definition
    """

    __all__ = []

    def __init__(self, odir='/tmp'):

        self.odir = odir
        self.setup()

    def setup(self):

        if not isdir(self.odir):
            mkdir(self.odir)

    def __call__(self, *args):

        try:
            
            [getattr(self, x)(LOG('<<<<<<<<<<<<',x,'>>>>>>>>>>>>>>')) for x in self.__all__]

        except Exception as e:

            LOG("ERR!", e)
