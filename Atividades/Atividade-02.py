print("Decimal    Octal     Hexadecimal     Binario")
print("-------- --------- --------------- ------------")

count = 0

while count<256:
    print("  ",count,"      ",oct(count),"       ",hex(count),"          ",bin(count))
    count=count+1