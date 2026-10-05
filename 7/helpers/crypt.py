
def ceaser_crypt(filename:str):
    alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    with open(filename, "r") as file:
        encrypted_text = []
        text = file.readlines()
        for line_num in range(len(text)):
            new_line = ""
            for char in text[line_num]:
                if char.lower() in alphabet:
                    char_ind = alphabet.find(char.lower())
                    if char.isupper():
                        new_line += alphabet[char_ind-(line_num+1)].upper()
                    else:
                        new_line += alphabet[char_ind-(line_num+1)]
                    continue
                new_line += char
            encrypted_text.append(new_line)
    return encrypted_text