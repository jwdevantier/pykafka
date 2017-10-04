from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import consts as c

import random as r

SCHEMAS = {
    'key': avro.load("pk.avsc"),
    'value': avro.load("person.avsc")
}

p = AvroProducer(
    {
        'bootstrap.servers': c.SERVERS,
        'schema.registry.url': 'http://127.0.0.1:8081'
        
    },
    default_key_schema= SCHEMAS['key'],
    default_value_schema=SCHEMAS['value']
)

NAME = [
"Kattie",  
"Carmon",  
"Tawanda",  
"Bobby",  
"Palmira",  
"Frieda",  
"Roseann",  
"Junior",  
"Aurea",  
"Loni",  
"Jarvis",  
"Roxann",  
"Ivette",  
"Deon",  
"Calista",  
"Brett",  
"Conrad",
"Raguel",
"Dakota",
"Venice"
]

SURNAMES = [
    "Lavoie",
    "Corson",
    "Ferrer",
    "Allgeier",
    "Acquino",
    "Nishimura"
]

def get_age():
    age = r.randint(10,45)
    if r.uniform(0,1) >= 0.85:
        return None
    else:
        return age

def make_person():
    return {
        "name": r.choice(NAME), 
        "surname": r.choice(SURNAMES),
        "age": get_age()
    }


try:
    for id in range(1, 100):
        print("Sending message '{0}'...".format(id))
        print(make_person())
        p.produce(
            topic='peoplestream',
            key=id,
            value=make_person(),
            callback=c.ack_echo
        )
        print("...")
        p.poll(0.5)
except KeyboardInterrupt:
    pass

print("flushing...")
p.flush(30)
print("done")