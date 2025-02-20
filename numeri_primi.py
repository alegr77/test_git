numeri = [2, 5, 8, 11, 14, 17, 20, 23, 28, 29, 32, 37, 40, 41, 44, 47, 50, 53, 56, 59]


def numeri_primi(x):
    if x <= 1:
        return False
    for i in range(2, int(x ** 0.5) +1):
        if x % i == 0:
            return False
    return True
    
numeri_primi = list(filter(numeri_primi, numeri))

print(numeri_primi)