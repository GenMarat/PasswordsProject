import csv

def menu():
    while True:
        print('1) Create a new user ID')
        print('2) Change a password')
        print('3) Display all user IDs')
        print('4) Quit')
        user_choice = input('Enter selection: ')
        if user_choice in ['1', '2', '3', '4']:
            break
        else:
            print('Incorrect choice')
            print()
    return user_choice

def score_pass(password: str) -> str: #Проверяет надежность пароля. Возвращает оценку от 0-5
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
        score = score_pass(password)
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

#запрашивает ID -> открывает файл на чтение -> получает ID из базы -> ищет на вхождение ID пользователя ->
#возвращет ID, если нет в базе данных / сообщает об задвоение и запрашивает повторно ID

def id_verification():
    file = csv.reader(open('id_file.csv', 'r'))
    while True:
        id_user = input('Enter ID: ')
        list_id = []
        for i in file:
            list_id.append(i)
        if id_user in list_id:
            print('Such a ID already exists')
        else:
            break
    return list_id #временно


def main():
    file = open('id_file.csv', 'w')
    file.close()

if __name__ == '__main__':
    main()
    x = id_verification()
    print(x)
