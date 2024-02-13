#---------------------------------- TASK 1 -------------------------------------------
#-------------------------------------------------------------------------------------

#ФУНКЦІЯ caching_fibonacci
def caching_fibonacci():
    #Створити порожній словник cache
    cache = dict()

    #ФУНКЦІЯ fibonacci(n)
    def fibonacci(n):
        #Якщо n <= 0, повернути 0
        if n <= 0:
            return 0
        #Якщо n == 1, повернути 1
        if n == 1:
            return 1
        #Якщо n у cache, повернути cache[n]
        if n in cache:
            return cache[n]
        # recursin
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    #Повернути функцію fibonacci
    return fibonacci
#КІНЕЦЬ ФУНКЦІЇ caching_fibonacci

fib = caching_fibonacci()

#print(fib(10))

#---------------------------------- TASK 2 -------------------------------------------
#-------------------------------------------------------------------------------------

import re

def generator_numbers(text):
    # Пошук потерну: пробіл цифри крапка цифри пробіл
    pattern = r" \d+\.\d+ "
    words_with_numbers = re.findall(pattern, text)
    sum = 0
    # сума чисел
    for word in words_with_numbers:
        sum += float(word)
    return sum

def sum_profit(text, func):
    return generator_numbers(text)

#використання
text = '''Загальний дохід працівника складається з декількох частин:
 1000.01 як основний дохід, доповнений додатковими 
 надходженнями 27.45 і 324.00 доларів.'''
total_income = sum_profit(text, generator_numbers)
#print(f"Загальний дохід: {total_income}")

#---------------------------------- TASK 3 -------------------------------------------
#-------------------------------------------------------------------------------------

import sys

def parse_log_line(line: str) -> dict:
    # створюємо пустий словник
    line_dic = dict()
     # записуємо частинки стрічки по різним елементам словнику
    line_dic['date'] = line.split()[0]
    line_dic['time'] = line.split()[1]
    line_dic['error_type'] = line.split()[2].lower()
    line_dic['message'] = ' '. join(line.split()[3:]) 
    return line_dic
    
def load_logs(file_path: str) -> list :
     # відкриваємо файл та створюємо список стрічок
    with open(file_path, "r") as fh:
        lines = [parse_log_line(el.strip()) for el in fh.readlines()]
    return lines
    
def filter_logs_by_level(logs: list, level: str) -> list:
     # перебираємо стрічки та створюємо список рядків, в яких співпадає левел
    list_by_log = [el for el in logs if el['error_type'] == level]
    return list_by_log

def count_logs_by_level(logs: list) -> dict:
     # перебираємо стрічки та створюємо словник: левел -> кількість повторів
    level_dic = dict()
    for log in logs:
        # якщо ключа з рівнем помилки нема, то ставимо значення 1, якщо є, то збільшуємо на 1
        if log['error_type'] not in level_dic:
            level_dic[log['error_type']] = 1
        else: 
            level_dic[log['error_type']] += 1
    return level_dic
    
def display_log_counts(counts: dict):
    print('Рівень логування \t| Кількість\n'+'\u2500' * 24+'+'+'\u2500' * 15)
    for i, j in counts.items():
        print(f'{i.upper()}\t\t\t| {j}')

if __name__=="__main__":
    try:
        filename=sys.argv[1] 
        logs=load_logs(file_path=filename)
        display_log_counts(count_logs_by_level(logs))
        # якщо в командному рядку ввели 3 аргументи, то фільтруємо за рівнем і виводимо
        if len(sys.argv)==3:
            level=sys.argv[2]
            logs=filter_logs_by_level(logs,level)
            print()
            print(f"Деталі логів для рівня '{level}':")
            print(''.join(map(lambda x:f"{x['date']} {x['time']} - {x['message']}\n",logs)))
    except FileNotFoundError:
        print('File not found')
    except:
        print('Input error')

#---------------------------------- TASK 4 -------------------------------------------
#-------------------------------------------------------------------------------------
        
#чи треба перевіряти, що номер - це цифри?

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "User not found."
        except IndexError:
            return "Give me name please."
    return inner


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

#Цей код міняє номер телефону на новий, якщо ми вводимо існуюче ім'я
@input_error
def add_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        contacts[name] = phone
        return "Contact added."
    else:
        return ('User does already exists')

def show_all( contacts):
    return contacts

@input_error
def show_phone(args, contacts):
    return contacts[args[0]]

@input_error
def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    # якщо ввели тільки phone без name, викликаємо keyerror (give me name)
    else: contacts[name]


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "all":
            print(show_all( contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()# Write your code here :-)
