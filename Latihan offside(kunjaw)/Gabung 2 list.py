def factor_tree(number):
    divisor = 2
    outer_while = 1
    inner_while = 1
    prime_factors = []
    if number <= 1:
        prime_factors.append(number)
        return prime_factors
    while (divisor <= number):
        print("Awal iterasi ke:",outer_while,"berisi:",prime_factors)
        if (number % divisor == 0):
            prime_factors.append([divisor, 0]) # menambahkan list berisi divisor dan jumlah pangkatnya kedalam list prime_factors
        while (number % divisor == 0):
            print("Sebelum ditambah: ", prime_factors)
            prime_factors[-1][1] += 1 # menambah angka pangkat sesuai jumlah pembagian dengan divisor tsb.
            print("Setelah ditambah: ", prime_factors)
            number //= divisor
            print("Hasil iterasi ke:",outer_while," dan", inner_while,"berisi:",prime_factors)
            inner_while += 1
        outer_while += 1
        divisor += 1
    return prime_factors

def print_prime_factors(prime_factors):
    for index in range(len(prime_factors)):
        print(str(prime_factors[index][0]), end='')
        if prime_factors[index][1] > 1:
            print('^' + str(prime_factors[index][1]), end='')
        if index != len(prime_factors)-1:
            print(' x ', end='')
    print()

prime_factors = factor_tree(int(input("Masukkan angkanya: ")))
print_prime_factors(prime_factors)
