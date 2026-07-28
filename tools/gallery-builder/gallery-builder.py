import yaml
import sys
import os
from pathlib import Path
# html entry template text
template = Path("template.html").read_text()
# html code for the rest of the page
base_html_page = Path("base_map_page.html")

# define path for the final page, deleting it before the rest of the script executes is necessary
final_page = Path("../../site/maps.html")
if final_page.exists():
    os.remove(final_page)
    print("Deleting page...")


# callable which uses a for loop to replace all strings in template with corresponding dictionary key values
def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text

# this callable adds a single entry from a single yaml file
def add_entry(yaml_file: Path):
    print(f"processing: {yaml_file}")
    # parse the yaml file as a dictionary called yaml_data
    with open(yaml_file) as stream:
        try:
            yaml_data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    # modify the data in the template
    new_entry = replace_all(template, yaml_data)
    all_entries = new_entry
    #
    if final_page.exists():
        with open(final_page, "r") as file:
            filedata = file.read()
    else:
        with open(base_html_page, "r") as file:
            filedata = file.read()

    filedata = filedata.replace("<!-- NEW ENTRY -->", new_entry)
    with open(final_page, "w") as file:
        file.write(filedata)

entry_directory = Path("./entries")

for yaml_file in sorted(entry_directory.iterdir()):
    if yaml_file.is_file():
        add_entry(yaml_file)
print("done")
