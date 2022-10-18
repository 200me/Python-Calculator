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
    if len(input_list) < 3:
        return True, "Please enter valid input"
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


def calculate_mul_div(input_list):
    # loop * / 처리 루프
    # list [ 1 + 2 - [3 * 4] / 5  ]
    # list [ 1 + 2 - [12 / 5] ]
    # list [ 1 + 2 - 2.4 ]
    mul_div = ['*', '/']
    while any(element in mul_div for element in input_list):
        for i in range(len(input_list)):
            if input_list[i] == '*':
                input_list[i - 1] = multiply(input_list[i - 1], input_list[i + 1])
                del input_list[i:i + 2]
                break
            elif input_list[i] == '/':
                input_list[i - 1] = divide(input_list[i - 1], input_list[i + 1])
                del input_list[i:i + 2]
                break

    return input_list


def controller(input):
    input_list = list(map(str, input.split()))

    # 처음이 숫자이면서 숫자 기호 반복, 마지막이 숫자
    # 다 숫자고, 숫자 기호 잘 되어있고, 모든 숫자 부분이 다 숫자임, 기호도 다 기호
    error, error_message = input_checker(input_list)

    if error:
        return error_message

    # + - 처리 루프
    # list [ [1 + 2] - 2.4 ]
    # list [ [3 - 2.4] ]
    # list [ 0.6 ]

    return calculate_mul_div(input_list)
