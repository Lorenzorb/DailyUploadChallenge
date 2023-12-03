# How to reverse a string

text = "string to reverse"
r_text = ""

for i in range(len(text)):
    r_text += text[-1-i]

print(text)
print(r_text)
