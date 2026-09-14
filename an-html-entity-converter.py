import re

def convert_html(string):
    html_entities = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;",
        "'": "&apos;",
    }

    return re.sub(
        r'[&<>"\']',lambda match: html_entities[match.group(0)],string
    )