dec_numbers = [15,12,2,4,7,8]

dec_TO_bin = [bin(i)[2:] for i in dec_numbers]
dec_TO_hex = [hex(i)[2:] for i in dec_numbers]

bin_TO_dec = [int(i,2) for i in dec_TO_bin]
hex_TO_dec = [int(i,16) for i in dec_TO_hex]
