text_encoded = input("Text encoded: ").split("%")[1:]
text_decoded = ""

for char in text_encoded:
    text_decoded += chr(int(char,16))

print (text_decoded)