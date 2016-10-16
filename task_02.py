#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 8 Synthesizing Task 2"""

DAY_RESULT = raw_input('What day is it today? \n').lower()[:3:]
TIME_RESULT = int(raw_input('What time is it now? \n')[:4:])

SNOOZE = True if DAY_RESULT == 'sat' or DAY_RESULT == 'sun' or \
    TIME_RESULT < 0600 else False

if  not SNOOZE:

    print 'Beep!' * 5
