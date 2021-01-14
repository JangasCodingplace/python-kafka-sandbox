import os
import json
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
from dotenv import load_dotenv

load_dotenv('.env')


class Consumer:
    def __init__(self):
        try:
            servers = os.getenv('LOG_SERVERS').replace(' ', '').split(',')
            topic_name = os.getenv('LOG_TOPIC_NAME')
            self.consumer = KafkaConsumer(
                topic_name,
                auto_offset_reset='earliest',
                bootstrap_servers=servers,
                value_deserializer=lambda x: json.loads(x.decode('utf-8'))
            )

        except NoBrokersAvailable:
            raise NoBrokersAvailable(
                "No Brokers with given LOG_SERVERS Available."
            )

    def receive_msg(self):
        for message in self.consumer:
            print(message.value)


if __name__ == "__main__":
    consumer = Consumer()
    print("PROCES HAS STARTED - WAITING FOR MESSAGES")
    consumer.receive_msg()
