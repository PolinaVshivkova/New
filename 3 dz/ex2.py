print(sum(map(lambda x: x ** 2, filter(lambda x: x % 9 == 0,(x for x in range(10,100))))))