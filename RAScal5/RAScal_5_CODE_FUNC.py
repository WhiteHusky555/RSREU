# ФУНКЦИИ ДЛЯ ПЕРЕВОДА ИЗ КОДА


def hex_to_bin(number_hex):
    number_conv_bin = bin(int(number_hex, 16))[2:]
    if len(number_conv_bin) % 4 != 0:
        number_conv_bin = '0' * (4 - len(number_conv_bin) % 4) + number_conv_bin
    return number_conv_bin


def straight_to_number(code_straight_bin):  # перевод из прямого в десятичное
    if code_straight_bin[0] == '0':  # если код начинается с нуля, то число положительное
        number_dec = int(code_straight_bin[1:], 2)
    else:
        number_dec = -1 * int(code_straight_bin[1:], 2)
    return number_dec


def reverse_to_number(code_reverse_bin):  # перевод из обратного кода в число
    if code_reverse_bin[0] == '0':  # если обратный код начинается с нуля, то он равен прямому
        number_dec = straight_to_number(code_reverse_bin)
    else:
        # Инвертирование
        code_reverse_bin = code_reverse_bin[1:]
        code_reverse_bin = code_reverse_bin.replace('1', '2', code_reverse_bin.count('1'))
        code_reverse_bin = code_reverse_bin.replace('0', '1', code_reverse_bin.count('0'))
        code_reverse_bin = code_reverse_bin.replace('2', '0', code_reverse_bin.count('2'))
        code_reverse_bin = '0' + code_reverse_bin
        number_dec = -1 * straight_to_number(code_reverse_bin)
    return number_dec


def additional_to_number(code_additional_bin):  # перевод из дополнительного кода в число
    if code_additional_bin[0] == '0':  # если дополнительный код начинается с нуля, то он равен прямому
        number_dec = straight_to_number(code_additional_bin)
    else:
        number_dec = reverse_to_number(bin(int(code_additional_bin, 2) - 1)[2:])  # переводим в обратный вычитая 1
    return number_dec
