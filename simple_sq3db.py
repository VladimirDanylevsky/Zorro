# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 09:58:57 2017

@author: Valder
"""
#execute once

import sqlite3

conn = sqlite3.connect('raw_data.db')
query_line = conn.cursor()


query_line.execute('''CREATE TABLE raw_data_prozorro
                       (page text, next_page text, chunk text, last_date integer primary key)''')