def remove_special_characters(text):
    new_text = ""
    for char in text:
        if char.isalpha():
            new_text += char
    return new_text
