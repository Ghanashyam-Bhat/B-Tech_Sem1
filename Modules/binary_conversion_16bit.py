def binary_def(the_number):
    while True:
        the_number = int(the_number)
        binary_non_list = ""
        quotient = the_number
        while quotient != 1:
            remainder = quotient % 2
            quotient = quotient // 2
            binary_non_list += str(remainder)
            binary_non_list += " "
        binary_non_list += "1"
        binary = binary_non_list.split(" ")
        binary.reverse()
        zero = binary.count("0")
        one = binary.count("1")
        z = zero + one
        n = 16 - z
        while n != 0:
            binary.insert(0, "0")
            n -= 1
        converted = ""
        for i in binary:
            converted += i
        return converted
