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

def id_verification():
    file = csv.reader(open('id_file.csv', 'r'))
    list_id = []
    while True:
        id_user = input('Enter ID: ')
        for i in file:
            list_id.append(i[0])
        if id_user in list_id:
            print('Such a ID already exists')
        else:
            break
    return id_user

def id_insert():
    file = csv.reader(open('id_file.csv', 'r'))
    list_id = []
    while True:
        id_user = input('Enter ID: ')
        for i in file:
            list_id.append(i[0])
        if id_user in list_id:
            break
        else:
            print('ID is not in the list')
    return id_user

def replace_pass(id, new_pass):
    file = csv.reader(open('id_file.csv', 'r'))
    list_id_pass = []
    for i in file:
        list_id_pass.append(i)
    for x in list_id_pass:
        if x[0] == str(id):
            x[1] = new_pass
    file = open('id_file.csv', 'w')
    for y in list_id_pass:
        write = str(y[0]) + ',' + str(y[1])
        file.write(write + '\n')
    file.close()
    print('Password changed')

def create_id_pass(id, password):
    file = open('id_file.csv', 'a')
    write = str(id) + ',' + str(password)
    file.write(write + '\n')
    file.close()
    print('Your data is saved')

def show_ids():
    file = csv.reader(open('id_file.csv', 'r'))
    list_id_pass = []
    for i in file:
        print(i[0])

if __name__ == '__main__':
    while True:
        item_menu = menu()
        if item_menu == '1':
            id_user = id_verification()
            pass_user = password()
            create_id_pass(id_user, pass_user)
        elif item_menu == '2':
            id_user = id_insert()
            pass_user = password()
            replace_pass(id_user, pass_user)
        elif item_menu == '3':
            show_ids()
        else:
            break