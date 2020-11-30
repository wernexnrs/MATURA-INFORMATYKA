str = '1000'

print(int(str,2)) # decimal -> binary  
print(int(str,8)) # decimal -> octal  
print(int(str,16)) # decimal -> hexadecimal 

binary = '1000' # 8 - dec

print(int(binary,2)) # binary -> decimal


octal = '0100' # 64 - dec

print(int(octal,8)) # octal -> decimal

hex = 'FFFF' # 65535 - dec

print(int(hex,16)) # hexadecimal -> decimal
