def calculate(limit):
    result = 0
    for i in xrange(limit):
        if i % 3 == 0 or i % 5 == 0:
            result += i
    print result
calculate(1000)
