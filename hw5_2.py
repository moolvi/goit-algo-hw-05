def generator_numbers(text: str):
    for part in text.split(' '):
        try:
            yield float(part.replace(',', '.'))
            # This processing for regional settings is not complete, but
            # it's for memory.
        except ValueError:
            pass
        except Exception:
            pass


def sum_profit(text: str, func: callable):
    return sum(func(text))