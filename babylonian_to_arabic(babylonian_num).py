def babylonian_to_arabic(babylonian_num):
    babylonian_dict = {'|': 1, '||': 10, '|||': 100}
    arabic_num = 0

    while babylonian_num:
        for symbol in reversed(sorted(babylonian_dict.keys())):
            if babylonian_num.startswith(symbol):
                arabic_num += babylonian_dict[symbol]
                babylonian_num = babylonian_num[len(symbol):]
                break

    return arabic_num

def arabic_to_babylonian(arabic_num):
    babylonian_dict = {1: '|', 10: '||', 100: '|||'}
    babylonian_num = ''

    for value in sorted(babylonian_dict.keys(), reverse=True):
        while arabic_num >= value:
            babylonian_num += babylonian_dict[value]
            arabic_num -= value

    return babylonian_num

# Example usage:
babylonian_num = '|||||'
arabic_equivalent = babylonian_to_arabic(babylonian_num)
print(f'Babylonian: {babylonian_num} => Arabic: {arabic_equivalent}')
