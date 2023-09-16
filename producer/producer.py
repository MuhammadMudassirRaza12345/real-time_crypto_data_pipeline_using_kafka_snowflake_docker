from bs4 import BeautifulSoup
import requests
import time
import datetime
import pandas as pd
# # import argparse
import json
from json import dumps
from time import sleep
from kafka import KafkaProducer
import logging 
 
KAFKA_BOOTSTRAP_SERVER = "broker:29092"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# # headers = {
# #     'User-Agent':'(Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15)'
# #     }

producer = KafkaProducer(
        bootstrap_servers=[KAFKA_BOOTSTRAP_SERVER],
        value_serializer=lambda x:dumps(x).encode('utf-8'),
        api_version=(0, 10, 1))


def scrape_data(url):
    allRecordsCombined = []
    for page in range(1,10):
        response = requests.get(url+str(page))
        soup = BeautifulSoup(response.content,'html.parser')
        current_timestamp = datetime.datetime.now() 
        treeTag = soup.find_all('tr')
        for tree in treeTag[1:]:
            rank = tree.find('td',{'class': 'css-w6jew4'}).get_text()
            name = tree.find('p',{'css-rkws3'}).get_text()
            symbol = tree.find('span',{'class':'css-1jj7b1a'}).get_text()
            market_cap = tree.find('td',{'class':'css-15lyn3l'}).get_text()
            price_arr = str(tree.find('div',{'class':'css-16q9pr7'}).get_text())
            if('-' in price_arr):
                price_arr = price_arr.split('-')
                change_24h = '-'+price_arr[1]
            else:
                price_arr = price_arr.split('+')
                change_24h = '+'+price_arr[1]
            price = price_arr[0]
            volume_24 = tree.find('td',{'class':'css-15lyn3l'}).get_text()
            current_timestamp_str = current_timestamp.strftime('%Y-%m-%d %H:%M:%S')
            allRecordsCombined.append([current_timestamp_str, rank, name, symbol, price, change_24h, volume_24, market_cap])
            
        #print('\n','\n','\n','\n','\n','page N0 :',page,allRecordsCombined,'\n','\n','\n','\n','\n')

    columns = ['SYSTEM_INSERTED_TIMESTAMP', 'RANK','NAME', 'SYMBOL', 'PRICE', 'PERCENT_CHANGE_24H','VOLUME_24H', 'MARKET_CAP']
    df = pd.DataFrame(columns=columns, data=allRecordsCombined)
    while True:
        for row in df.iterrows():
            dict_stock = row[1].to_dict()
            producer.send('demo_testing2', value=dict_stock)
            # print(dict_stock, '\n')
            logging.info(dict_stock,'Data send to consumer')
            producer.flush
            sleep(1)
 
scrape_data('https://crypto.com/price?page=')    

 

# import logging
# from kafka import KafkaProducer
# from json import dumps

# KAFKA_BOOTSTRAP_SERVER = "broker:29092"

# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger()

# try:
    # producer = KafkaProducer(
    #     bootstrap_servers=[KAFKA_BOOTSTRAP_SERVER],
    #     value_serializer=lambda x: dumps(x).encode('utf-8'),
    #     api_version=(0, 10, 1)
#     )
#     producer.send('demo_testing2', value={'number': 1})
#     logger.info('Data sent to consumer')
# except Exception as e:
#     logger.error(f"Error: {e}")