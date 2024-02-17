import sys
import collections

from pathlib import Path
from datetime import datetime

LEVELS = ('INFO', 'ERROR', 'DEBUG', 'WARNING')
KEYS = ('data', 'time', 'level', 'messege')

display_with_level = None
logs = None


def parse_log_line(line: str) -> dict:
    try:
        values = line.split(' ', len(KEYS) - 1)

        if len(values) != 4:
            raise IndexError
        if not datetime.strptime(values[0], '%Y-%m-%d'):
            raise ValueError
        if not datetime.strptime(values[1], '%H:%M:%S'):
            raise ValueError
        if values[2] not in LEVELS:
            raise ValueError
        if len(values[3]) < 1:
            raise ValueError
        if not display_with_level in LEVELS:
            raise ValueError
        return {KEYS[a]: values[a] for a in range(4)}
    
    except ValueError:
        return f'Unknown values in the line: {line}'
    except IndexError:
        return f'Unknown structure in the line: {line}'
    except Exception:
        return f'Unknow Error: {line}'
    finally:
        pass


def load_logs(file_path: str) -> list:
    rows = []
    try:
        with open(file_path, encoding='utf-8') as file:
            for row in file.readlines():
                rows.append(parse_log_line(row.strip()))
    except FileNotFoundError:
        return f'File not found: {file_path}'
    except ValueError:
        return f'Unknow value in file: {row}'
    except IndexError:
        return f'The number of lines has changed: {row}'
    except Exception:
        return f'Unknow Error: {row}'
    finally:
        return rows


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    return dict(collections.Counter(list(log['level'] for log in logs)))


def display_log_counts(counts: dict):
    size_key = len(max(*counts.keys(), 'Рівень логування')) + 1
    size_value = len(max(str(item) for item in {*counts.values(), "Кількість"})) + 1

    print(f'{'Рівень логування':<{size_key}}|{'Кількість':>{size_value}}')
    print(f'{'-' * size_key}|{'-' * size_value}')

    for key, value in counts.items(): 
        print(f'{key:<{size_key}}|{value:>{2}}')
    
    if display_with_level in LEVELS:
        user_level = filter_logs_by_level(logs, display_with_level)
        print(f"\nДеталі логів для рівня '{display_with_level}':")
        
        for item in user_level:
            print(f'{item[KEYS[0]]} {item[KEYS[1]]} - {item[KEYS[3]]}')


def main():
    global display_with_level
    global logs

    user_input = ''
    if len(sys.argv) > 2:
        user_input = sys.argv[1]
        display_with_level = sys.argv[2]
    
    path = Path(user_input)
    if path.exists():
        if path.is_file():
            logs = load_logs(path)
            display_log_counts(count_logs_by_level(logs))
        else:
            print(f'{path} isn\'t file')
    else:
        print(f'{path.absolute()} isn\'t exists')


if __name__ == '__main__':
    main()