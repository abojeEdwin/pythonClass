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