import os, glob, re

html_files = glob.glob('*.html')

pattern1 = re.compile(r'Thiruvalluvar street, gandhi nagar\s*<br>\s*saligramam, vadapalani - 600093 Chennai', re.IGNORECASE)
pattern2 = re.compile(r'Thiruvalluvar street, Gandhi nagar\s*<br>\s*Saligramam, Vadapalani\s*<br>\s*Chennai - 600093', re.IGNORECASE)

new_address = "Dasaratha Puram, Vadapalani, Chennai, Greater Chennai, Tamil Nadu 600093"

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    new_content = pattern1.sub(new_address, content)
    new_content = pattern2.sub(new_address, new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated address in {filepath}")

print("Address update complete.")
