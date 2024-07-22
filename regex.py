import re
a="maariraj302@gmail.com"
for i in range(10):
    pattern=r'\b\w+@'
    match=re.findall(pattern,a)
    print(match)