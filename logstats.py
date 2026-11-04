from collections import Counter
levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR']
def parse_event(line):
    parts= line.strip().split(maxsplit = 2)
    if len(parts) !=3:
        raise ValueError('Неверный формат строки')
    time, level, message  = parts
    if level not in levels:
        raise ValueError('Неизвестный уровень')
    return {'time': time, 'level': level, 'message': message}

 

def count_levels(lines):
    counts =Counter()
    for line in lines:
        if not line.strip():
            continue 
        try:
            counts[parse_event(line)['level']] += 1
        except ValueError:
            counts['BROKEN'] += 1 
    return dict(counts)

def top_errors(lines, n):
    messages = Counter()
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue  
        if event['level'] == 'ERROR':
            messages[event['message']] += 1
    pairs = sorted(messages.items())
    pairs.sort(key = lambda pair: pair[1], reverse = True)
    result = []
    for message, count in pairs[:n]:
        result.append([message, count])
    return result



def format_report(counts, errors):
    lines = ["Отчёт по журналу", '']
    for level in sorted(counts):
        lines.append(f'{level}: {counts[level]}')
    lines.append('')
    lines.append('Частые ошибки:')
    for message, count in errors:
        lines.append(f' {message} - {count}')
    return '\n'.join(lines) + '\n'