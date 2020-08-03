from sympy import nextprime
from sympy import Mod
from sympy.abc import x

from secrets import randbelow

from random import sample

import pandas as pd


def polynomial(k, secret, prime):
    pol = 0

    for pow in range(1, k):
        coeff = randbelow(prime)
        pol += coeff*(x**pow)
    pol += secret

    return pol


def gen_x(n, prime):
    points = []

    for _ in range(n):
        points.append(randbelow(prime))

    return points


def gen_points(pol, points_x, prime):
    points = []

    for point_x in points_x:
        point_y = Mod(pol, prime).subs({x: point_x})
        points.append([point_x, point_y])

    return points


def generate(n, k, input_file):
    # type change
    n, k = int(n), int(k)

    # read secret
    # secret = int(open(input_file, 'r').read())
    secret = int(pd.read_csv(input_file).iloc[0])

    # prime
    prime = nextprime(max(secret, n))

    # generate polynomial of deg k-1
    f_x = polynomial(k, secret, prime)

    # generate x points
    points_x = gen_x(n, prime)

    # generate y points
    points = gen_points(f_x, points_x, prime)

    # generated points
    out_data = [['- K POINTS -', ], ['PRIME', prime]] + sample(points, k)

    # save points
    file_name = "K_POINTS"
    pd.DataFrame(out_data).to_csv(file_name, index=False, header=None)

    return file_name
