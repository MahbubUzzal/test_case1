def welcoming_you(name):
    your_name = get_greetings(name)
    print(your_name)


def get_greetings(name):
    sur_name = f'Welcome home {name}!!!'
    return sur_name


def adi(a, b):
    return a + b


def divide(a, b):
    if b != 0:
        result = a / b
        return result
    else:
        raise ZeroDivisionError('Error: Divsion by Zero is not allowed')


def fizz_buzz(n):
    for num in range(n):
        print(fizz_buzz_logic(num + 1))


def fizz_buzz_logic(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


# Call the function to execute Fizz-Buzz

def body_condition():
    hungry = input('Are you hungry? ').lower()
    hunger_status(hungry)


def hunger_status(hungry):
    if hungry == 'yes':
        need_energy = input('What are you going to eat? ').lower()
        if need_energy == 'pizza':
            print('Find a pizza shop near you!! ')
        elif need_energy == 'burger':
            print('Find a burger shop near you!! ')
        elif need_energy == 'salal':
            print('Go home and make some Salad yourself!!! ')
        else:
            print('Are you confused?')
    else:
        print('Are you thirsty?')


def spathi():
    spathiphyllum = input('What is the best plant ever?')
    if spathiphyllum == 'SPATHIPHYLLUM':
        print('Yes - Spathiphyllum is the best plant ever!')
    elif spathiphyllum == 'spathiphyllum':
        print('No, I want a big Spathiphyllum!')
    else:
        print('Spathiphyllum! Not [input]!')


def _sum(n):
    number_sum = 0
    index = 1
    while index <= n:
        number_sum += index
        index += 1
        return number_sum


blocks = int(input('Enter a number: '))





