import pandas as pd
from services import detect_encoding as encode
from services.progress_bar import ProgressBar


def get_data(source):
    print(f"Обрабатываю файл: {source}")
    pb = ProgressBar(200, prefix='Обработка')
    chunk_size = 10000 # строк за раз
    bearish = 0
    bullish = 0
    for chunk in pd.read_csv(source, chunksize=chunk_size, encoding=encode.get_encoding(source)):
        for index, row in chunk.iterrows():
            if row['open'] > row['close']:
                bearish += 1
            else:
                bullish += 1
        pb.update()
    pb.finish()

    return (
        f"Количество медвежих свечей: {bearish}, "
        f"количество бычьих свечей: {bullish}"
    )


# open_time,open,high,low,close,volume,close_time,quote_asset_volume,number_of_trades,taker_buy_base_asset_volume,\
# taker_buy_quote_asset_volume

# 2024-09-13 10:00:00,0.3794,1.0,0.378,0.4092,4224830.8,1970-01-20 23:30:21.659999,1806219.20231,8565,2307013.3,
# 981119.54358

# 2024-09-13 10:05:00,0.4053,0.4096,0.3935,0.3951,1297652.9,1970-01-20 23:30:21.959999,519515.08503,1661,611658.2,
# 245360.74548

# Index(['open_time', 'open', 'high', 'low', 'close', 'volume', 'close_time',
#        'quote_asset_volume', 'number_of_trades', 'taker_buy_base_asset_volume',
#        'taker_buy_quote_asset_volume'],
#       dtype='object')
