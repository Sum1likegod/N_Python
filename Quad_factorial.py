def quad_divi(arr):
    for i in arr:
        lsi = []
        sum = 0
        for di in range(1, i + 1):
            if i % di == 0:
                lsi.append(di)
        if len(lsi) == 4:
            for el in lsi:
                sum += el
        if sum > 0:
            return sum


arr = []
len_arr = int(input("enter the length of array "))
for iu in range(0, len_arr):
    i = int(input(f'enter the element {iu + 1} '))
    arr.append(i)

print('the sum will be', quad_divi(arr))