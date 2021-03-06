# -*- coding: UTF-8 -*-

import win32api
import win32gui
import win32con
import os


def setwallpaper(pic):
    # open register
    regkey = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)
    win32api.RegSetValueEx(regkey, "WallpaperStyle", 0, win32con.REG_SZ, "0")
    win32api.RegSetValueEx(regkey, "TileWallpaper", 0, win32con.REG_SZ, "0")
    # refresh screen
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, pic, win32con.SPIF_SENDWININICHANGE)


setwallpaper(os.path.dirname(os.getcwd()) + "\\cache\\cache.jpg")
