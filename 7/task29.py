#todo: Взлом шифра
# Вы знаете, что фраза зашифрована кодом цезаря с неизвестным сдвигом.
# Попробуйте все возможные сдвиги и расшифруйте фразу.
import string

secret = "grznuamn zngz cge sge tuz hk uhbouay gz loxyz atrkyy eua'xk jazin."
alphabet = string.ascii_lowercase

for shift_value in range(len(alphabet)):
    result_text = ""
    for char in secret:
        if char.lower() in alphabet:
            char_ind = alphabet.find(char.lower())
            new_ind = (char_ind - shift_value) % len(alphabet)
            new_char = alphabet[new_ind]
            result_text += new_char
        else:
            result_text += char
            
    print(f"Сдвиг {shift_value}: {result_text}")
