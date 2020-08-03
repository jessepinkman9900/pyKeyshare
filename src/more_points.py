from random import sample

import pandas as pd

from .secret import interpolate
from .generate import gen_x
from .generate import gen_points


def more_points(point_file):
    # read points
    point_file_df = pd.read_csv(point_file)

    # unpacking
    prime = int(point_file_df.iloc[0][1])
    k = len(point_file_df.index)-1
    n = 2*k-1
    points = point_file_df.iloc[1:]

    # getting secret
    f_x = interpolate(points, prime)

    # generate x points
    points_x = gen_x(n, prime)

    # generate y points
    points = gen_points(f_x, points_x, prime)

    # generated points
    out_data = [['- K POINTS -', ], ['PRIME', prime]] + sample(points, k)

    # save points
    file_name = 'EXTRA_POINTS'
    pd.DataFrame(out_data).to_csv(file_name, index=False, header=None)

    return file_name
