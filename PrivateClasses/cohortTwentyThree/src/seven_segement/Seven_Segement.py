def display(hex_num):
    if hex_num & 1 == 1:
        return '#'
    else:
        return ' '

def A(hex_num):
    return display(hex_num >> 6)

def B(hex_num):
    return display(hex_num >> 5)

def C(hex_num):
    return display(hex_num >> 4)

def D(hex_num):
    return display(hex_num >> 3)

def E(hex_num):
    return display(hex_num >> 2)

def F(hex_num):
    return display(hex_num >> 1)

def G(hex_num):
    return display(hex_num)


class Seven_Segment:
    hex_num = 0x30
    while(True):
        option = '''
        Display 1 -> Press 1
        Display 2 -> Press 2
        Display 3 -> Press 3
        Display 4 -> Press 4
        Display 5 -> Press 5
        Display 6 -> Press 6
        Display 7 -> Press 7
        Display 8 -> Press 8
        Display 9 -> Press 9
        Display 0 -> press 0
        Display A -> press A
        Display B -> press B
        Display C -> press C
        Display D -> press D
        Display E -> press E
        Display F -> press F  
    '''

        print(option)
        choice = input("Enter a valid character : ")

        if choice == "1":
            hex_num = 0x30
        elif choice == "2":
            hex_num = 0x6D
        elif choice == "3":
            hex_num = 0x79
        elif choice == "4":
            hex_num = 0x33
        elif choice == "5":
            hex_num = 0x5B
        elif choice == "6":
            hex_num = 0x5F
        elif choice == "7":
            hex_num = 0x70
        elif choice == "8":
            hex_num = 0x7F
        elif choice == "9":
            hex_num = 0x7B
        elif choice == "0":
            hex_num = 0x7E
        elif choice == "a":
            hex_num = 0x77
        elif choice == "b":
            hex_num = 0x1F
        elif choice == "c":
            hex_num = 0x4E
        elif choice == "d":
            hex_num = 0x3D
        elif choice == "e":
            hex_num = 0x4F
        elif choice == "f":
            hex_num = 0x47
        else:
             print("Please use a valid input display")



        print(f"  {A(hex_num)}{A(hex_num)}")
        print(f"{F(hex_num)}    {B(hex_num)}")
        print(f"{F(hex_num)}    {B(hex_num)}")
        print(f"  {G(hex_num)}{G(hex_num)}")
        print(f"{E(hex_num)}    {C(hex_num)}")
        print(f"{E(hex_num)}    {C(hex_num)}")
        print(f"  {D(hex_num)}{D(hex_num)}")


        # print("  ## ")
        # print("#    #")
        # print("#    #")
        # print("  ## ")
        # print("#    #")
        # print("#    #")
        # print("  ## ")

