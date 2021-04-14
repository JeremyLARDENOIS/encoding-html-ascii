import json

data = {"foo": "bar"}

text_to_encode = json.dumps(data)

text_encoded = "" 

for char in text_to_encode:
    text_encoded += "%" + hex(ord(char))[2:]

print (text_encoded)