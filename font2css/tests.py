#!/usr/bin/env python

"""tests.py: Testing for font2css
"""

__author__ = "Jean-Martin Archer"
__copyright__ = "Copyright 2013, MIT License."

import nose
from font2css import *


def test_generateFontList():

    directory = 'example'

    expected = [('OpenSans-Bold', 'example/Open_Sans/OpenSans-Bold.ttf'),
                ('OpenSans-BoldItalic',
                'example/Open_Sans/OpenSans-BoldItalic.ttf'),
                ('OpenSans-ExtraBold',
                'example/Open_Sans/OpenSans-ExtraBold.ttf'),
                ('OpenSans-ExtraBoldItalic',
                 'example/Open_Sans/OpenSans-ExtraBoldItalic.ttf'),
                ('OpenSans-Italic', 'example/Open_Sans/OpenSans-Italic.ttf'),
                ('OpenSans-Light', 'example/Open_Sans/OpenSans-Light.ttf'),
                ('OpenSans-LightItalic',
                'example/Open_Sans/OpenSans-LightItalic.ttf'),
                ('OpenSans-Regular', 'example/Open_Sans/OpenSans-Regular.ttf'),
                ('OpenSans-Semibold',
                'example/Open_Sans/OpenSans-Semibold.ttf'),
                ('OpenSans-SemiboldItalic',
                'example/Open_Sans/OpenSans-SemiboldItalic.ttf'),
                ('Quicksand-Bold', 'example/Quicksand/Quicksand-Bold.ttf'),
                ('Quicksand-Light', 'example/Quicksand/Quicksand-Light.ttf'),
                ('Quicksand-Regular', 'example/Quicksand/Quicksand-Regular.ttf')]

    results = generateFontList(directory)

    assert(results == expected)


def test_decodeFontName():

    inputs = ['OpenSans-LightItalic',
              'Quicksand-Bold', 'OpenSans-ExtraBoldItalic']
    expected = [('OpenSans', 'italic', '300'),
                ('Quicksand', 'regular', '700'), ('OpenSans', 'italic', '700')]

    for (count, item) in enumerate(inputs):
        result = decodeFontName(item)

        assert(result == expected[count])


def test_replace_all():

    inputs = 'abc'
    input_replace = {'a': '4', 'b': '5', 'c': '6'}
    expected = '456'

    result = replace_all(inputs, input_replace)

    assert(expected == result)


def test_generateCSSdata():

    inputs = ('Quicksand-Regular', 'example/Quicksand/Quicksand-Regular.ttf')

    results = generateCSSdata(inputs[0], inputs[1])
    expected = """
    @font-face {
        font-family: 'Quicksand';
        font-style: regular;
        font-weight: 400;
        src: url(data:font/truetype;charset=utf-8;base64,AAEAAAAPAIAAAwBwRFNJRwAAAAEAAFzMAAAA"""

    # The results is truncated because the expected string would be too long.
    assert(results[0:200] == expected)
