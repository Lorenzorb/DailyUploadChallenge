# Determine if palindrome

text = "tacocat"

r_text = ""

for i in range(len(text)):
    r_text += text[-1-i]

if(text.lower() == r_text.lower()):
    print("Is Palindrome")
else:
    print("Is not Palindrome")
