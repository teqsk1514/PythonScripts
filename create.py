import sys
import os

path = '/home/ravi/Documents/'


def create():
    # print(str(sys.argv))
    print('Creating Directory'+path+str(sys.argv[1]))
    os.makedirs(path + str(sys.argv[1]))
    print('Directory'+path+str(sys.argv[1]+'  Created successfully'))


if __name__ == "__main__":
    create()
