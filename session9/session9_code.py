import pickle

data = {1: "1", "a": "b"}
path = 'mydata.pcl'

# pickle.load()  # deserialization is its inverse operation (convert string -> object).
# pickle.loads(str_repr)

# pickle.dump()  # convert an object into string
# pickle.dumps(data)


with open(path, 'wb') as f:
    str_repr = pickle.dumps(data)
    print(str_repr)
    pickle.dump(data, file=f)

with open(path, 'rb') as f:
    data1 = pickle.loads(str_repr)
    data2 = pickle.load(f)

print(data1, data2)


