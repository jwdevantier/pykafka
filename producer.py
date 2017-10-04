from confluent_kafka import Producer

p = Producer({
    'bootstrap.servers': 'localhost:9921,localhost:9922,localhost:9923'
})
p.produce('gossip', key='hello', value='world')

def acked(err, msg):
    if err is not None:
        print("failed delivering msg: '{0}: {1}'"
              .format(msg.value(), err.st()))
    else:
        print("message {0} sent".format(msg.key()))

try:
    for val in range(1, 1000):
        p.produce('gossip', 
            key="{0}".format(val), value='myvalue #{0}'.format(val),
                  callback=acked)
        p.poll(0.5)
except KeyboardInterrupt:
    pass

print("flushing...")
p.flush(30)
print("done")
