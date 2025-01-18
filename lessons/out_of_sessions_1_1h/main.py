import MetaTrader5 as mt5
import pandas as pd
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()

symbol = "EURUSD_i"
time_frame = 30
number_candles = 100
rates_frame = pd.DataFrame()
rates = mt5.copy_rates_from_pos(symbol, time_frame, 0, number_candles)
if rates is None:
    print(mt5.last_error())
    quit()
else:
    rates_frame = pd.DataFrame(rates)
    rates_frame['time'] = pd.to_datetime(rates_frame['time'], unit='s')

rates_frame.to_excel(f"{symbol}_{time_frame}_candlestick.xlsx", index= False)

