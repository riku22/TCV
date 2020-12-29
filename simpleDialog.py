﻿# -*- coding: utf-8 -*-
#Simple dialog

import wx
import ctypes
import sys

def dialog(title, message):
	dialog = wx.MessageDialog(None,message,title,wx.OK)
	dialog.ShowModal()
	dialog.Destroy()
	return

def yesNoDialog(title, message):
	dialog = wx.MessageDialog(None,message,title,wx.YES_NO)
	result = dialog.ShowModal()
	dialog.Destroy()
	return result

def errorDialog(message):
	dialog = wx.MessageDialog(None,message,"error",wx.OK|wx.ICON_ERROR)
	dialog.ShowModal()
	dialog.Destroy()
	return

def debugDialog(message):
	if hasattr(sys, "frozen") == False:
		dialog = wx.MessageDialog(None,str(message),"debug",wx.OK)
		dialog.ShowModal()
		dialog.Destroy()
		return

def winDialog(title,message):
	ctypes.windll.user32.MessageBoxW(0,message,title,0x00000040)

def simpleDialog(title,message):
	ctypes.windll.user32.MessageBoxW(0,message,title,0x00000040)
