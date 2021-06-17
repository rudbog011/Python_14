import random
def is_valid_number(question, number):
    while True:
        print(question)
        user_input = input()
        if user_input.isdigit():
            user_number = int(user_input)
            if user_number >= number:
                return user_number
            else:
                continue
        else:
            continue
def ask_question(question):
    while True:
        print(question, '(Да/Нет):')
        answer = input()
        answer = answer.lower().strip()
        if answer == 'да':
            return True
        elif answer == 'нет':
            return False

def generate_password(length, chars):
    password = ''
    for i in range(length):
        random_index = random.randint(0, len(chars) - 1)
        password += chars[random_index]
    return password

def password_new(count, length):  
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
    for i in range(length - 1):
        password = generate_password(length, enabled_chars)
        print(password)
    
    answer = ask_question('Сгенерировать пароль?')
    if answer:
        print('Генератор паролей.\nОтветьте на уточняющие вопросы.')
        count = is_valid_number('Введите количество паролей от 1 и более:', 1)
        length = is_valid_number('Введите длину пароля от 4 и более:', 4)
        password_new(count, length)
    else:
        print('Спасибо!')
print('Генератор паролей.\nОтветьте на уточняющие вопросы.')
count = is_valid_number('Введите количество паролей от 1 и более:', 1)
length = is_valid_number('Введите длину пароля от 4 и более:', 4)
password_new(count, length)