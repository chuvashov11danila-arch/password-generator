#подключаем модуль 'random'
import random
#создаём функцию 
def generated_passwords(count_password, len_def_password, include_digits, include_lowercase_letters, include_uppercase_letters, include_punctuation, exclude_ambiguous):
    #Создайте строковые константы
    digits = '0123456789'
    lowercase_letters ='abcdefghijklmnopqrstuvwxyz'
    uppercase_letters ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_.'
    #Создайте переменную, которая будет содержать символы 
    chars = ''
    #Проверка ввода 
    if include_digits == 'да':
        chars += digits
    else:
        pass
    if include_lowercase_letters == 'да':
        chars += lowercase_letters
    else:
        pass
    if include_uppercase_letters == 'да':
        chars += uppercase_letters
    else:
        pass
    if include_punctuation == 'да':
        chars += punctuation
    else:
        pass
    if exclude_ambiguous == 'да':
        for c in 'il1Lo0O':
            chars = chars.replace(c, '')
    #Ещё одна проверка, чтобы не запускать каждый раз
    if count_password <= 0:
        print('Необходимо ввести количество больше 0')
        return []
    elif count_password > 10:
        print('Вы превысили лимит!!!')
        return []
    if len_def_password < 1:
        print('Длина должна быть больше 0!!!')
        return []


    if len_def_password >= 101:
        print('Вы превысили лимит!!!')
        return []
    #Создаём итоговый список 
    result_password = []
    #Создаём цикол для количества 
    for _ in range(count_password):
        # Создаём временный список 
        time_password = []
        # Создаём цикол для проверки длины
        for _ in range(len_def_password):
            time_password.append(random.choice(chars))
        one_password = ''.join(time_password)
        result_password.append(one_password)
    return result_password
# Ввод  
count_password = int(input('Количество паролей для генерации[от 1 до 10]:'))
len_def_password = int(input('Длину одного пароля[от 0 до 100]:'))
include_digits = input('Включать ли цифры?[Да/Нет]:').lower()
include_lowercase_letters = input('Включать ли прописные буквы?[Да/Нет]:').lower()
include_uppercase_letters = input('Включать ли строчные буквы?[Да/Нет]:').lower()
include_punctuation = input('Включать ли символы?[Да/Нет]:').lower()
exclude_ambiguous = input('Исключать ли неоднозначные символы il1Lo0O?[Да/Нет]:').lower()
print(generated_passwords(count_password, len_def_password, include_digits, include_lowercase_letters, include_uppercase_letters, include_punctuation,exclude_ambiguous))

