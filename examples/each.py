import xml7shi

# Parse XML string
xml = '''<?xml version="1.0" encoding="UTF-8"?>
<root>
  <item id="1">First item</item>
  <item id="2">Second item</item>
</root>'''

# Create reader instance
xr = xml7shi.reader(xml)

# Iterate through each 'item' element
for _ in xr.each("item"):
    id = xr["id"]
    # Read the content of the current element
    if xr.read():
        print(f"ID: {id}, Content: {xr.text}")