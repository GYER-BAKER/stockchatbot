from iexfinance import get_historical_data
from datetime import datetime


def get_history(stock,start_year,start_month,start_day,end_year,end_month,end_day):
    start = datetime(start_year, start_month, start_day)
    end = datetime(end_year, end_month, end_day)
    df = get_historical_data(stock, start=start, end=end, output_format='pandas')
    return df