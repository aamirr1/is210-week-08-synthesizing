#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 8 Synthesizing Task 3"""

import decimal

RECIPIENT = raw_input('What is your name? \n')
PRINCIPAL = int(raw_input('What is the principal of the loan? \n'))
DURATION = int(raw_input('For how long is this being borrowed? \n'))
PRE_QUALIFICATION = raw_input('Are you pre-qualified? \n')

STATUS = PRE_QUALIFICATION[:1].lower() == 'y'
DISPLAY = 'Yes'
TOTAL = 0
INTEREST_RATE = 0

if PRINCIPAL <= 199999:
    if 1 <= DURATION <= 15:
        if STATUS:
            INTEREST_RATE = decimal.Decimal(3.63) / 100
        else:
            INTEREST_RATE = decimal.Decimal(4.65) / 100
            DISPLAY = 'No'
    elif 16 <= DURATION <= 20:
        if STATUS:
            INTEREST_RATE = decimal.Decimal(4.04) / 100
        else:
            INTEREST_RATE = decimal.Decimal(4.98) / 100
            DISPLAY = 'No'

    elif 21 <= DURATION <= 30:
        if STATUS:
            INTEREST_RATE = decimal.Decimal(5.77) / 100
        else:
            INTEREST_RATE = decimal.Decimal(6.39) / 100
            DISPLAY = 'No'
elif 200000 <= PRINCIPAL <= 999999:
    if 1 <= DURATION <= 15:
        if STATUS:
            INTEREST_RATE = decimal.Decimal(3.02) / 100
        else:
            INTEREST_RATE = decimal.Decimal(3.98) / 100
            DISPLAY = 'No'
    elif 16 <= DURATION <= 20:
        if STATUS:
            INTEREST_RATE = decimal.Decimal(3.27) / 100
        else:
            INTEREST_RATE = decimal.Decimal(4.08) / 100
            DISPLAY = 'No'
    elif 21 <= DURATION <= 30:
        if STATUS:
            INTEREST_RATE = decimal.Decimal(4.66) / 100
        else:
            INTEREST_RATE is None
            DISPLAY = 'No'
else:
    if 1 <= DURATION <= 15:
        if STATUS:
            INTEREST_RATE = decimal.Decimal(2.05) / 100
        else:
            INTEREST_RATE = 0
            DISPLAY = 'No'
    elif 16 <= DURATION <= 20:
        if STATUS:
            INTEREST_RATE = decimal.Decimal(2.62) / 100
        else:
            INTEREST_RATE is None
            DISPLAY = 'No'
    else:
        if STATUS:
            INTEREST_RATE is None
        else:
            INTEREST_RATE is None
            DISPLAY = 'No'
        if not STATUS:
            DISPLAY = 'No'

if INTEREST_RATE is None:
    TOTAL = None
else:
    TOTAL = int(
        round(PRINCIPAL * ((1 + (INTEREST_RATE / 12))
                                  ** (12 * DURATION))))


REPORT = ('Loan report for: {:>35}\n'
          '----------------------------------------------------\n'
          'Principal: ${:>40,.0f}\n'
          'Duration: {:>39}yrs\n'
          'Pre-qualified?: {:>36}\n'
          '\n'
          'Total: ${:>44,.0f}')

print REPORT.format(RECIPIENT, PRINCIPAL, DURATION,
DISPLAY, TOTAL)
