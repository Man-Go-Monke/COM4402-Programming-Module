sentence = input("enter a sentence")
sentence = sentence.lower()
char = 0
for ch in sentence:
        char += 1
        if ch in " ":
            char -= 1
print(f"{char}")