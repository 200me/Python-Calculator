from model.arithmetic import *


def error_message_maker(input_list, error_index_list):
    return_string = "Error found:"
    for i in range(len(input_list)):
        if i in error_index_list:
            return_string += f" [{input_list[i]}]"
        else:
            return_string += f" {input_list[i]}"
    return return_string


def input_checker(input_list):
    error_index_list = []
    for i in range(len(input_list)):
        if i % 2 == 0:
            try:
                int(input_list[i])  # 숫자여야함
            except ValueError:
                error_index_list.append(i)
        else:
            if input_list[i] not in ['+', '-', '*', '/']:
                error_index_list.append(i)

    return len(error_index_list) > 0, error_message_maker(input_list, error_index_list)


def controller(input):
    input_list = list(map(str, input.split()))

    # 처음이 숫자이면서 숫자 기호 반복, 마지막이 숫자
    # 다 숫자고, 숫자 기호 잘 되어있고, 모든 숫자 부분이 다 숫자임, 기호도 다 기호
    error, error_message = input_checker(input_list)

    if error:
        return error_message

    # try:
    #     num1 = int(num1)
    #     num2 = int(num2)
    # except ValueError:
    #     return "Enter a number"
    #
    # if sign == '+':
    #     return add(num1, num2)
    # elif sign == '-':
    #     return subtract(num1, num2)
    # elif sign == '*':
    #     return multiply(num1, num2)
    # elif sign == '/':
    #     try:
    #         return divide(num1, num2)
    #     except ZeroDivisionError:
    #         return "Zero Division Error detected"
