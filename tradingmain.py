from portfolio import Portfolio
from candleservice import CandleService

menu_options = {
    1: 'Buy',
    2: 'Sell',
    3: 'Hold',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def Buy():
     print('Handle option \'Buy\'')

def Sell():
     print('Handle option \'Sell\'')

def Hold():
     print('Handle option \'Hodl\'')        
        
if __name__ == '__main__':
    print("starting")
    #Initialize portfolio
    print("initializing Portfolio")
    pf = Portfolio(1000)
    cd = CandleService("CandleData.csv")
    print(pf)
    isRunning = True
    while(isRunning):
        print("Adding Candle")
        abcd = input("Add candle ?")
        c_date,c_open,c_high,c_low,c_close,c_volume = cd.get_candle()
        pf.add_candle(c_open,c_high,c_low,c_close,c_volume)
        print("Display Current State")
        print(pf)
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        
        if option == 1:
            pf.action_buy() 
            print(pf)
        elif option == 2:
            pf.action_sell()
            print(pf)
        elif option == 3:
            pf.action_hold()
            print(pf)
        elif option == 4:
            print('Thanks message before exiting')
            isRunning = False
            exit(0)
        else:
            print('Invalid option. Please enter a number between 1 and 4.')