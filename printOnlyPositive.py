#print only positive and brak on zero
sum = 0
while True:
    n = int(input("Enter the number"))
    if n == 0:
        break
    elif n < 0:
        continue
    else:
        sum = sum + n
        continue
print(sum)

