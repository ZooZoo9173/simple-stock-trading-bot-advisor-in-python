'''API key : NASDAQ '''
import nasdaqdatalink
NASDAQ_DATA_LINK_API_KEY = 'dz4P57-ncNFiWsUsK7J-'

'nasdaqdatalink.read_key(filename="/data/.datalinkapikey")'
data = nasdaqdatalink.get('NSE/OIL')
data2 = nasdaqdatalink.get_table('ZACKS/FC', ticker='AAPL')

print(data2)
'''
plt.figure(figsize=(12, 8))
plt.bar(data[],data[], color="blue")
plt.xticks(rotation=90)
plt.xlabel("Country")
plt.ylabel("GDP (Current US$)")
plt.title("Top 50 Countries by GDP")
plt.tight_layout()
plt.show()
'''
print('----------------------Great Success--------------------------')