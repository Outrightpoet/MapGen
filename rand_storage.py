import random

count=0

random_store_1_3 = [random.randint(1,3) for i in range(1000)]
random_store_neg_1_1 = [random.randint(-1,1) for i in range(1000)]
random_store_0_10 = [random.randint(0,10) for i in range(1000)]

def get_random_store_1_3():
    global count
    count += 1
    try:
        return random_store_1_3[count]
    except IndexError:
        count = 0
        return random_store_1_3[count]

def get_random_store_neg_1_1():
    global count
    count += 1
    try:
        return random_store_neg_1_1[count]
    except IndexError:
        count = 0
        return random_store_neg_1_1[count]

def get_random_store_0_10():
    global count
    count += 1
    try:
        return random_store_0_10[count]
    except IndexError:
        count = 0
        return random_store_0_10[count]