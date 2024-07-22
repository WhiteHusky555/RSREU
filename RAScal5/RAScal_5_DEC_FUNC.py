# ФУНКЦИИ ДЛЯ ПЕРЕВОДА В КОД


def complete_to_cell(str_to_conv, comp_el):  # дополнение нулями до байта, слова, двойного и учетверенного слова
    conv_str = ''
    if len(str_to_conv) <= 7:  # меньше или равно количеству разрядов байта
        conv_str += comp_el * (7 - len(str_to_conv)) + str_to_conv  # дополнение нулями до нужного числа разрядов
    elif len(str_to_conv) <= 15:  # меньше или равно количеству разрядов слова
        conv_str += comp_el * (15 - len(str_to_conv)) + str_to_conv
    elif len(str_to_conv) <= 31:  # меньше или равно количеству разрядов двойного слова
        conv_str += comp_el * (31 - len(str_to_conv)) + str_to_conv
    elif len(str_to_conv) <= 63:  # меньше или равно количеству разрядов учетверенного слова
        conv_str += comp_el * (63 - len(str_to_conv)) + str_to_conv
    return conv_str


def bin_to_hex(number_bin):  # перевод двоичного числа в шестнадцатеричное
    number_hex = ''  # код в шестнадцатеричной системе
    for k in range(0, len(number_bin) - 3, 4):  # перевод из двоичной в шестнадцатеричную включая знаковый бит
        number_hex += hex(int(number_bin[k:k + 4], 2))[2:]
    return number_hex


def number_to_straight(number_dec):  # перевод десятичного числа в прямой код
    if number_dec < 0:
        number_straight_bin = '1'  # строка со значением прямого кода
        str_to_conv = bin(number_dec)[3:]  # число number_dec в двоичной системе
    else:
        number_straight_bin = '0'
        str_to_conv = bin(number_dec)[2:]
    number_straight_bin += complete_to_cell(str_to_conv, '0')
    return number_straight_bin


def number_to_reverse(number_dec):  # перевод десятичного числа в обратный код
    number_rev_bin = number_to_straight(number_dec)  # обратный код соответствует прямому если число больше 0
    if number_dec < 0:
        # ИНВЕРТИРОВАНИЕ
        number_rev_bin = number_rev_bin.replace('1', '2', number_rev_bin.count('1'))
        number_rev_bin = number_rev_bin.replace('0', '1', number_rev_bin.count('0'))
        number_rev_bin = number_rev_bin.replace('2', '0', number_rev_bin.count('2'))
        number_rev_bin = '1' + number_rev_bin[1:]  # обратный код начинается с единицы
    return number_rev_bin


def number_to_additional(number_dec):  # перевод десятичного числа в дополнительный код
    number_reverse_bin = number_to_reverse(number_dec)  # обратный код числа
    number_add_bin = number_reverse_bin  # дополнительный код соответствует прямому если число больше 0
    if number_dec < 0:
        number_add_bin = bin(int(number_reverse_bin, 2) + 1)[2:]  # добавление единицы к младшему разряду
    return number_add_bin
