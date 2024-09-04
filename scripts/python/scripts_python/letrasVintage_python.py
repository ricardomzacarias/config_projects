#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 15:36:26 2023

@author: architectparrot
"""


from termcolor import colored
from pyfiglet import Figlet


f = Figlet(font='standard')
print(colored(f.renderText('Bienvenido a TRIKI!'), 'green'))