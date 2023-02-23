from portfolio import Portfolio
from candleservice import CandleService


from ai import Dqn


brain = Dqn(8,3,0.9)
actontotrade = ['BUY','SELL','HOLD']
last_reward = 0
scores = []


first_update = True
def init():
    global goal
    global first_update
    global pf
    pf = Portfolio(1000)
    global cd
    cd = CandleService("CandleData.csv")
    goal = 1010
    first_update = False
    print("initiated")
    print(pf)
       
        
if __name__ == '__main__':
    if first_update:
        init()
    for j in range(100):
        cd = CandleService("CandleData.csv")
        for i in range(cd.get_length()-1):
            print(i)
            c_date,c_open,c_high,c_low,c_close,c_volume = cd.get_candle()
            pf.add_candle(c_open,c_high,c_low,c_close,c_volume)
            last_signal = pf.getstate()
            action = brain.update(last_reward, last_signal)
            scores.append(brain.score())
            new_action = actontotrade[action]
            last_reward = pf.trade(new_action)
            print(pf)
        
        #aaa=input('Enter your choice: ')
