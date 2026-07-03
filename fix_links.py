import os, glob, re

# Map broken templates to our actual pages
link_mapping = {
    'about-1.html': 'about.html',
    'contact-1.html': 'contact.html',
    'contact-2.html': 'contact.html',
    'contact-3.html': 'contact.html',
    'services.html': 'index.html',
    'portfolio-1.html': 'index.html',
    'team.html': 'about.html',
    'archive-1.html': 'index.html',
    'pricing.html': 'contact.html',
}

valid_files = set(glob.glob('*.html'))

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    # Find all href="something.html"
    def replacer(match):
        original_link = match.group(1)
        # If it's not valid, and it's in our mapping, replace it
        if original_link not in valid_files:
            if original_link in link_mapping:
                return 'href="' + link_mapping[original_link] + '"'
            else:
                return 'href="index.html"' # Fallback
        return match.group(0) # unchanged

    new_content = re.sub(r'href="([^"]+\.html)"', replacer, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated links in {filepath}")

print("Done fixing links.")
