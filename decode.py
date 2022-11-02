#!/usr/bin/python3

'''Allow to decode encoded string'''


def main():
    """main function"""
    text_encoded = input("Text encoded: ")
    text_decoded = ""
    i = 0
    while i < len(text_encoded):
        if text_encoded[i] == '%':
            text_decoded += chr(int(text_encoded[i+1:i+3], 16))
            i += 3
        else:
            text_decoded += text_encoded[i]
            i += 1

    print(text_decoded)


main()
