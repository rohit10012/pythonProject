

import random
n = random.randint(1, 100)
q = 0
while q != n:
    q = eval(input("Enter the number"))
    if q == n:
        print("Congratulations you have guessed it right!!")
    elif q > n:
        print("Number is too large")
    else:
        print("Number is too small")

