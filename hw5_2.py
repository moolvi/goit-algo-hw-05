def generator_numbers(text: str):
    number=''
    real_number = float(0)
    for symbol in text:
        if symbol == ' ':
            try:
                # This processing for regional settings is not complete, but...
                number = number.replace(',', '.')
                real_number = float(number)
                yield real_number
            except:
                pass
            finally:
                number = ''
                real_number = float(0)
        else:
            number += symbol

def sum_profit(text: str, func: callable):
    sum_real_number = 0.0
    for real in func(text):
        sum_real_number += real
    return sum_real_number