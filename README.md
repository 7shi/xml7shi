# xml7shi

A pull-based simple and permissive XML parser for Python.

## Why xml7shi?

Originally developed around 2000 for SGML parsing, xml7shi emerged from the need to handle imperfect HTML/XML with missing closing tags. It uses a pull-based parsing model where the application actively reads the next element, providing fine-grained control over the parsing process.

The name is admittedly a personal project identifier. If you find the name off-putting, please feel free to fork this project under a different name - it's released under CC0, so you have complete freedom to do so.

## Design Philosophy

Unlike DOM parsers that build a complete tree structure in memory, xml7shi processes documents as a flat stream of events. This makes it particularly suitable for:
- Web scraping from sites with imperfect HTML
- Processing large XML files where memory efficiency matters
- Extracting specific data without needing full document structure
- Legacy system integration where strict XML compliance cannot be guaranteed

## Features

- **Practical parsing**: Handles malformed or incomplete XML/HTML gracefully
- **Memory efficient**: Processes documents as a stream without building a DOM tree
- **Pull-based model**: Application controls parsing flow by requesting next elements
- **No external dependencies**: Pure Python implementation
- **Permissive parsing**: Designed for real-world HTML with structural issues

Detailed description (in Japanese): https://qiita.com/7shi/items/d8d3ab5371aa9dddcb3e

## Installation

### As a library

To use xml7shi as a library in your project:

```bash
uv add https://github.com/7shi/xml7shi.git
```

### For development

To download and develop the project:

```bash
git clone https://github.com/7shi/xml7shi.git
cd xml7shi
uv sync
```

## API Reference

`xml7shi.reader`: Main parser class that reads XML content.

Methods:

- `read()`: Read next element
- `find(tag, **kwargs)`: Find next element matching tag and attributes
- `each(tag="", **kwargs)`: Returns a generator that iterates over elements matching the tag and attributes

Notes:

- `kwargs` is a dictionary of attribute names and values to match in the element. For example, `find("item", id="1")` will find the next `<item>` element with matching attributes

## Examples

### Basic Example (Using read())

```python
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
```

### Generator Example (Using each())

```python
import xml7shi

# Parse XML string
xml = '''<?xml version="1.0" encoding="UTF-8"?>
<root>
  <item id="1">First item</item>
  <item id="2">Second item</item>
</root>'''

# Create reader instance
xr = xml7shi.reader(xml)

# Iterate through each 'item' element using generator
for _ in xr.each("item"):
    id = xr["id"]
    # Read the content of the current element
    if xr.read():
        print(f"ID: {id}, Content: {xr.text}")
```

Notes:

- The reader instance `xr` is stateful; its internal state changes with each read operation

## Specifications

Based on the test cases, the parser adheres to the following behaviors:

**Tag Processing:**
- Tag names are treated as case-insensitive and are normalized to lowercase.
- Standard opening (`<tag>`), closing (`</tag>`), and text content are parsed sequentially.
- Self-closing tags, both with and without spaces (`<tag/>`, `<tag />`), are treated as a distinct opening tag followed immediately by a corresponding closing tag.
- When a tag is read, `xr.text` is empty for opening tags, and contains the preceding text content for closing tags.

**Attribute Handling:**
- Attribute names are treated as case-insensitive and are normalized to lowercase.
- Attributes are parsed from opening tags and stored in the `values` dictionary.
- Multiple attributes within a single tag are supported.
- Attribute values are always returned as strings.
- The parser is permissive, allowing spaces around the equals sign in attribute assignments (e.g., `a = 3`).
- Attributes can be specified with or without quotes. For instance, `from=139` and `index="Dante Alighieri"` are both valid.
- Attributes without values (e.g., `<input checked>`) are parsed with empty string values.

**Comment Processing:**
- HTML-style comments (`<!--comment-->`) are parsed as a special case.
- When a comment is read, the `tag` property is empty, and the comment's content is stored in the `values` dictionary under the key `'comment'`.

**Parser State:**
- Each `read()` operation returns the next element (opening tag, closing tag, or comment).
- The parser maintains three main properties:
  - `text`: The text content preceding the current tag
  - `tag`: The name of the current tag (empty for comments)
  - `values`: A dictionary containing attributes (for opening tags) or special values (for comments)

**General Behavior:**
- The parser does not build a tag hierarchy (DOM tree). It processes the XML as a flat stream of events.

For detailed parsing behavior examples and edge cases, see the [test cases](tests/test_tag.py).

## Testing

Run the test suite with:

```bash
uv run pytest
```

## Developer Notes

This project uses [uv](https://docs.astral.sh/uv/) as its package manager and [hatchling](https://hatch.pypa.io/) as its build backend.

**Building:**

```bash
uv build
```

This will generate wheel and source distribution files in the `dist` directory.

**Installing from built package:**

```bash
uv pip install dist/*.whl
```

The project configuration is managed through `pyproject.toml`, which includes all dependencies and build settings.
