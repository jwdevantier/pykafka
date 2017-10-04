from confluent_kafka import KafkaError
from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError
import consts as c

c = AvroConsumer({
    'bootstrap.servers': c.SERVERS,
    'schema.registry.url': 'http://example.com:9999',
    'group.id': 'person-eater-1',
    'schema.registry.url': 'http://127.0.0.1:8081'
})

c.subscribe(['peoplestream'])

try:
    while True:
        msg = c.poll(0.1)
        if msg is None:
            continue
        elif not msg.error():
            print("received: '{0}'".format(msg.value()))
        elif msg.error().code() != KafkaError._PARTITION_EOF:
            print(c.fmt_end_of_partition(msg))
        else:
            print("Error: '{0}'".format(msg.error().str()))
except KeyboardInterrupt:
    print("Interrupted, ending")
finally:
    c.close()