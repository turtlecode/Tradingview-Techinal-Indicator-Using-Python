from tradingview_ta import TA_Handler, Interval, Exchange


output = TA_Handler(
    symbol="BTCUSDT",
    screener="Crypto",
    exchange="Coinbase",
    interval=Interval.INTERVAL_5_MINUTES
    )
print('Symbol : ' + output.symbol)
print((str(output.get_analysis().summary['RECOMMENDATION'])))


