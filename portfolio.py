# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:21:12 2023

@author: balak
"""

class Portfolio():
    
    total_amount = 0
    
    def __init__(self,total_amount):
        self.total_amount = total_amount
        self.invested = 0.0
        self.balance = self.total_amount - self.invested
        self.realized = 0.0
        self.unrealized = 0.0
        self.open_trades = 0
        self.closed_trades = 0
        self.open_price = 0.0
        self.high_price = 0.0
        self.low_price = 0.0
        self.close_price = 0.0
        self.volume = 0.0
        self.last_trade_open_price = 0.0
        self.last_trade_type = ''
        self.last_trade_amount = 0.0
        self.last_trade_close_price = 0.0
        self.reward = 0.0
        
    def add_candle(self,open_price,high_price,low_price,close_price,volume):
        self.open_price = open_price
        self.high_price = high_price
        self.low_price = low_price
        self.close_price = close_price
        self.volume = volume
        if self.open_trades != 0:
            #Update profit loss based on new candle values
            units = self.last_trade_amount/self.last_trade_open_price
            
            if self.last_trade_type == 'BUY':
                price_diff = self.close_price-self.last_trade_open_price
            else:
                price_diff = self.last_trade_open_price - self.close_price
            
            pnl = units* price_diff
            self.unrealized = pnl
        
        
    def action_buy(self):
        print("Buying action")
        if self.open_trades !=0 and self.last_trade_type == 'SELL':
            #CLose the short trade which is open
            print("closing trade")
            self.last_trade_close_price = self.close_price
            self.open_trades = 0
            self.closed_trades +=1
            self.realized += self.unrealized
            self.total_amount += self.unrealized
            
            self.invested = 0
            self.balance = self.total_amount - self.invested
            self.last_trade_open_price = 0.0
            self.last_trade_type = ''
            self.last_trade_amount = 0.0
            if self.unrealized > 0:
                self.reward = 0.2
            else:
                self.reward = -0.3
            self.unrealized = 0
            
        else:
            if self.open_trades == 0 and self.balance > 500:
                self.open_trades = 1
                self.invested = self.invested + 100.0
                self.last_trade_amount = 100.0
                self.balance = self.total_amount - self.invested
                self.last_trade_open_price = self.open_price
                self.last_trade_type = 'BUY'
                self.reward = 0.1
            else:
                self.reward = 0
            
            
    def action_sell(self):
        print("Selling action")
        if self.open_trades !=0 and self.last_trade_type == 'BUY':
            #CLose the trade which is open
            print("closing trade")
            self.last_trade_close_price = self.close_price
            self.open_trades = 0
            self.closed_trades +=1
            self.realized += self.unrealized
            self.total_amount += self.unrealized
            
            self.invested = 0
            self.balance = self.total_amount - self.invested
            self.last_trade_open_price = 0.0
            self.last_trade_type = ''
            self.last_trade_amount = 0.0
            
            if self.unrealized > 0:
                self.reward = 0.2
            else:
                self.reward = -0.3
            self.unrealized = 0
            
        else:
            #Open new sell trade
            if self.open_trades == 0 and self.balance > 500:
                self.open_trades = 1
                self.invested = self.invested + 100.0
                self.last_trade_amount = 100.0
                self.balance = self.total_amount - self.invested
                self.last_trade_open_price = self.open_price
                self.last_trade_type = 'SELL'
                self.reward = 0.1
            else:
                self.reward = 0
                
    def action_hold(self):
        print("Hold action")
        if self.open_trades ==0:
            self.reward = -0.7
        else:
            self.reward = -0.6
            
    def trade(self,action):
        if action == "BUY":
            self.action_buy()
            
        elif action == "SELL":
            self.action_sell()
            
        else:
            self.action_hold()
            
        return self.reward
        

    def getstate(self):
        
        return [self.unrealized,self.open_trades,self.open_price,self.high_price,self.low_price,self.close_price,self.volume,self.last_trade_open_price]
        

    def __str__(self):
        return "Portfolio[total_amount={},invested={},balance={},realized={},\
            unrealized={},open_trades={},closed_trades={},open_price={},high_price={}\
            low_price={},close_price={},volume={},last_trade_open_price={},\
            last_trade_type={},last_trade_amount={}]".format(self.total_amount,\
            self.invested,self.balance,self.realized,self.unrealized,self.open_trades,\
            self.closed_trades,self.open_price,self.high_price,self.low_price,self.close_price,\
                self.volume,self.last_trade_open_price,self.last_trade_type,self.last_trade_amount)
    
    
    
    
    
    
    
    
    
    
    
    
    