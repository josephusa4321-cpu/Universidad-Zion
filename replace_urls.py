import os

def replace_in_file(file_path, old_str, new_str):
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        return
    # Read file content
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Replace content
    new_content = content.replace(old_str, new_str)
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Successfully replaced in {file_path}")

# Paths to the combined assets
css_path = 'wp-content/uploads/siteground-optimizer-assets/siteground-optimizer-combined-css-a6ea0cc2fcb4e82110e248c24fbc0ec9.css'
js_path = 'wp-content/uploads/siteground-optimizer-assets/siteground-optimizer-combined-js-57238bcf86038096e37a053bbd42ab3f.js'

print("Starting URL replacement...")
replace_in_file(css_path, 'https://dbtm.tds.tu.ac.th', '../../..')
replace_in_file(js_path, 'https://dbtm.tds.tu.ac.th', '.')
replace_in_file(js_path, 'https:\\/\\/dbtm.tds.tu.ac.th', '.')
print("Done!")
