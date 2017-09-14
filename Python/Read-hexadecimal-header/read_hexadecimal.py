#!/usr/bin/python
# -*- coding: utf-8 -*-

def header_while (path_to_copy_from):
	header = ""
	byte_list = ""
	with open(path_to_copy_from, 'rb') as f:
		key = True
		while key:
			byte = f.read(1)
			byte_list += byte + " "
			if hex(ord(byte))[2:] == "a":
				key=False
			header += hex(ord(byte))[2:] + " "
		print header[:-2]
		print byte_list

def header_while_scalpel (path_to_copy_from):
	header = "\\x"
	byte_list = ""
	with open(path_to_copy_from, 'rb') as f:
		key = True
		while key:
			byte = f.read(1)
			byte_list += byte + " "
			if hex(ord(byte))[2:] == "a":
				key=False
			header += hex(ord(byte))[2:] + "\\x"
		print header[:-5]
		print byte_list

def range_header(path_to_copy_from, x_range):
	header = ""
	with open(path_to_copy_from, 'rb') as f:
		for i in range(x_range):
			byte = f.read(1)
			header += hex(ord(byte))[2:] + " "
			print byte
			print header

path_to_copy_from = "test2.py"
x_range = 4

range_header(path_to_copy_from, x_range)
header_while(path_to_copy_from)
header_while_scalpel(path_to_copy_from)