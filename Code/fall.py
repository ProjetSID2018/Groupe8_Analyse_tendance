# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 16:37:36 2018

@author: samba
"""
import pandas
import re
def findOGR(text):
    pattern = "live in"
    for val in re.finditer('[A-Z]\.+([A-Z]\w+)'+pattern, text):
        print (val.group(0))
def main():
    df = pandas.DataFrame.from_csv("simplewiki.csv", encoding='utf-8')
    for page in list(df['text']):
        findOGR(page)
if __name__ == "__main__":
    main()


