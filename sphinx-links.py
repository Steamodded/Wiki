import os
import sys
import re
from urllib.parse import unquote, quote
directory = "."
lookup = {}

for root, _, files in os.walk(directory):
	for file in files:
		if file.endswith(".md"):
			basename = os.path.splitext(os.path.basename(file))[0].replace(" ", "-")
			if basename in lookup:
				print("Double named md:", basename)
				sys.exit(1)
			rel_path = os.path.relpath(os.path.join(root, file), directory)
			lookup[basename] = rel_path

pattern = re.compile(r'https://github\.com/Steamodded/smods/wiki/([^\])>}#"\s]*[^\])>}#"\s\.])')

for key, value in lookup.items():
    print(f"{key}: {value}")
    file_path = os.path.join(directory, value)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    matches = pattern.findall(content)
    for match in matches:
        decoded = unquote(match)
        if decoded not in lookup:
            sys.exit(f"Error: Linked page '{decoded}' not found in directory.")
        new_path = quote(os.path.splitext(lookup[decoded])[0], safe='/')
        replacement = f'https://wikitest.smods.dev/{new_path}'
        original_url = f'https://github.com/Steamodded/smods/wiki/{match}'
        content = content.replace(original_url, replacement, 1)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
