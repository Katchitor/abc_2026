#todo: Допишите для игры "Поле чудес" функции сохранения и загрузки игры через сериализацию.
# Данные сериализации записываются и сохраняются в файле.
import  random
import json


_dict = {'False': 'Логическое значение', 'None': 'Пустой'}
keys = list(_dict.keys())
ind = random.randint(0, len(keys) - 1)
secret = keys[ind]
mask = [' * '] * len(secret)


def save_game(_dict, secret, mask):
    save_data = {"dict": _dict, "secret": secret, "mask": mask}
    with open("save_data.json", "wt") as f:
        json.dump(save_data, f,ensure_ascii=False, indent=4)

def load_game():
    with open("save_data.json", "rt") as f:
        save_data = json.load(f)
    _dict=save_data["dict"]
    secret=save_data["secret"]
    mask=save_data["mask"]
    return _dict, secret, mask

def show_describe(_dict, secret):
    """ Выводит описание слова  """
    print(_dict[secret])


def show_secret(mask):
    """ Выводит слово """
    for val in mask:
       print(val, end="")


def get_letter():
    letter = input("\n Введите букву:")
    return letter


def check_letter(letter, secret, mask):
    for ind, val in enumerate(secret):
        if val.upper() == letter.upper():
            mask[ind] = f" {letter} "


def start():
    _dict, secret, mask = load_game()
    while ( " * " in mask):
        show_describe(_dict, secret)
        show_secret(mask)
        letter = get_letter()
        check_letter(letter, secret, mask)

start()