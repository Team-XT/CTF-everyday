import gmpy2
import math
e="0x10001"
n="0x291733BAB061EF9C599139CB3E40A5C762B6F448FFFFFFFFFFFFFF"
m="0x237200C0F72B97DB55BA37C7AACBB61A26A0CB47D294726259C4DF"
ee=int(e,16)
nn=int(n,16)
mm=int(m,16)
print(ee,nn)
p=1578173871764844869716052171
q=10710927547195113973175047066215146269
ol=(p-1)*(q-1)
dd=gmpy2.invert(ee,ol)
plain=pow(mm,dd,nn)
plain=hex(plain)
#ans='{:x}'.format(plain).decode('hex')
print(plain)
