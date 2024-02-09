import os
import re
import sys

import html2text
from bs4 import BeautifulSoup, NavigableString


def parse_method_declaration(text):
    # Extract method name and parameters, handling potential line breaks and multiple parameters
    method_match = re.search(r'\[method:this (\w+)\]', text)
    params_matches = re.findall(r'\[param:(\w+) (\w+)\]', text.replace('\n', ' '))

    if method_match:
        method_name = method_match.group(1)
        params_list = ', '.join(
            f"{param_name}: {param_type}" + ("?" if "Boolean" in param_type else "") for param_type, param_name in
            params_matches)
        return f"<br/>\nfunction {method_name}( {params_list} ): {method_name};\n<br/>"
    return None


def convert_custom_links_to_ts(soup):
    # Iterate through all text nodes to find patterns
    for content in soup.find_all(string=True):
        if isinstance(content, NavigableString):
            updated_content = content

            # Handle property pattern
            prop_matches = re.finditer(r'\[property:(\w+) (\w+)\]', content)
            for match in prop_matches:
                prop_type, prop_name = match.groups()
                ts_declaration = f"<br/>\n{prop_type} {prop_name};\n<br/>"
                updated_content = updated_content.replace(match.group(0), ts_declaration)

            # Handle method pattern, accounting for multiple parameters and line breaks
            if '[method:this' in content:
                method_declaration = parse_method_declaration(content)
                if method_declaration:
                    updated_content = updated_content.replace(content, method_declaration)

            # Only replace content if changes were made
            if updated_content != content:
                content.replace_with(updated_content)


def replace_code_tags(soup):
    for code in soup.find_all('code'):
        code_text = code.get_text(separator="\n")
        code_lines = code_text.split('\n')
        code_with_br = '<br/>'.join(code_lines)
        markdown_code = "<br/>\n```ts\n" + code_with_br + "\n```\n<br/>"
        new_code = BeautifulSoup(markdown_code, 'html.parser')
        code.replace_with(new_code)


def convert_html_to_markdown(html_content, relative_path_to_root):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Convert custom links to TypeScript format
    convert_custom_links_to_ts(soup)

    replace_code_tags(soup)

    h = html2text.HTML2Text()
    h.ignore_links = False
    return h.handle(str(soup))


# Sample usage within the process_file function or similar


def process_file(html_file, source_root, dest_root):
    relative_path_to_root = os.path.relpath(html_file, start=source_root)
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    markdown = convert_html_to_markdown(html_content, relative_path_to_root)

    markdown_file_path = os.path.join(dest_root, os.path.splitext(relative_path_to_root)[0] + '.md')
    os.makedirs(os.path.dirname(markdown_file_path), exist_ok=True)

    with open(markdown_file_path, 'w', encoding='utf-8') as md_file:
        md_file.write(markdown)

    print(f"Converted {html_file} to {markdown_file_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: script.py <input_path> [destination_directory]")
        sys.exit(1)

    input_path = sys.argv[1]
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else f"{input_path.rstrip(os.path.sep)}-md"

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    if os.path.isdir(input_path):
        for root, dirs, files in os.walk(input_path):
            for file in files:
                if file.endswith('.html'):
                    html_file_path = os.path.join(root, file)
                    process_file(html_file_path, input_path, dest_dir)
    elif os.path.isfile(input_path) and input_path.endswith('.html'):
        # Adjust source_root to handle single file correctly
        source_root = os.path.dirname(input_path) or '.'
        process_file(input_path, source_root, dest_dir)
    else:
        print(f"The input path {input_path} is not a valid HTML file or directory.")
        sys.exit(1)
