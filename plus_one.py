def plusOne(digits):
        num = int("".join([str(elem) for elem in digits]))
        num_new = str(num + 1) 
        arr = list(map(int, list(num_new)))
        
        return arr


print(plusOne([1, 2, 3]))