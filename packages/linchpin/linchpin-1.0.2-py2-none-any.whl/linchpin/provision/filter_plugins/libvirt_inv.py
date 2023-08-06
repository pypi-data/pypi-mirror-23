#!/usr/bin/env python

import os
import sys
import abc
import StringIO
from ansible import errors
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser
from InventoryFilters import LibvirtInventory

filepath = os.path.realpath(__file__)
filepath = "/".join(filepath.split("/")[0:-2])
sys.path.append(filepath)


class FilterModule(object):
    ''' A filter to fix interface's name format '''

    def filters(self):

        inv = LibvirtInventory.LibvirtInventory()
        return {
            'libvirt_inv': inv.get_inventory
        }
