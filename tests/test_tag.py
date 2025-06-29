import xml7shi

def _run_test(xml, expected):
    xr = xml7shi.reader(xml)
    result = []
    while xr.read():
        result.append(f"{xr.text};{xr.tag};{xr.values}")
    assert result == expected

def test_simple_tag():
    _run_test('<tag>test</tag>', [
        ';tag;{}',
        'test;/tag;{}'
    ])

def test_self_closing_tag():
    _run_test('<tag/>', [
        ';tag;{}',
        ';/tag;{}'
    ])

def test_self_closing_tag_with_space():
    _run_test('<tag />', [
        ';tag;{}',
        ';/tag;{}'
    ])

def test_tag_with_attribute():
    _run_test('<tag a=3>test</tag>', [
        ";tag;{'a': '3'}",
        'test;/tag;{}'
    ])

def test_self_closing_tag_with_attribute():
    _run_test('<tag a=3/>', [
        ";tag;{'a': '3'}",
        ';/tag;{}'
    ])

def test_tag_with_multiple_attributes():
    _run_test('<tag a=3 b=4>', [
        ";tag;{'a': '3', 'b': '4'}"
    ])

def test_tag_with_space_in_attribute():
    _run_test('<tag a = 3>', [
        ";tag;{'a': '3'}"
    ])

def test_complex_tag():
    _run_test('<pages index="Dante Alighieri"from=139 to=144 fromsection = B139 tosection=A144  header=1/>', [
        ";pages;{'index': 'Dante Alighieri', 'from': '139', 'to': '144', 'fromsection': 'B139', 'tosection': 'A144', 'header': '1'}",
        ';/pages;{}'
    ])

def test_comment_with_tag():
    _run_test('<!--foobar--><tag/>', [
        ";;{'comment': 'foobar'}",
        ';tag;{}',
        ';/tag;{}'
    ])
