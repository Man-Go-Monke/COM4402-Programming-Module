reverse = ""
Word = input("Give me a word")
Length = len(Word)


for i in range (Length -1, -1, -1):
    reverse += Word[i]

print(reverse)
