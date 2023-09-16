# import time
# import datetime
# import pandas as pd
 
import json
from json import dumps,loads
from time import sleep
from kafka import KafkaConsumer 
import boto3
import logging
 

logger = logging.getLogger() 
 
KAFKA_BOOTSTRAP_SERVER="broker:29092"

consumer = KafkaConsumer('demo_testing2',value_deserializer=lambda x:loads(x.decode('utf-8')),bootstrap_servers=[KAFKA_BOOTSTRAP_SERVER])

                        
def get_data_from_producer():
    while True:
        try:
            for msg in consumer:
                cryptoRecord = msg.value
                logging.info(msg.value,'Data come from producer')
                def convert_value(value_str):
                    if value_str == 'N/A':
                        return None
                    value_str = value_str.replace('%', '')
                    return float(value_str.replace('$', '').replace('B', 'E9').replace('M', 'E6').replace(',', '').replace(' ', ''))
                transform_data = {
                            'SYSTEM_INSERTED_TIMESTAMP': cryptoRecord['SYSTEM_INSERTED_TIMESTAMP'], 
                            'RANK': int(cryptoRecord['RANK']),
                            'NAME': cryptoRecord['NAME'],
                            'SYMBOL': cryptoRecord['SYMBOL'],
                            'PRICE': float(cryptoRecord['PRICE'].replace('$', '').replace(',', '').replace(' ', '')),
                            'PERCENT_CHANGE_24H': float(cryptoRecord['PERCENT_CHANGE_24H'].replace('%', '').replace(',', '').replace(' ', '')),
                            'VOLUME_24H': convert_value(cryptoRecord['VOLUME_24H']),
                            'MARKET_CAP':convert_value(cryptoRecord['MARKET_CAP']),
                            # 'VOLUME_24H': float(cryptoRecord['VOLUME_24H'].replace('$', '').replace('B', 'E9').replace('M', 'E6').replace(',', '').replace(' ', '')),
                            # 'MARKET_CAP': float(cryptoRecord['MARKET_CAP'].replace('$', '').replace('B', 'E9').replace('M', 'E6').replace(',', '').replace(' ', '')),
                            'CURRENCY': 'USD'
                        }
                # Convert datetime to string format
                json_str = json.dumps(transform_data)
                # print(json_str)
                file_name = "real_time_data/top_100_crypto_data_" + str(cryptoRecord['SYSTEM_INSERTED_TIMESTAMP']) + '_' + str(cryptoRecord['RANK']) + '.json'
                s3 = boto3.client('s3', aws_access_key_id='AKIAXONTFZ3BXZON2AI2', aws_secret_access_key='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',region_name='us-east-1')
                response = s3.put_object(
                        Bucket='kafka-stock-market-video-mudassir',
                        Key=file_name,
                        Body=json_str)    
                print("file_uploaded sucessfully: ",file_name)
                # sleep(1)
                
        except KeyboardInterrupt:
            break
    print("ALl datauploaded sucessfully.Now consumer going to be closed")    
    consumer.close() 

get_data_from_producer() 
 



# ,api_version=(0, 10, 1)
# consumer = KafkaConsumer(
#    'test',
#     auto_offset_reset='earliest',
#     enable_auto_commit=True,
#     group_id='my-group-1',
#     value_deserializer=lambda m: loads(m.decode('utf-8')),
#     bootstrap_servers=['172.17.0.1:32783','172.17.0.1:32782','172.17.0.1:32781'])

# for m in consumer:
#     print(m.value) 


#local file create
            # with open(file_name, 'w') as file:
            #     file.write(json_str)
            #     print(f"Data saved to {file_name}")

            # print(transform_data)
            # sleep(1)