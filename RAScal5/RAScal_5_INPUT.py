def hex_to_bin(number_hex):
    number_conv_bin = bin(int(number_hex, 16))[2:]
    if len(number_conv_bin) % 4 != 0:
        number_conv_bin = '0' * (4 - len(number_conv_bin) % 4) + number_conv_bin
    return number_conv_bin


def is_a_number(numb_str):  # проверка на отсутствие знаков не числа
    for symbol in numb_str:
        if symbol not in '1234567890.,':
            return False  # возвращается если есть знаки не числа

    return True  # возвращается если есть знаки не числа


def input_value(convert_type, code_type, valinput):
    correct_input = False
    error_type = 'None'
    if convert_type == 0:
        error_type = '01'
    elif (convert_type == 2 or convert_type== 3) and code_type == 0:
        error_type = '02'
    elif len(valinput) < 1:
        error_type = '03'
    else:
        if convert_type == 1:
            number_dec_str = valinput
            correct_input = True
            # ПРОВЕРКА ВВЕДЕННОЙ СТРОКИ НА ПРАВИЛЬНОСТЬ
            if (number_dec_str[0] in '+-' and not is_a_number(number_dec_str[1:])) or \
                    (number_dec_str[0] not in '+-' and not is_a_number(
                        number_dec_str)):  # условие наличия недопустимых знаков
                error_type = '10'
                correct_input = False
            elif (number_dec_str[0] in '+-' and number_dec_str[1] == '0') or \
                    (len(number_dec_str) > 1 and number_dec_str[0] == '0'):  # условие начала числа с нуля
                error_type = '11'
                correct_input = False
            elif (',' in number_dec_str) or ('.' in number_dec_str):  # условие наличия точки в числе
                error_type = '12'
                correct_input = False
            elif (int(number_dec_str) < -(2 ** 63 - 1)) or (int(number_dec_str) > (2 ** 63 - 1)):  # условие выхода
                # за диапазон
                error_type = '13'
                correct_input = False
        elif convert_type == 2:
            bin_code_str = valinput
            correct_input = True  # флаг правильности ввода цифр кода
            for k in bin_code_str:  # проверка на отсутствие недопустимых символов
                if k not in '01':
                    correct_input = False
            if not correct_input:
                error_type = '20'
                correct_input = False
            elif len(bin_code_str) > 64:
                error_type = '21'
                correct_input = False
            elif len(bin_code_str) < 2:
                error_type = '22'
                correct_input = False
            elif code_type == 2 and ('0' not in bin_code_str):
                error_type = '23'
                correct_input = False
            elif code_type == 3 and ('1' not in bin_code_str[1:] and bin_code_str[0] == '1'):
                error_type = '24'
                correct_input = False
        else:
            hex_code_str = valinput
            correct_input = True  # флаг правильности ввода цифр кода
            for k in hex_code_str:  # проверка на отсутствие недопустимых символов
                if k not in '0123456789abcdef':
                    correct_input = False
            if not correct_input:
                error_type = '30'
                correct_input = False
            elif len(hex_code_str) > 16:
                error_type = '31'
                correct_input = False
            elif code_type == 2 and (not ('0' in hex_to_bin(hex_code_str))):
                error_type = '32'
                correct_input = False
            elif code_type == 3 and ('1' not in hex_to_bin(hex_code_str)[1:] and
                                           hex_to_bin(hex_code_str)[0] == '1'):
                error_type = '33'
                correct_input = False
    if correct_input:
        res = (correct_input, error_type)
    else:
        res = (correct_input, error_type)
    return res
