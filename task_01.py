#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 8 Synthesizing Task 1"""

BASE = raw_input('Which base color, "Seattle Gray" or "Mantee"? ')

if BASE is 'Seattle Gray':
    ACCENT = raw_input('Which accent color, "Ceramic Glaze" or'
                       '"Cumulus Nimbus"?: ')
    if ACCENT is 'Ceramic Glaze':
        HIGHLIGHT = raw_input('Which highlight color, "Basically'
                              'White" or "White"?: ')
else:
    ACCENT = raw_input('Which accent color,"Platinum Mist"'
                       'or "Spartan Sage"? ')
    if ACCENT is 'Platinum Mist':
        HIGHLIGHT = raw_input('Which highlight color, "Bone White"'
                              'or "Just White"? : ')
    else:
        HIGHLIGHT = raw_input('Which highlight color, "Fractal White"'
                              'or "Not White"?: ')

OUTPUT = 'Your selected colors are, {} , {} , and {} '.\
    format(BASE, ACCENT, HIGHLIGHT)

print OUTPUT
