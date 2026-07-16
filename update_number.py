import os
import glob

old_number = "9361737903"
new_number = "9361737903"
directory = r"e:\Business\Chennai FPV Drones\Chennai FPV Drones\chennai-fpv-drones-web"

count = 0
for filepath in glob.glob(os.path.join(directory, '**', '*.*'), recursive=True):
    if filepath.endswith('.html') or filepath.endswith('.py'):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            if old_number in content:
                content = content.replace(old_number, new_number)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
                print(f"Updated: {filepath}")
        except Exception as e:
            print(f"Error reading {filepath}: {e}")

print(f"Total files updated: {count}")
