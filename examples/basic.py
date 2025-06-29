import xml7shi

xr = xml7shi.reader('''
<root>
    <list id="1">
        <item>foo</item>
        <item>bar</item>
        <item>baz</item>
    </list>
</root>
''')

# Read and process each element
while xr.read():
    print(f"Tag: {xr.tag}, Text: {xr.text}, Attributes: {xr.values}")