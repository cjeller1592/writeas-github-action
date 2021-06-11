import writeas
import re
import os

token = os.environ.get('TOKEN')

c = writeas.client()
c.setToken(token)

# p = c.retrievePost('e30m2wbxgsalir1g')

with open('test.md', 'r') as f:
    lines = f.readlines()

# Extract title
title = re.sub('\n', '', lines[0].split("# ",1)[1])

# Extract body
body = ''.join(lines[1:])

post = c.updatePost('e30m2wbxgsalir1g', body=body, title=title)

print(post)

