from SingleDDT import singleDDT

# Author: Osman Tayfun Yelim
# Date: 15.12.2016


def completeUB():#UB : Undisturbed Bits

    l_sboxes = [[0,8,6,13,5,15,7,12,4,14,2,3,9,1,11,10],#S0
               [15,12,2,7,9,0,5,10,1,11,14,8,6,13,3,4], #S1
               [8,6,7,9,3,12,10,15,13,1,14,4,0,11,5,2], #S2
               [11,9,4,14,0,15,10,13,6,12,5,7,3,8,1,2], #S3
               [14,4,11,2,3,8,0,9,1,10,7,15,6,12,5,13], #S4
               [7,10,2,12,4,8,15,0,5,9,1,14,3,13,11,6], #S5
               [7,2,12,5,8,4,6,11,14,9,1,15,13,3,10,0], #S6
               [1,4,11,13,12,3,7,14,10,15,6,8,0,5,9,2], #S7
               [0,10,4,15,12,7,2,8,13,14,9,11,5,6,3,1]] #S8

    while True:
        l_input = input("Chose an s-box(0-8) or type end: ")
        if l_input != "":
            if l_input.strip('\t\n\r') == "end":
                return
            else:
                if l_input.isnumeric():
                    l_intinput = int(l_input)
                    if l_intinput <9 and l_intinput>-1:
                        print(" ~~~~~~~~~~Undisturbed Bits of S-BOX {}~~~~~~~~~~\n".format(l_intinput))
                        singleUB(l_sboxes[l_intinput])


def singleUB(p_sbox): #UB : Undisturbed Bits

    get_bin = lambda x, n: format(x, 'b').zfill(n)
    l_tempArray = ["" for x in range(16)]
    l_counter = 0
    DDT = singleDDT(p_sbox)
    for i in range(1,16): # input diff
        for j in range(0,16): # output diff
            if DDT[i][j] != 0:
                l_tempArray[l_counter] = get_bin(j,4)
                l_counter += 1
        findUB(l_tempArray,i)
        print("\n")
        l_counter = 0

def findUB(p_tempArray,p_inpDiff):
    counter = 0
    temp = ["?","?","?","?"]
    for i in range(0,16):
        if p_tempArray[i] == "":
            break
        counter += 1
    for j in range(0,4):
        for k in range(0,counter):
            if p_tempArray[0][j] != p_tempArray[k][j]:
                break
            else:
                if k == counter -1:
                    temp[j] = p_tempArray[k][j]
    print("For Input Difference {},  Undisturbed Bits: {}".format(p_inpDiff, temp))


completeUB()
