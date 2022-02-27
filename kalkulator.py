#kalkulator v.1

działanie = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: \n')
num1 = int(input('Podaj pierwszą liczbe:'))
num2 = int(input('Podaj drugą liczbe:'))

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

if działanie == '1':
    print (f'Wynik działania: ' , add(num1,num2))

if działanie == '2':
    print (f'Wynika działania: ' , sub(num1,num2))

if działanie == '3':
    print (f'Wynika działania: ' , mul(num1,num2))

if działanie == '4':
    print (f'Wynik działania: ' , div(num1,num2))

