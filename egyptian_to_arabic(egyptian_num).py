def egyptian_to_arabic(egyptian_num):
    egyptian_dict = {'|': 1, '||': 2, '|||': 3, '||||': 4, '-': 5, '-|': 6, '-||': 7, '-|||': 8, '-||||': 9}
    arabic_num = 0

    while egyptian_num:
        for symbol in reversed(sorted(egyptian_dict.keys())):
            if egyptian_num.startswith(symbol):
                arabic_num += egyptian_dict[symbol]
                egyptian_num = egyptian_num[len(symbol):]
                break

    return arabic_num

def arabic_to_egyptian(arabic_num):
    egyptian_dict = {1: '|', 2: '||', 3: '|||', 4: '||||', 5: '-', 6: '-|', 7: '-||', 8: '-|||', 9: '-||||'}
    egyptian_num = ''

    for value in sorted(egyptian_dict.keys(), reverse=True):
        while arabic_num >= value:
            egyptian_num += egyptian_dict[value]
            arabic_num -= value

    return egyptian_num

# Example usage:
egyptian_num = '||||'
arabic_equivalent = egyptian_to_arabic(egyptian_num)
print(f'Egyptian: {egyptian_num} => Arabic: {arabic_equivalent}')
