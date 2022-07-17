import re
from io import StringIO

FOOTER_TXT = """
Looking forward to seeing you at #time# !

Thanks,

DisneyStreaming Recruiting
"""

TEMPLATE_TXT = """
Hello #name#,

Your DisneyStreaming interview will be at #time# on #date#

#include footer.txt#
"""


def open(filename):
    if filename == "template.txt":
        return StringIO(TEMPLATE_TXT)
    elif filename == "footer.txt":
        return StringIO(FOOTER_TXT)
    else:
        raise RuntimeError(f"Could not find file: {filename}")


def render(template_filename: str, variables: dict) -> str:
    raw_text = open(template_filename).read()

    for filename in re.findall("#include ([a-zA-Z-_.]+)#", raw_text):
        file_text = open(filename).read()
        raw_text = raw_text.replace(f"#include {filename}#", file_text)

    for key, val in variables.items():
        raw_text = raw_text.replace(f"#{key}#", val)

    return raw_text


if __name__ == "__main__":
    print(
        render("template.txt", {"name": "Piyush", "time": "4pm", "date": "June 20th"})
    )
