while 1:
    array = []
    bin_array = []
    number = ''
    while number != 'end':
        number = (input('enter the decade number(type end for finish): '))
        if number != 'end':
            try:
                int_number = int(number)
                if int_number >= 0:
                    if int_number not in array:
                        array.append(int_number)
                        bin_num = bin(int_number)
                        result_bin = ''
                        for i in range(len(bin_num)):
                            if i != 0 and i != 1:
                                result_bin += bin_num[i]
                        bin_array.append(result_bin)
                    else:
                        print("number already in set")
                else:
                    print("decade number can't be negative")
            except ValueError:
                print("number can't contain a letters")
        else:
            break
    for q in range(len(array)):
        print("decade set is: \t\t", "binary set is: ")
        print(array[q], "\t\t\t\t\t", bin_array[q])
