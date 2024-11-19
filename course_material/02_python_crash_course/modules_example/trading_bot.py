module_variable1 = 'Some Variable'

def do_something():
    print('Doing something...')

class TradingBot:
    # initializing default when creating the class
    def __init__(self, name, account_balance, account_currency):
        # properties
        self.name = name
        self.account_balance = account_balance
        self.account_currency = account_currency

    # methods
    def open_trade(self, symbol, order_type, volume):
        print(f'The Bot is opening a {order_type} trade on {symbol} with volume {volume}')

    def close_all_trades(self):
        print('The Bot is closing all trades now')