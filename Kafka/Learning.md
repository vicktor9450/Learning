# Kafka learning root
https://www.linkedin.com/learning/learn-apache-kafka-for-beginners/kafka-broker-discovery?autoplay=true&u=98593218

## Kafka theory

- Topic, Partitions and Offset
- Broker and topic
- Topic replication
    Leader for a partition
    Replication = 3 is good choice:
        allow 1 down for maintenance
        allow 1 down unexpectedly
        and we have 1 work perfectly

- Producers and Message keys
    Write data to topics (which is made of partitions)
    Key need for messsage kept always fixed in particular partitions ( important )
- Consumers and Consumer group
- Consumer offsets
- Zookeeper
    manage brokers
    helps in performing leader election
    send notifications to kafka incase of changes
    SETUP in odd number of servers( 1-3-5-7)
    has a leader (handle writes), and the rest servers are follower(handle reads)


## Start Kafka
- Install Java
- Start Zookeeper
    - make data/zookeeper
    - Config 
        - zookeeper.properties
            Change dataDir=data/zookeeper #need fullPath
            clientPort=2181 # default port for zookeeper
    - Start
        zookeeper-server-start config/zookeeper.properties
- Start Kafka
    - make data/kafka
    - Config
        - server.properties
            Change log.dirs=/data/kafka #need fullPath
    - Start
        kafka-server-start config/server.properties



