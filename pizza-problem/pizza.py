import numpy as np


def import_data(file):
    line_one = file.readline().split(' ')
    max_desired = int(line_one[0].strip())
    types = int(line_one[1].strip())

    slice_types = file.readline().split(' ')

    return max_desired, types, slice_types


def main():
    file_name = 'pizza.txt'
    file_object = open(file_name, 'r+')

    max_slices, pizza_types, slice_types = import_data(file_object)

    file_object.close()
    return


main()
