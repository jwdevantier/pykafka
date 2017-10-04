import avro.schema
from avro.datafile import DataFileReader, DataFileWriter
from avro.io import DatumReader, DatumWriter

DATFILE="users.avro"

schema = avro.schema.Parse(open("user.avsc", mode="r").read())

writer = DataFileWriter(open(DATFILE, mode="wb"), DatumWriter(), schema)

writer.append({"name": "Alyssa", "favorite_number": 256})
writer.append({"name": "Ben", "favorite_number": 7, "favorite_color": "red"})
writer.close()

reader = DataFileReader(open(DATFILE, mode="rb"), DatumReader())
for user in reader:
    print(user)
reader.close()
