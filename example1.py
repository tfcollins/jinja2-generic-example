from jinja2 import Environment, FileSystemLoader
import os

template_filename = "template1.txt"
output_filename = "output1.txt"

# Data for template
data = {
    "title": "MyTitle",
    "devices": [
        {"name": "dev1", "iscool": True},
        {"name": "dev2", "iscool": False},
        {"name": "dev3", "iscool": True},
    ],
}

# Import template
loc = os.path.dirname(__file__)
loc = os.path.join(loc, "templates")
file_loader = FileSystemLoader(loc)
env = Environment(loader=file_loader)

loc = os.path.join(template_filename)
template = env.get_template(loc)
output = template.render(data=data)

with open(output_filename, "w") as f:
    f.write(output)
