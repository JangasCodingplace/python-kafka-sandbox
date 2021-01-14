import os
import json
from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
from datetime import datetime
from dotenv import load_dotenv

load_dotenv('.env')


class Producer:
    def __init__(self):
        try:
            servers = os.getenv('LOG_SERVERS').replace(' ', '').split(',')
            self.producer = KafkaProducer(
                bootstrap_servers=servers,
                value_serializer=lambda d: json.dumps(d).encode('utf-8')
            )

        except NoBrokersAvailable:
            raise NoBrokersAvailable(
                "No Brokers with given LOG_SERVERS Available."
            )

    def send_msg(self, msg):
        """
        Send Message to Kafka Cluster

        Attributes:
        ----------
            msg dict:
                Message to send
        """
        assert isinstance(msg, dict), (
            "msg property must be a dictionary."
            "It's type %s." % str(type(msg))
        )
        self.producer.send(os.getenv('LOG_TOPIC_NAME'), value=msg)


if __name__ == "__main__":
    producer = Producer()
    user_input = ""
    while user_input != 'exit':
        user_input = input(" >  ")
        msg = {
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'user_input': user_input
        }
        producer.send_msg(msg)
