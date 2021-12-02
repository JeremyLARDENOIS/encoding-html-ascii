import json

# data = "pornhub.com"

#text_to_encode = json.dumps(data)
text_to_encode = "pornhub.com"


text_encoded = "" 

for char in text_to_encode:
    text_encoded += "%" + hex(ord(char))[2:]

print ("https://" + text_encoded)
