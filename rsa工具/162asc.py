import os
import textwrap
from binascii import a2b_hex
f1= 0X6C6F76656C6F76656C6F76656C6F76656C6F76656C6F76656C6F76656C6F7665
f2= 0X0A031702560115110A140E0A1E300E0A1E300E0A1E30140C190D1F100E060318
f3 = f1^f2
f3 = hex(f3)
#
print(f3)
class Converter(object):
    @staticmethod
    def to_ascii(h):
        list_s = []
        for i in range(0, len(h), 2):
            list_s.append(chr(int(h[i:i+2], 16)))
        return ''.join(list_s)
    def to_hex(s):
        list_h = []
        for c in s:
            list_h.append(str(hex(ord(c))[2:]))
        return ''.join(list_h)    
print(Converter.to_ascii('7ffcfba64a00'))