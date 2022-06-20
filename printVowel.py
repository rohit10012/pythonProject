#print file without vowels
'''
text = input("Enter a string: ")
i = 0
while i < len(text):
    ch = text[i]
    if ch not in "aeiouAEIOU":
        print(ch, end="")
    i += 1
'''

#method 2 for this same program using continue

text = input("Enter a string: ")
i = 0
while i < len(text):
    ch = text[i]
    i += 1
    if ch in "aeiouAEIOU":
        continue
    print(ch, end="")



