import random
from math import sqrt


def gen_pq():
    prime_array = []
    for i in range(10000, 99999):
        for x in range(2, int(sqrt(i)) + 1):
            if i % x == 0:
                break
        else:
            prime_array.append(i)

    while True:
        num1 = random.choice(prime_array)
        num2 = random.choice(prime_array)
        if num1 != num2:
            return num1, num2


def nwd(a, b):
    if b > 0:
        return nwd(b, a % b)
    return a


def gen_e(phi_num):
    while True:
        for i in range(phi_num):
            if i == 1 or i == 0:
                continue
            for x in range(2, int(sqrt(i)) + 1):
                if i % x == 0:
                    break
            else:
                if nwd(phi_num, i) == 1:
                    return i


def cipher_message(message_m, e_num, n_num):
    return pow(message_m, e_num, n_num)


def decipher_message(message_m, d_num, n_num):
    return pow(message_m, d_num, n_num)


if __name__ == '__main__':
    p, q = gen_pq()
    N = p * q
    phi = (p - 1) * (q - 1)
    e = gen_e(phi)
    d = pow(e, -1, phi)

    print("p: " + str(p))
    print("q: " + str(q))
    print("N: " + str(N))
    print("phi: " + str(phi))
    print("e: " + str(e))
    print("d: " + str(d))

    while True:
        print("Type message:")
        message = input()
        if int(message) > N:
            print("Message too large")
            continue
        print("Your message:")
        print(cipher_message(int(message), e, N))
        print("Type message to decipher:")
        message = input()
        print(decipher_message(int(message), d, N))
