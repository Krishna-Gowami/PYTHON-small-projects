decNum = int(input("Enter a decimal number: "))
rem = 0
currNum = decNum
binarryArr = []

while currNum != 1:
    rem = currNum % 2
    currNum = currNum//2
    binarryArr.append(rem)
binarryArr.append(currNum)

binary = "".join(str(value) for value in binarryArr[-1::-1])
print(f"binary equivalent of {decNum} = {binary}")