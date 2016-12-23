import numpy as np

def completeLAT():

    l_sboxes = [[0,8,6,13,5,15,7,12,4,14,2,3,9,1,11,10], #S0
                [15,12,2,7,9,0,5,10,1,11,14,8,6,13,3,4], #S1
                [8,6,7,9,3,12,10,15,13,1,14,4,0,11,5,2], #S2
                [11,9,4,14,0,15,10,13,6,12,5,7,3,8,1,2], #S3
                [14,4,11,2,3,8,0,9,1,10,7,15,6,12,5,13], #S4
                [7,10,2,12,4,8,15,0,5,9,1,14,3,13,11,6], #S5
                [7,2,12,5,8,4,6,11,14,9,1,15,13,3,10,0], #S6
                [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2], #S7
                [0,10,4,15,12,7,2,8,13,14,9,11,5,6,3,1]] #S8

    while True:
        l_input = input("Chose an s-box(0-8) or type end : ")
        if l_input != "":
            if l_input.strip('\t\n\r') == "end":
                return
            else:
                if l_input.isnumeric():
                    l_intinput = int(l_input)
                    if l_intinput <9 and l_intinput>-1:
                        print(" ~~~~~~~~~~LAT of S-BOX {}~~~~~~~~~~\n".format(l_intinput))
                        singleLAT(l_sboxes[l_intinput])

def singleLAT(p_sbox):

    l_lat = np.zeros(shape=(16,16))
    for k in range(0,16):
        for i in range(0,16):
            for j in range(0,16):
                l_lat[k,i] += innerProduct(k,j) ^ innerProduct(i,p_sbox[j])
    l_lat = l_lat - 8
    printLAT(l_lat)

# This function handles the operations such as 3.4 = 0("." being the inner product)
def innerProduct(p_num1, p_num2):
    get_bin = lambda x, n: format(x, 'b').zfill(n)
    strBinNum1 = get_bin(p_num1,4)
    strBinNum2 = get_bin(p_num2,4)
    counter = 0
    validBits = 0
    for bit in strBinNum1:
        if bit == "1":
            validBits += int(strBinNum2[counter])
        counter += 1
    validBits = validBits % 2
    return validBits


def printLAT(p_ddt):

    l_index = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

    print("    ",end = " ")
    for i in range(0,16):
        print("{} |".format(l_index[i]),end = " ")
    print("\n")

    for i in range(0,16):
        print("{} |".format(l_index[i]),end = " ")
        for j in range(0,16):
            print("{} |".format(int(p_ddt[i][j])),end=" ")
        print("\n")

completeLAT()
