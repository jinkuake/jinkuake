import requests
url = 'http://quote.eastmoney.com/center/gridlist.html#hs_a_board'
response = requests.get(url=url)
html_data = response.json()
data_list = html_data['data']['list']
for i in data_list:
 dit = {}
 dit['股票代码'] = i['symbol']
 dit['股票名字'] = i['name']
 dit['当前价'] = i['current']
 dit['涨跌额'] = i['chg']
 dit['涨跌幅/%'] = i['percent']
 dit['年初至今/%'] = i['current_year_percent']
 dit['成交量'] = i['volume']
 dit['成交额'] = i['amount']
 dit['换手率/%'] = i['turnover_rate']
 dit['市盈率TTM'] = i['pe_ttm']
 dit['股息率/%'] = i['dividend_yield']
 dit['市值'] = i['market_capital']
 print(dit)