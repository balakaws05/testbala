# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:39:02 2023

@author: balak
"""
import pandas as pd

class CandleService:
    
    def __init__(self,file_name):
        self.ds = pd.read_csv(file_name)
        self.current_index = 0
        
        
    def get_candle(self):
        df = self.ds.iloc[self.current_index]
        self.current_index += 1
        return df["Date"],df["Open"],df["High"],df["Low"],df["Close"],df["Volume"]
    
    def get_length(self):
        return self.ds["Date"].size