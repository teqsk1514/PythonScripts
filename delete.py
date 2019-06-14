import sys
import os


path = '/home/ravi/Documents/'


def delete():
    # print(path + sys.argv[1])
    try:
        print('Removing Directory'+path+str(sys.argv[1]))
        os.rmdir(path + str(sys.argv[1]))
        print('Directory'+path+str(sys.argv[1]+'  removed successfully'))
    except:
        print(path+sys.argv[1]+' Dosent exist')


if __name__ == "__main__":
    delete()
