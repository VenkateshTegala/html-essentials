numbers = [
    704, 1, 167, 9, 136, 344, 287, 35, 229, 442, 3289, 104, 1748, 771, 713, 709,
    2959, 2540, 1684, 3005, 2161, 2149, 1572, 1470, 2011, 1929, 2143, 2133, 189, 
    58, 2390, 1047, 2351, 1475, 3340, 2469, 1108, 1528, 1877, 2418, 2413, 2150,
    345, 2944, 2610, 3105, 2798, 2652, 43
]

def search(num):
    if num in numbers:
        print("Number exists")
    else:
        print("Number not there")

def get_length():
    return len(numbers)

def add_number(num):
    numbers.append(num)

search()
print(get_length())
