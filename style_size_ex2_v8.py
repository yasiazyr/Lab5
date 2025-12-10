import re

FILENAME = 'task2.html'

with open(FILENAME, encoding='utf-8') as f:
    html = f.read()

pattern_font_style = re.compile(r'font-style\s*:\s*([^;"]+)', re.IGNORECASE)
font_styles = pattern_font_style.findall(html)

pattern_font_size_css = re.compile(r'font-size\s*:\s*([^;"]+)', re.IGNORECASE)
font_sizes_css = pattern_font_size_css.findall(html)

pattern_font_size_attr = re.compile(r'<font[^>]*\bsize\s*=\s*["\']?([^"\'\s>]+)', re.IGNORECASE)
font_sizes_attr = pattern_font_size_attr.findall(html)

print('Стиль шрифтов:')
for s in set(map(str.strip, font_styles)):
    print(s)

print('\nРазмеры шрифтов:')
all_sizes = set(map(str.strip, font_sizes_css + font_sizes_attr))
for sz in all_sizes:
    print(sz)