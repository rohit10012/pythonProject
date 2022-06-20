
text = input("Enter a string: ")
i = 0
while i < len(text):
    ch = text[i]
    if ch not in "aeiouAEIOU":
        print(ch, end="")
    i += 1
