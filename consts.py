"""
Constants for examples
"""
SERVERS = 'localhost:9921,localhost:9922,localhost:9923'

def ack_echo(err, msg):
    if err is not None:
        print("failed delivering msg: '{0}: {1}'"
              .format(msg.value(), err.st()))
    else:
        print("message {0} sent".format(msg.key()))

def __strfmt(str, *args, **kwargs):
    return str.format(*args, **kwargs)

def fmt_end_of_partition(msg):
    return __strfmt("End of partition reached {0}/{1}", msg.topic(), msg.partition())