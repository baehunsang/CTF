from Crypto.Util.number import *

num = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
print(bytes.fromhex(hex(num)[2:]).decode())
print(long_to_bytes(num).decode())