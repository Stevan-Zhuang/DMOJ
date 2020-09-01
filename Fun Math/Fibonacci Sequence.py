def fib_fast_double(n, result=[0, 1]):
    
    for bit in "{:b}".format(n):
        fib_n = result[0]

        fib_n_plus_1 = result[1]

        fib_2n = 2 * fib_n_plus_1 - fib_n
        if fib_2n < 0: fib_2n += mod
        fib_2n = (fib_n * fib_2n) % mod

        fib_2n_plus_1 = (fib_n ** 2 + fib_n_plus_1 ** 2) % mod

        if bit == '0': result = [fib_2n, fib_2n_plus_1]
        if bit == '1': result = [fib_2n_plus_1, fib_2n + fib_2n_plus_1]

    return result[0]

mod = 1000000007
print(fib_fast_double(int(input())))
