#!/usr/bin/env python

"""font2css.py: Embeddeds font files in CSS.

Walks through directories (and sub directories), encode TTF and OTF files
with base64 and save the result to a CSS file.
"""

__author__      = "Jean-Martin Archer"
__copyright__   = "Copyright 2013, Do what you want with it"

import base64
import os


def generateFonts(directory, output):
    """
    Main function that generates the css file.
    """

    file_content = ''

    fonts = generateFontList(directory)

    print fonts

    for (font, path) in fonts:
        file_content += generateCSSdata(font, path)

    saveCSS(file_content, output)

    print 'Done'


def generateFontList(directory):

    font_list = []
    files = os.walk(directory, followlinks=True)

    for (dirpath, dirnames, filenames) in files:

        for filename in filenames:
            (file_basename, file_extension) = os.path.splitext(filename)
            
            if file_extension in ['.ttf', '.otf']:
                font_list.append(
                    (file_basename, os.path.join(dirpath, filename)))

    return font_list


def decodeFontName(font_name):
    """
    Presume weight and style based on the font filename.
    """

    name = font_name.split('-')[0]

    font_name = font_name.lower()

    weight = 400
    style = 'regular'

    weights = {'light': 300,
               'extralight': 200,
               'bold': 700,
               'semibold': 600,
               'extrabold': 800, }

    for weight_item in weights.keys():
        if weight_item in font_name:
            weight = str(weights[weight_item])

    if 'italic' in font_name:
        style = 'italic'

    return (name, style, str(weight))


def generateCSSdata(font_name, path):

    (name, style, weight) = decodeFontName(font_name)

    base_css = '''
    @font-face {
        font-family: '{{name}}';
        font-style: {{style}};
        font-weight: {{weight}};
        src: url(data:font/truetype;charset=utf-8;base64,{{data}}) format("truetype");
    }

    '''

    details = {
        "{{name}}": name,
        '{{style}}': style,
        '{{weight}}': weight,
        '{{data}}': encodeFile(path)
    }

    return replace_all(base_css, details)


def saveCSS(data, output_path):

    file = open(output_path, 'w')

    file.write(data)
    file.close()


def encodeFile(path):
    data = open(path, 'rb').read()
    return base64.b64encode(data)


def replace_all(text, dic):
    for i, j in dic.iteritems():
        text = text.replace(i, j)
    return text

if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--directory", help="Specify which directory to walk through.")
    parser.add_argument("-o", "--output", help="Specify file to output to.")
    args = parser.parse_args()

    if args.directory:
        directory = args.directory
    else:
        directory = '.'

    if args.output:
        output = args.output
    else:
        output = './fonts.css'

    generateFonts(directory, output)
