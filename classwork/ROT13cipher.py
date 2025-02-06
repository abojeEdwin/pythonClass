def encrypt_text(text):

    encrypted = ""
    shift = 13
    for chartext in text:
        if chartext.isupper():
                encrypted += chr((ord(chartext) + shift - 65) % 26 +65)
        elif chartext.islower():
            encrypted += chr((ord(chartext) + shift - 97) % 26 + 97)
        else:
            encrypted += chartext
    return encrypted




text = ("welcome,123")
print(encrypt_text(text))
