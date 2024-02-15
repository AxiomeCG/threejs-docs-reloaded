import os
import re
import sys

import html2text
from bs4 import BeautifulSoup, NavigableString

page_dict = {}


# Step 1: Build the page dictionary
def build_page_dictionary(input_folder):
    dict = {}
    for root, dirs, files in os.walk(input_folder):
        for filename in files:
            if filename.endswith('.html'):  # Adjust as needed
                page_name = os.path.splitext(filename)[0]
                # Construct the file path relative to the input folder
                filepath = os.path.join(root, filename)
                dict[page_name] = filepath
    return dict


def transform_text_anchor(text):
    # First replacement: [page:.method]
    def replace(match):
        page_name = match.group(1)
        return f"[.{page_name}](#{page_name})"

    text = re.sub(r'\[page:.(\w+) ([\w\.\s]+)\]', replace, text)
    return text


# Step 2: Transform text
def transform_text(text, page_dict):
    # First replacement: [page:name] to [page:name title] (if needed)
    text = re.sub(r'\[page:([\w\.]+)\]', r'[page:\1 \1]', text)

    # Third replacement: [page:name title] to HTML anchor tags
    def replace_with_link(match):
        page_name = match.group(1)
        title = match.group(2)
        href = page_dict.get(page_name, "#")

        return f"[{title}]({href})"

    text = re.sub(r'\[page:([\w\.]+) ([\w\.\s]+)\]', replace_with_link, text)
    return text


def parse_method_declaration(text):
    # Extract method name and parameters, handling potential line breaks and multiple parameters
    method_match = re.search(r'\[method:(\w+) (\w+)\s*\]', text)
    params_matches = re.findall(r'\[param:(\w+) (\w+)\s*\]', text.replace('\n', ' '))

    if method_match:
        method_return_type = method_match.group(1)
        method_name = method_match.group(2)
        params_list = ', '.join(
            f"{param_name}: {param_type}" for param_type, param_name in
            params_matches)
        return f"\nfunction {method_name}( {params_list} ): {method_return_type};\n"
    return None


def convert_custom_links_to_markdown(text, relative_path_to_root):
    # Normalize the relative path and ensure it uses forward slashes, remove '.html' extension
    relative_path_to_root = relative_path_to_root.replace('\\', '/').replace('.html', '')

    # Define patterns to match both types of custom link formats
    # Pattern 1: Matches [link:URL src/[path].js]
    pattern1 = re.compile(
        r'\[link:(https://github\.com/mrdoob/three\.js/blob/master/src/\[path\]\.js)\s+src/\[path\]\.js\]')
    # Pattern 2: Matches [link:URL LinkText]
    pattern2 = re.compile(r'\[link:(https?://[^\s]+)\s+([^\]]+)\]')

    # Function to replace pattern 1 matches with <a> tags
    def replacement1(match):
        url_part = match.group(1).replace('[path]', relative_path_to_root)
        # Clean up the URL to remove any newlines or excessive whitespace
        clean_url = re.sub(r'\s+', '', url_part)
        return f'<a href="{clean_url}">src/{relative_path_to_root}.js</a>'

    # Function to replace pattern 2 matches with <a> tags
    def replacement2(match):
        url, link_text = match.groups()
        # Clean up the URL to remove any newlines or excessive whitespace
        clean_url = re.sub(r'\s+', '', url)
        return f'<a href="{clean_url}">{link_text}</a>'

    # Apply replacements for both patterns
    converted_text = pattern1.sub(replacement1, text)
    converted_text = pattern2.sub(replacement2, converted_text)

    return converted_text

def convert_custom_links_to_ts(soup, relative_path_to_root=None):

    # Iterate through all <h3> tags (or other relevant tags)
    for h3 in soup.find_all('h3'):
        content = h3.get_text(strip=True)
        match = re.search(r'\[property:(\w+) (\w+)\]', content)
        if match:
            prop_type, prop_name = match.groups()

            h3.clear()
            h3.append(prop_name)

            br_tag = soup.new_tag('br')
            h3.insert_after(br_tag)

            # Use strip() to ensure no leading/trailing whitespace
            ts_declaration = f"{prop_name}: {prop_type};".strip()

            # Create and insert <code> tag directly, minimizing whitespace
            code_tag = soup.new_tag('code', attrs={'class': 'typescript'})
            code_tag.string = ts_declaration

            br_tag.insert_after(code_tag)

    for h3 in soup.find_all('h3'):
        original_text = str(h3)
        token = re.search(r'\\(\w+).html', relative_path_to_root)

        if(token):original_text = original_text.replace('[name](', f"[method:void {token.group(1)}](")
        print(f"Found method: {original_text}")


        method_declaration = parse_method_declaration(original_text)

        if method_declaration:
            # Clear existing content and set the method name as the new content
            method_name = re.search(r'\[method:\w+ (\w+)\s*\]', original_text).group(1)
            print(f"Found method: {method_name}")
            h3.clear()
            h3.append(method_name)

            # Insert a <br/> tag after <h3>
            br_tag = soup.new_tag('br')
            h3.insert_after(br_tag)

            # Create and insert <code> tag with the TypeScript declaration
            code_tag = soup.new_tag('code', attrs={'class': 'typescript'})
            code_tag.string = method_declaration.strip()  # Remove leading/trailing newlines
            br_tag.insert_after(code_tag)

    # Iterate through all text nodes to find patterns
    for content in soup.find_all(string=True):
        if isinstance(content, NavigableString):

            updated_content = content

            updated_content = updated_content.strip().replace('\n', '').replace('\t', ' ').strip()

            # Replace by the name of the file
            if '[name]' in updated_content:
                token = re.search(r'\\(\w+).html', relative_path_to_root)
                if (token): updated_content = updated_content.replace('[name]', token.group(1))
            if '[page:.' in content:
                updated_content = transform_text_anchor(updated_content)
            if '[page:' in content:
                updated_content = transform_text(updated_content, page_dict)

            if '[link:' in content:
                updated_content = convert_custom_links_to_markdown(updated_content, relative_path_to_root)
            # Only replace content if changes were made
            if updated_content != content:
                content.replace_with(updated_content)


def replace_code_tags(soup):
    for code in soup.find_all('code'):
        code_text = code.get_text(separator="\n")
        code_lines = code_text.split('\n')
        code_with_br = '<br/>'.join(code_lines)
        markdown_code = "<br/>\n```ts\n<br/>" + code_with_br + "\n<br/>\n```\n<br/>"
        new_code = BeautifulSoup(markdown_code, 'html.parser')
        code.replace_with(new_code)


def convert_html_to_markdown(html_content, relative_path_to_root):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Convert custom links to TypeScript format
    convert_custom_links_to_ts(soup, relative_path_to_root)

    replace_code_tags(soup)

    h = html2text.HTML2Text()
    h.ignore_links = False

    # print("debug", str(soup))
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
    dest_dir = sys.argv[2] if len(sys.argv) > 2 else f"demo/docs/{input_path.rstrip(os.path.sep)}"

    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    if os.path.isdir(input_path):
        page_dict = build_page_dictionary(input_path)
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
