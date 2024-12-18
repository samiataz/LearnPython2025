# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 17:15:34 2024

@author: samiataz
"""
from string import Template
myStr=Template("my name is $name and I am learning $lang")
print(myStr.substitute(name="John",lang="python"))

