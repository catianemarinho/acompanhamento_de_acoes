import yfinance as yf

def get_price(ticker):
    df = yf.Ticker(ticker).history(period='1y')
    df.reset_index(inplace=True)
    df["ticker"] = ticker.split(".")[0]
    return df

petra = get_price('PETR4.SA')
bb = get_price('BBAS3.SA')
vale = get_price('VALE3.SA')
