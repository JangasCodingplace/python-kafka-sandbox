# Apache Kafka Python Producer Consumer Sandbox

This is a Containerized Sandbox for Using Apache Kafka in a Python configuration.

It's a single node cluster with an automatic created topic named `fun`. It's running on `port 9092`.

**Note** This Docker Setup is using basic configuration by [Wurstmeister](https://github.com/wurstmeister/kafka-docker)

## Usage
1. Start the cluster `docker-compose up -d`
2. Start `consumer.py` file
3. Start `producer.py` file in a seperate Terminal
4. Have fun

## Note
You can even use the Kafka Shell by typing `docker exec -it <CONTAINER_ID> bash`. navigate into `./opt/kafka` for using shell commands like

**Creating a Cluster**
```
./bin/kafka-topics.sh --create --topic <TOPIC_NAME> --bootstrap-server `broker-list.sh`
```

**Starting a Producer**
```
./bin/kafka-console-producer.sh --topic=<TOPIC_NAME> --broker-list=`broker-list.sh`
```

**Starting a Consumer**
```
./bin/kafka-console-consumer.sh --topic=<TOPIC_NAME> --from-beginning --bootstrap-server `broker-list.sh`
```

**List all Brokers**
```
./bin/kafka-topics.sh --list --bootstrap-server `broker-list.sh`
```
