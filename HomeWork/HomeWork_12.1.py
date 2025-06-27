import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()


    cleaned = ''  # удаляю HTML-теги
    inside_tag = False
    for char in html:
        if char == '<':
            inside_tag = True
        elif char == '>':
            inside_tag = False
        elif not inside_tag:
            cleaned += char

    lines = cleaned.split('\n')

    cleaned_lines = []
    previous_was_text = False

    for line in lines:
        stripped = line.strip()
        collapsed = re.sub(r'\s{2,}', ' ', stripped)

        if collapsed:
            if not previous_was_text and cleaned_lines:
                cleaned_lines.append('')  # разделитель-блок
            cleaned_lines.append(collapsed)
            previous_was_text = True
        else:
            previous_was_text = False

    with codecs.open(result_file, 'w', 'utf-8') as output:
        output.write('\n'.join(cleaned_lines))