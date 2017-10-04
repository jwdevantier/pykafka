from confluent_kafka import Consumer, KafkaError

settings = {
    'bootstrap.servers': 'localhost:9921,localhost:9922,localhost:9923',
    'group.id': 'mygroup',
    'client.id': 'consumer-einz',
    'enable.auto.commit': True,
    'session.timeout.ms': 6000,
    'default.topic.config': {'auto.offset.reset': 'smallest'}
}

c = Consumer(settings)
c.subscribe(['gossip'])
try:
    while True:
        msg = c.poll(0.1)
        if msg is None:
            continue
        elif not msg.error():
            print("received: '{0}'".format(msg.value()))
        elif msg.error().code() == KafkaError._PARTITION_EOF:
            print("End of partition reached {0}/{1}"
                  .format(msg.topic(), msg.partition()))
        else:
            print("Error: {0}".format(msg.error().str()))
except KeyboardInterrupt:
    print("Interrupted, ending")

finally:
    c.close()
