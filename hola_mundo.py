print("Hello world to everyone!")

def search_target(arr, target):
    conj = {}
    for ix, i in enumerate(arr):
        resta = target - i
        if resta in conj:
            return conj[resta], ix
        conj[i] = ix
    return ()

print(search_target([1, 6], 5))