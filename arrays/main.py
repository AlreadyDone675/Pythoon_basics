hash_table = [None] * 11

def ascii_hash(key):
    total = 0
    for char in key:
        total += ord(char)
    return total %11

def insert(key):
    index = ascii_hash(key)
    hash_table[index] = key

def search(key):
    index = ascii_hash(key)

    if hash_table[index] is None:
        return "Not Found"

    if hash_table[index] == key:
        return f"{key} found at index {index}"

    else:
        return "Not Found"

insert("example")
insert("test")
insert("hello")
insert("world")
insert("python")
insert("hash")
insert("table")
insert("data")
insert("structure")
insert("algorithm")
insert("function")

print(hash_table)

print(search("hello"))
print(search("programming"))
print(search("data"))
