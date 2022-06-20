
'''
import time
while True:
    time.sleep(10)
    break
##another program

#!/usr/bin/python3

import time
print("Start : %s" % time.ctime())
#time.sleep( 5 )
#text = input("Enter a string: ")
text = "Rohit"
i = 0
while i < len(text):
    ch = text[i]
    i += 1
    if ch in "aeiouAEIOU":
        continue
    print(ch, end="")
print("\nEnd : %s" % time.ctime())
'''

import time
start_time = time.time()
text = "Rohit"
time.sleep(1)
i = 0
while i < len(text):
    ch = text[i]
    i += 1
    if ch in "aeiouAEIOU":
        continue
    print(ch, end="")
print("--- %s seconds ---" % (time.time() - start_time))