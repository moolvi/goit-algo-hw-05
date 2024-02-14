import sys
import collections

from pathlib import Path
from datetime import datetime


def parse_log_line(line: str) -> dict:
    levels = ('INFO', 'ERROR', 'DEBUG', 'WARNING')
    keys = ('data', 'time', 'level', 'messege')
    
    try:
        values = line.split(' ', len(keys)-1)

        if len(values) != 4:
            raise IndexError
        if not datetime.strptime(values[0], '%Y-%m-%d'):
            raise ValueError
        if not datetime.strptime(values[1], '%H:%M:%S'):
            raise ValueError
        if values[2] not in levels:
            raise ValueError
        if len(values[3]) < 1:
            raise ValueError
        
        return {keys[a]: values[a] for a in range(4)}
    
    except ValueError:
        return f'Unknows values in the line: {line}'
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
        return rows
    except ValueError:
        return rows
    except IndexError:
        return rows
    except:
        return rows
    finally:
        return rows


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'] == level, logs))


def count_logs_by_level(logs: list) -> dict:
    return dict(collections.Counter(list(log['level'] for log in logs)))


def display_log_counts(counts: dict):

    size_key = len(max(str(item) for item in (*counts.keys(), 'Рівень логування ')))
    size_value = max(len(str(item)) for item in {*counts.values(), " Кількість"})

    print(f'{'Рівень логування ':<{size_key}}|{' Кількість':<{size_value}}')
    print(f'{'-' * size_key}|{'-' * size_value}')

    for key, value in counts.items(): 
        print(f'{key:<{size_key}}| {value:<{size_value}}')


def main():
    user_input = ''
    if len(sys.argv) > 1:
        user_input = sys.argv[1]
    path = Path(user_input)
    if path.exists():
        if path.is_file():
            display_log_counts(count_logs_by_level(load_logs(path)))
        else:
            print(f'{user_input} isn\'t file')
    else:
        print(f'{path.absolute()} isn\'t exists')


if __name__ == '__main__':
    main()