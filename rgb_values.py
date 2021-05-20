#!/usr/bin/env python3

# Created by: Jenoe Balote
# Created on: May 2021
# This program shows all RGB values


def main():

    loop1 = 0
    loop2 = 0
    loop3 = 0

    # process & output
    for loop1 in range(255):
        for loop2 in range(255):
            for loop3 in range(255):
                print("RGB ({0},{1},{2})".format(loop1, loop2, loop3))


if __name__ == "__main__":
    main()
