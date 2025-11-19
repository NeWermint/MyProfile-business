# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone = ''
email = ''
index = ''
mail = ''
info = ''
# business info
OGRNIP = ''
ITN = ''
payment_account = ''
bank_name = ''
bic = ''
correspondent_account = ''


def general_info_user(name_parameter, age_parameter, phone_parameter, email_parameter, index_parameter, mail_parameter, info_parameter):
    print(SEPARATOR)
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19: years_parameter = 'лет'
    elif age_parameter % 10 == 1: years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4: years_parameter = 'года'
    else: years_parameter = 'лет'


    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    print('Почтовый индекс:', index_parameter)
    print('Почтовый адрес:', mail_parameter)
    if info:
            print('')
            print('Дополнительная информация:')
            print(info_parameter)

def business_info_user(OGRNIP, ITN, payment_account, bank_name, bic, correspondent_account):
    print('\nИнформация о предпринимателе')
    print('ОГРНИП:', OGRNIP)
    print('ИНН:', ITN)
    print('Банковские реквизиты')
    print('Р/c:', payment_account)
    print('Банк:', bank_name)
    print('БИК:', bic)
    print('К/с:', correspondent_account)

def OGRNIP_counting(OGRNIP):
    ORGNIP_copy = OGRNIP
    count = 0
    while ORGNIP_copy > 0:
        count += 1
        ORGNIP_copy //= 10
    return count
    
def payment_account_counting(payment_account):
    payment_account_copy = payment_account
    count = 0
    while payment_account_copy > 0:
        count += 1
        payment_account_copy //= 10
    return count
    
def index_filter(index):
    filtered_index = ''
    for symbol in index:
        for numbers in range(10):
            if str(numbers) == symbol:
                filtered_index += symbol
    return filtered_index

print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
            break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name = input('Введите имя: ')
                while 1:
                        # validate user age
                        age = int(input('Введите возраст: '))
                        if age > 0:
                            break
                        print('Возраст должен быть положительным')

                updated_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                phone = ''
                for character in updated_phone:
                    if character == '+' or ('0' <= character <= '9'):
                        phone += character


                email = input('Введите адрес электронной почты: ')
                index = input('Введите почтовый индекс: ')
                index = index_filter(index)
                mail = input('Введите почтовый адрес (без индекса): ')
                info = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input social links
                OGRNIP = int(input('Введите ОГРНИП: '))
                OGRNIP_numbers = OGRNIP_counting(OGRNIP)
                while OGRNIP_numbers != 15:
                    OGRNIP = int(input('Корректный ОГРНИП должен содержать 15 цифр: '))
                    OGRNIP_numbers = OGRNIP_counting(OGRNIP)
                ITN = int(input('Введите ИНН: '))
                payment_account = int(input('Введите номер расчетного счета: '))
                payment_account_numbers = payment_account_counting(payment_account)
                while payment_account_numbers != 20:
                    payment_account = int(input('Номер расчетного счета должен содержать 20 цифр: '))
                    payment_account_numbers = payment_account_counting(payment_account)
                bank_name = input('Введите название банка: ')
                bic = int(input('Введите БИК: '))
                correspondent_account = int(input('Введите номер корреспондентского счета: '))
            else: print('Введите корректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Общая информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone, email, index, mail, info)

            elif option2 == 2:
                general_info_user(name, age, phone, email, index, mail, info)
                

                business_info_user(OGRNIP, ITN, payment_account, bank_name, bic, correspondent_account)
            else:   print('Введите корректный пункт меню')
    else:       print('Введите корректный пункт меню')