import pyperclip
import keyboard


# Класс для хранения глобальных переменных
class per:
    count1 = 0
    count2 = 0
    regi = ''

# подсчёт длины строчки
with open('Рабочий.txt', newline='', encoding="utf-8") as file:
    # подсчет длины

    for x in file:
        per.count1 += 1


# Копирует текст из буфера обмена, соединяет с предыдущей строкой и вставляет в буфер обмена новую строку
def new_region():
    try:
        street = pyperclip.paste() # Забирает из буфера обмена
        with open('result.txt', 'a', encoding="utf-8", ) as res_file:
            res_file.write(f'{per.regi.strip()} {street}\n')
            print(f"Строка {per.regi.strip()} {street} вставлена")
            print(f"Прошло - {per.count2}, Осталось - {per.count1 - per.count2}")

        with open('Рабочий.txt', newline='', encoding="utf-8") as file:
            list_req = [x for x in file]
            res = list_req[per.count2]
            res = res.replace('\r\n', '')
            per.regi = list_req[per.count2]
            pyperclip.copy(res)
            per.count2 += 1


    except:
        print('Ошибка!')
        pass

# Берёт первую строчку из файла
def first_word():
    with open('Рабочий.txt', newline='', encoding="utf-8") as file:
        list_req = [x for x in file]
        res = list_req[per.count2]
        res = res.replace('\r\n', '')
        per.regi = list_req[per.count2]
        pyperclip.copy(res)
        per.count2 += 1


# Следит за нажатыми клавишами
keyboard.add_hotkey("ctrl+3", new_region)
keyboard.add_hotkey('ctrl+5', first_word)
keyboard.wait()

