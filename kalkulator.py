#kalkulator v.2

import logging


operation = int(input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: \n'))
num1 = float(input('Podaj skadnik 1 :'))
num2 = float(input('Podaj skadnik 2 :'))
logging.basicConfig(level=logging.DEBUG, format='')
def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mul(num1,num2):
    return num1 * num2

def div(num1,num2):
    if num2 == 0:
        return 'nie można dzielić przez zero'
    else:
        return num1 / num2

if operation == 1:
    logging.debug(f'Dodaje {num1} i {num2}')
    print (f'Wynik to : ' , add(num1,num2))

if operation == 2:
    logging.debug(f'Odemmuje {num2} od {num1}')
    print (f'Wynik to : ' , sub(num1,num2))

if operation == 3:
    logging.debug(f'Mnoze {num1} przez {num2}')
    print (f'Wynik to : ' , mul(num1,num2))

if operation == 4:
    logging.debug(f'Dziele {num1} przez {num2}')
    print (f'Wynik to : ' , div(num1,num2))

