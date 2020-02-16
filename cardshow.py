import os
page_header = """
<html>
    <head>
        <meta charset="utf-8">
        <title>cardshow</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/milligram/1.3.0/milligram.css" integrity="sha256-7LuOHbsBImoaCHWzjqQDLeGK9kq/rZZqIr6Gtkz0WzI=" crossorigin="anonymous" />
        <link href="https://fonts.googleapis.com/css?family=Farro|Oswald|Roboto+Condensed&display=swap" rel="stylesheet"> 
        <style type="text/css">
            @media print, screen {
                .card, .column {
                    border: 1px solid #000;
                    height: 88mm;
                    width: 63mm;
                    margin-top: 5px;
                    padding: 5px;
                }
                .right-margin {
                    margin-right: 5px;
                }
                .card p {
                    font-family: 'Oswald', 'Roboto Condensed', arial, helvetica, 'Farro', sans-serif;
                    font-weight: bold;
                    color: #000;
                    font-size: 25px;
                    letter-spacing: 0.01px;
                }
                .questions {
                    background-color: #000;
                }
                .questions p {
                    color: #fff;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
"""
page_footer = """
        </div>
    </body>
</html>
"""


def fetch(file):
    with open(file, 'r', encoding='utf8') as f:
        contents = f.read()
    lines = contents.split('\n')
    return lines

def get_card_html(text, position_in_row, card_type = 'answers'):
    card_class = 'card questions' if card_type == 'questions' else 'card'
    if position_in_row < 3:
        card_class += " right-margin"
    html = """\n\t<div class="column {}"><p>{}</p></div>""".format(card_class, text)
    return html


def build(what):
    entries = fetch('{}.txt'.format(what))
    page = page_header
    position_in_row = 0
    for idx, line in enumerate(entries):
        position_in_row += 1 # print row <div> every three cards so we get a new line
        if position_in_row == 1:
            page += '\n<div class="row">'
        page += get_card_html(line, position_in_row, what)

        if position_in_row == 3:
            page += '</div>'
            position_in_row = 0

        # make sure we end our page with blanks, if we have to
        elif idx == len(entries)-1:
            while position_in_row < 3:
                position_in_row += 1
                page += get_card_html('', position_in_row, what)
            page += '</div>'
            

    page += page_footer
    return page

def export(what):
    page = build(what)
    with open('{}.html'.format(what), 'w', encoding='utf8') as f:
        f.write(page)
    return

export('questions')
export('answers')