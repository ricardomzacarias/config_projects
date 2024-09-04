#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:50:46 2023

@author: bubu
"""

import keyboard as kb
# import sys 
# sys.path.insert(0,'/home/bubu/.local/lib/python3.11/site-packages/keyboard')

rec = kb.record(until="escape")

seq = kb.get_typed_strings(rec)
print("".join(seq))