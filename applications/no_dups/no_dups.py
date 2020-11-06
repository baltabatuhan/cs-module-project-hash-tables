def no_dups(s):
    # Your code here
    if s == "":
        return s

    words = s.split(' ')
    store = {}
    i = 1
    for word in words:
        if store.get(word) is None:
            store[word] = i
            i += 1

    store_items = list(store.items())
    store_items.sort(key=lambda x: x[1])

    s = [""] * len(store_items)

    for i, item in enumerate(store_items):
        s[i] = item[0]

    return ' '.join(s)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
