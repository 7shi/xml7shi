import xml7shi

success = 0
total = 0

def test(xml, expected):
    global success, total
    ok = 1
    it = iter(expected.strip().split("\n"))
    print()
    print(xml)
    xr = xml7shi.reader(xml)
    while xr.read():
        val = f"{xr.text};{xr.tag};{xr.values}"
        exp = next(it, None)
        if val == exp:
            print("OK:", val)
        else:
            print("NG:", val)
            print("EXPECTED:", exp)
            ok = 0
    success += ok
    total += 1

test('<tag>test</tag>', """
;tag;{}
test;/tag;{}
""")
test('<tag/>', """
;tag;{}
;/tag;{}
""")
test('<tag />', """
;tag;{}
;/tag;{}
""")
test('<tag a=3>test</tag>', """
;tag;{'a': '3'}
test;/tag;{}
""")
test('<tag a=3/>', """
;tag;{'a': '3'}
;/tag;{}
""")
test('<tag a=3 b=4>', """
;tag;{'a': '3', 'b': '4'}
""")
test('<tag a = 3>', """
;tag;{'a': '3'}
""")
test('<pages index="Dante Alighierik"from=139 to=144 fromsection = B139 tosection=A144  header=1/>', """
;pages;{'index': 'Dante Alighierik', 'from': '139', 'to': '144', 'fromsection': 'B139', 'tosection': 'A144', 'header': '1'}
;/pages;{}
""")
test('<!--foobar--><tag/>', """
;;{'comment': 'foobar'}
;tag;{}
;/tag;{}
""")

print()
print(f"Success: {success}/{total}")
