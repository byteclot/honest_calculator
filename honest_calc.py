import math

result = 0
num_x = 0
num_y = 0
calc = ""
x = 0
y = 0
oper = ""
memory = 0


def read_calc():
    global calc, memory
    # print(f'Memory: {memory}')
    calc = input("Enter an equation")


def split_calc():
    global x, y, oper
    x, oper, y = calc.split()


def check_memory():
    global memory, x, y
    if x == "M":
        # num_x = memory
        x = str(memory)
    if y == "M":
        # num_y = memory
        y = str(memory)


def check_numbers():
    global num_x, num_y, x, y
    try:
        num_x = float(x)
        num_y = float(y)
        return True
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
        return False


def check_oper():
    global oper
    if oper not in ["+", "-", "*", "/"]:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        return False
    else:
        return True


def perform_operation():
    global num_x, num_y, oper, result
    if oper == "+":
        result = num_x + num_y
    elif oper == "-":
        result = num_x - num_y
    elif oper == "*":
        result = num_x * num_y
    elif oper == "/" and num_y != 0:
        result = num_x / num_y
    else:
        print("Yeah... division by zero. Smart move...")
        return False
    return True


def print_result():
    global result
    print(result)


def prompt(msg):
    while True:
        answer = input(msg)
        if answer == "y":
            return True
        elif answer == "n":
            return False


def ask_to_confirm():
    global result
    msg_10 = "Are you sure? It is only one digit! (y / n)"
    msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
    msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

    # print(is_one_digit(result))
    if is_one_digit(result):
        if prompt(msg_10):
            if prompt(msg_11):
                if prompt(msg_12):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    return True


def ask_to_store():
    global memory
    while True:
        answer = input("Do you want to store the result? (y / n):")
        if answer == "y":
            if ask_to_confirm():
                # print("Storing in memory")
                memory = result
            break
        elif answer == "n":
            break


def ask_to_continue():
    global keep_running
    while True:
        answer = input("Do you want to continue calculations? (y / n):")
        if answer == "y":
            # print("Yes answered")
            break
        elif answer == "n":
            keep_running = False
            break


def is_one_digit(v):
    if v.is_integer() and -10 < v < 10:
        # print("Integer")
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"

    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg = msg + msg_7
    if (v1 == 0 or v2 == 0) and v3 in ["*", "+", "-"]:
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)


keep_running = True
while keep_running:
    read_calc()
    split_calc()
    check_memory()
    if check_numbers():
        if check_oper():
            check(num_x, num_y, oper)
            if perform_operation():
                print_result()
                ask_to_store()
                ask_to_continue()
