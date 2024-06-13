def sumerian_to_arabic(sumerian_num):
    sumerian_dict = {'𒐕': 1, '𒐒': 10, '𒐏': 60, '𒐁': 600, '𒐈': 3600}
    arabic_num = 0
    current_value = 0

    for c in reversed(sumerian_num):
        value = sumerian_dict.get(c, 0)
        if value < current_value:
            arabic_num -= value
        else:
            arabic_num += value
            current_value = value

    return arabic_num

def arabic_to_sumerian(arabic_num):
    sumerian_dict = {1: '𒐕', 10: '𒐒', 60: '𒐏', 600: '𒐁', 3600: '𒐈'}
    sumerian_num = ''
    
    for value in sorted(sumerian_dict.keys(), reverse=True):
        while arabic_num >= value:
            sumerian_num += sumerian_dict[value]
            arabic_num -= value
    
    return sumerian_num

# Example usage:
sumerian_num = '𒐕𒐒𒐏'
arabic_equivalent = sumerian_to_arabic(sumerian_num)
print(f'Sumerian: {sumerian_num} => Arabic: {arabic_equivalent}')
