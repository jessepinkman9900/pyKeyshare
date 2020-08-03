import sys

from src.generate import generate
from src.secret import secret
from src.more_points import more_points

if __name__ == '__main__':
    # -g N K inp_file [generate points with secret]
    # -s point_file [get secret]
    # -m point_file [generate more points with points]

    flag = sys.argv[1]
    if flag == '-g':
        # generate from secret
        N, K = sys.argv[2], sys.argv[3]
        inputFile = sys.argv[4]
        file_name = generate(N, K, inputFile)
        print('K-POINT FILE SAVED AS: {}'.format(file_name))
    elif flag == '-s':
        # get secret
        point_file = sys.argv[2]
        file_name = secret(point_file)
        print('SECRET SAVED IN: {}'.format(file_name))
    elif flag == '-m':
        # more points from points
        point_file = sys.argv[2]
        file_name = more_points(point_file)
        print('K EXTRA POINTS SAVED IN: {}'.format(file_name))
