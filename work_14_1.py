import random
def ask_question(question):
    print(question, '(Да/Нет):')
    answer = input()
    if answer == 'Да':
        return True
    else:
        return False

def generate_password(length, chars):
    password = ''
    for i in range(length):
        random_index = random.randint(0, len(chars) - 1)
        password += chars[random_index]
    return password
def password_new():
    print('Генератор паролей.\nОтветьте на уточняющие вопросы.')
    print('Введите длину пароля:')
    length = int(input())
    digits_enabled = ask_question('Включать ли цифры?')
    latin_lowercase_enabled = ask_question('Включать ли строчные латинские буквы?')
    latin_uppercase_enabled = ask_question('Включать ли заглавные латинские буквы?')
    russian_lowercase_enabled = ask_question('Включать ли строчные русские буквы?')
    russian_uppercase_enabled = ask_question('Включать ли заглавные русские буквы?')
    punctuation_enabled = ask_question('Включать ли знаки пунктуации?')

    enabled_chars = ''
    latin_uppercase_letters = 'AEIOUYBCDFGHJKLMNPQRSTVWXYZ'
    latin_lowercase_letters = 'aeiouybcdfghjklmnpqrstvwxyz'
    russian_lowercase_letters = 'абвгдеёжз​ийклмнопрстуфхцчшщъыьэюя'
    russian_uppercase_letters = 'АБВГДЕЁЖЗ​ИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    punctuation = '!#$&*+-=?@^_'
    digits = '1234567890'

    if digits_enabled:
        enabled_chars += digits
    if latin_uppercase_enabled:
        enabled_chars += latin_uppercase_letters
    if latin_lowercase_enabled:
        enabled_chars += latin_lowercase_letters
    if russian_lowercase_enabled:
        enabled_chars += russian_lowercase_letters
    if russian_uppercase_enabled:
        enabled_chars += russian_uppercase_letters
    if punctuation_enabled:
        enabled_chars += punctuation
    password = generate_password(length, enabled_chars)
    print(password)
    print('Сгенерировать пароль? (Да/Нет) ')
    answer = input()
    if answer == 'Да':
        password_new()
password_new()



