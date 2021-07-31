# Aim:
# Write a Python program to get OS name, platform and release information.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import os
import platform

if __name__ == '__main__':
    print("Name of OS : {}".format(os.name))
    print("Release Information : {}".format(platform.release()))
    print("Platform Name : {}".format(platform.system()))
