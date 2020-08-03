from sympy import Mod
from sympy import mod_inverse
from sympy.abc import x

import pandas as pd


# Lagrange Basis Func in Finite Field
def lbf(k, points_x, i, prime):
    numerator, denominator = 1, 1

    for j in range(k):
        if i == j:
            continue
            # replace 0 with x, for symbolic LBF
        numerator *= (x - int(points_x[j]))
        denominator *= (int(points_x[i]) - int(points_x[j]))

    multiplicative_inverse = mod_inverse(denominator, prime)
    return numerator * multiplicative_inverse


def interpolate(points, prime):
    # unpack
    points_x, points_y = list(points[points.columns[0]]), list(points[points.columns[1]])

    # sum of Lagrange Basis Func in Finite Field
    k = len(points.index)
    poly = 0
    for i in range(0, k):
        poly += int(points_y[i])*lbf(k, points_x, i, prime)

    return Mod(poly, prime)


def secret(point_file):
    # read points
    point_file_df = pd.read_csv(point_file)

    # unpacking
    prime = int(point_file_df.iloc[0][1])
    # k = len(point_file_df.index)-1
    points = point_file_df.iloc[1:]

    # getting secret
    f_0 = interpolate(points, prime).subs({x: 0})
    out_data = ['- SECRET -', f_0]

    # save secret
    file_name = 'SECRET'
    pd.DataFrame(out_data).to_csv(file_name, index=False, header=None)

    return file_name
