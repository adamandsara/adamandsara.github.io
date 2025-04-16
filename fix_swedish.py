import os

html_numeric_escapes = {
    'ä': '&#228;',
    'Ä': '&#196;',
    'ö': '&#246;',
    'Ö': '&#214;',
    'å': '&#229;',
    'Å': '&#197;',
}


def replace_swedish_chars(content):
    for char, escape in html_numeric_escapes.items():
        content = content.replace(char, escape)
    return content


def process_html_files(directory='.'):
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            new_content = replace_swedish_chars(content)

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

            print(f"Processed: {filename}")


if __name__ == '__main__':
    process_html_files()
