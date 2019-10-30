# Loop to iterate through binary strings and convert them to their respective binary, decimal and hexadecimal format.

for i in ["00000000", "00000010", "00000100", "01010101", "11110010", "11111111"]:
    # Hex format. Outputs the number in base 16, using upper- case letters for the digits above 9.
    print("{0} | {1:3} | {2:2x}".format(i, int(i, 2), int(i, 2)))
