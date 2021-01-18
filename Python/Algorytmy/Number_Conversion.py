dec_numbers = [15,12,2,4,7,8]

dec_TO_bin = [bin(i)[2:] for i in dec_numbers]
dec_TO_oct = [oct(i)[2:] for i in dec_numbers]
dec_TO_hex = [hex(i)[2:] for i in dec_numbers]


bin_TO_dec = [int(i,2) for i in dec_TO_bin]
oct_TO_dec = [int(i,8) for i in dec_TO_oct]
hex_TO_dec = [int(i,16) for i in dec_TO_hex]

#to_base(number,base)
BS="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def to_base(n, b): 
    return BS[n] if n < b else to_base(n // b, b) + BS[n % b]

def to_base2(s, b):
    res = ""
    while s:
        res+=BS[s%b]
        s//= b
    return res[::-1] or "0"

print(to_base(12, 16))
print(to_base2(12, 16))
