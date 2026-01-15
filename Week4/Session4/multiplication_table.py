def multiplication_table(n):
    multiplestable = []

    if not type(n) is int:
        raise TypeError
    elif n < 0:
        raise ValueError

    else:

        for i in range(1,n+1):
            multiples = []
            for num in range(1,n+1):
                multiples.append(num*i)

            multiplestable.append(multiples)
        print(multiplestable)
        return multiplestable



multiplication_table(3)