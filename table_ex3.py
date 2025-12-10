import re
import csv

FILENAME_IN = 'task3.txt'
FILENAME_OUT = 'task3_result.csv'

with open(FILENAME_IN, encoding='utf-8') as f:
    text = f.read()

pattern_id = re.compile(r'(?:^|\s)(\d+)(?=\s|$)')
pattern_surname = re.compile(r'\b[А-ЯЁ][а-яё]+|\b[A-Z][a-z]+\b')
pattern_email = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}')
pattern_date = re.compile(r'\b\d{4}\-\d{2}\-\d{2}\b')
pattern_site = re.compile(r'\b(?:https?://)?(?:www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(?:/\S*)?\b')

ids = pattern_id.findall(text)
surnames = pattern_surname.findall(text)
emails = pattern_email.findall(text)
dates = pattern_date.findall(text)
sites = pattern_site.findall(text)

n = max(len(ids), len(surnames), len(emails), len(dates), len(sites))

def safe_get(lst, i):
    return lst[i] if i < len(lst) else ''

rows = []
for i in range(n):
    rows.append([
        safe_get(ids, i),
        safe_get(surnames, i),
        safe_get(emails, i),
        safe_get(dates, i),
        safe_get(sites, i)
    ])

with open(FILENAME_OUT, 'w', encoding='utf-8-sig', newline='') as f_out:
    writer = csv.writer(f_out, delimiter=';')
    writer.writerow(['ID', 'Фамилия', 'Email', 'Дата регистрации', 'Сайт'])
    writer.writerows(rows)

print(f'Готово! Файл сохранён')