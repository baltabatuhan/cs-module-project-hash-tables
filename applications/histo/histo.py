# Your code here

def s2ni(s):
    return s.encode()[0] * -1


def histogram():
    with open("robin.txt") as f:
        words = f.read()

    words = words.lower()

    ignored = r'":;,.-+=/\|[]{}()*^&'
    for c in ignored:
        words = words.replace(c, '')

    words = words.split()

    store = {}

    for word in words:
        if word in store:
            store[word] += 1
        else:
            store[word] = 1

    longest_word = 0
    for key, value in store.items():
        if(len(key) > longest_word):
            longest_word = len(key)

        store[key] = value * '#'

    longest_word += 2

    store_items = list(store.items())

    store_items.sort(reverse=True, key=lambda x: (x[1], s2ni(x[0])))

    for key, value in store_items:
        print(key + " " * (longest_word - len(key)), value)


histogram()
