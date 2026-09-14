import re

def convert_markdown(text:str)->str:
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img alt="\1" src="\2">', text)
    
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', text)
    
    text = re.sub(r'^[ \t]*### (.*)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^[ \t]*## (.*)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^[ \t]*# (.*)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    
    text = re.sub(r'^[ \t]*> (.*)$', r'<blockquote>\1</blockquote>', text, flags=re.MULTILINE)
    
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'__(.*?)__', r'<strong>\1</strong>', text)
    
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    text = re.sub(r'_(.*?)_', r'<em>\1</em>', text)

    return text.replace('\n','')

print()
print(convert_markdown("# title 1"))

print(convert_markdown("> **this is a *quote***"))

print(convert_markdown("![alt](src)\n[link](url)"))