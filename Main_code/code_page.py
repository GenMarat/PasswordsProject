import csv

def menu():
    print('1) Create a new user ID')
    print('2) Change a password')
    print('3) Display all user IDs')
    print('4) Quit')
    while True:
        user_choice = input('Enter selection: ')
        if user_choice in ['1', '2', '3', '4']:
            break
        else:
            print('Incorrect choice')
    return user_choice

def password_score(password: str) -> str: #Проверяет надежность пароля. Возвращает оценку от 0-5
    score = 0
    temp = 0
    if len(password) >= 8: #проверка длины пароля
        score += 1
    for i in password: #начилие букв верхнего регистра
        if i.isupper() == True:
            temp += 1
    if temp > 0:
        score += 1
    temp = 0
    for i in password: #начилие букв нижнего регистра
        if i.islower() == True:
            temp += 1
    if temp > 0:
        score += 1
    temp = 0
    for i in password: #наличие цифр
        if i.isnumeric() == True:
            temp += 1
    if temp > 0:
        score += 1
    temp = 0
    for i in password: #наличие спецсимволов
        if i in ['!', '$', '%', '&', '<', '*', '@']:
            temp += 1
    if temp > 0:
        score += 1
    return score

def password():
    while True:
        password = input('Enter a password: ')
        score = password_score(password)
        if score in [1, 2]:
            print('Too simple password')
        elif score in [3, 4]:
            print('Password can be improved')
            answer = input('Do you want to improve it? (y/n): ')
            if answer == 'y':
                print()
            else:
                break
        else:
            print('This is good password')
            break
    return password

