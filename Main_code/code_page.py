def password_test(password: str) -> str: #Проверяет надежность пароля. Возвращает оценку от 0-5
    score = 0
    temp = 0
    if len(password) >= 8: #проверка длинны пароля
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
