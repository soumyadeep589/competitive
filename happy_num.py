def is_happy_num(n):
    check = {}
    while(1):
        n = num_square_sum(n)
        if (n == 1):
            return True
        if n in check:
            return False
        check[n] = 1

def num_square_sum(n):
    square_sum = 0
    while(n):
        square_sum += (n % 10) * (n % 10)
        n = int(n / 10)
    return square_sum


print(is_happy_num(20))