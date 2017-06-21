__author__ = 'root'
from definitions import *

version_id = set_version_id()


def read_data(filename):

    """
    reads the data from a file to list
    :param filename:
    :return data from file as a list:
    """

    in_file = open(filename, 'r')
    lst = in_file.readlines()
    if log_level <= CONST_LOG_LEVEL_NO_DEBUG:
        if version_id == 2:
            print "file data is", lst
        else:
            print("file data is", lst)
    in_file.close()
    return lst


def get_num_attr(data_list):
    """
    Returns the number of attributes by parsing a
    single row of data
    :param data_list:
    :return number of attributes:
    """
    row = data_list[0]
    if log_level <= CONST_LOG_LEVEL_NO_DEBUG:
        if version_id == 2:
            print "data_list[0] is ", data_list[0]
        else:
            print("data_list[0] is", data_list[0])
    row = row.split(',')
    if log_level <= CONST_LOG_LEVEL_NO_DEBUG:
        if version_id == 2:
            print "row after splitting", row
        else:
            print("row after splitting", row)
    num_attrib = len(row) - 1       # This one is for removing the class label attribute
    return num_attrib


def get_possible_values(data_list, attr_index):
    """
    Returns the possible values of data for the
    attribute identified by attr_index in the data_list
    :param data_list:
    :param attr_index:
    :return list containing possible values:
    """
    row_count = len(data_list)
    value_list = []
    if log_level <= CONST_LOG_LEVEL_NO_DEBUG:
        if version_id == 2:
            print "row count is: ", row_count
        else:
            print("row count is: ", row_count)
    for row_num in range(0, row_count, 1):
        current_row = data_list[row_num]
        current_row = current_row.split(',')
        if current_row[attr_index].rstrip() not in value_list:
            value_list.append(current_row[attr_index].rstrip())
            if log_level <= CONST_LOG_LEVEL_NO_DEBUG:
                if version_id == 2:
                    print "attribute added: ", current_row[attr_index]
                else:
                    print("attribute added: ", current_row[attr_index])
    return value_list