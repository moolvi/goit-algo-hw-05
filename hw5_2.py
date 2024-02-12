def generator_numbers(text: str):
    number=''
    for symbol in text:
        if symbol == ' ':
            try:
                # This processing for regional settings is not complete, but...
                yield float(number.replace(',', '.'))
            except ValueError:
                pass
            except:
                pass
            finally:
                number = ''
        else:
            number += symbol

def sum_profit(text: str, func: callable):
    return sum(func(text))