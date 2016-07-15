from ctypes import CDLL, c_void_p
from ctypes.util import find_library

library = find_library("xenctrl")
libxenctrl = CDLL(library)

gntshr_open = libxenctrl.xc_gntshr_open
gntshr_open.restype = c_void_p

gntshr_close = libxenctrl.xc_gntshr_close
gntshr_close.argtypes = [c_void_p]

class GntshrHandle():
    def __init__(self):
        self.handle = gntshr_open()

    def close(self):
        gntshr_close(self.handle)
