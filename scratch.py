# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:43:02 2023

@author: balak
"""

from candleservice import CandleService

cd = CandleService("CandleData.csv")

print(cd.get_length())

c_date,c_open,c_high,c_low,c_close,c_volume = cd.get_candle()

print(c_open)

