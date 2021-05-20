#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Oct 2019
# This program shows all RGB values


def main():

    loop1 = 0
    loop2 = 0
    loop3 = 0

    # process & output
    for loop_counter1 in range(255):
        for loop_counter2 in range(255):
            for loop_counter3 in range(255):
                print("RGB ({0},{1},{2})".format(loop1, loop2, loop3))


if __name__ == "__main__":
    main()
