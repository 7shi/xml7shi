import xml7shi

def test(xml):
    print()
    print(xml)
    xr = xml7shi.reader(xml)
    while xr.read():
        print(f"{xr.text};{xr.tag};{xr.values}")

test('<tag>test</tag>')
# ;tag;{}
# test;/tag;{}

test('<tag/>')
# ;tag;{}
# ;/tag;{}

test('<tag />')
# ;tag;{}
# ;/tag;{}

test('<tag a=3>test</tag>')
# ;tag;{'a': '3'}
# test;/tag;{}

test('<tag a=3/>')
# ;tag;{'a': '3'}
# ;/tag;{}

test('<tag a=3 b=4>')
# ;tag;{'a': '3', 'b': '4'}

test('<tag a = 3>')
# ;tag;{'a': '3'}

test('<pages index="Dante Alighierik"from=139 to=144 fromsection = B139 tosection=A144  header=1/>')
# ;pages;{'index': 'Dante Alighierik', 'from': '139', 'to': '144', 'fromsection': 'B139', 'tosection': 'A144', 'header': '1'}
# ;/pages;{}

test('<!--foobar--><tag/>')
# ;;{'comment': 'foobar'}
# ;tag;{}
# ;/tag;{}
