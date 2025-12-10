import re

FILENAME = 'task1-ru.txt'

with open(FILENAME, encoding='utf-8') as f:
    text = f.read()

pattern_fig = re.compile(r'\b(?:рис|Fig)\.\s*\d+', re.IGNORECASE)
fig_matches = pattern_fig.findall(text)

print('Конструкции "рис. #" или "Fig. #":')
for i in fig_matches:
    print(i)

pattern_4_letters = re.compile(r'\b[А-Яа-яA-Za-z]{4}\b')
words_4_letters = pattern_4_letters.findall(text)

print('\nСлова из 4 букв:')
for i in words_4_letters:
    print(i)