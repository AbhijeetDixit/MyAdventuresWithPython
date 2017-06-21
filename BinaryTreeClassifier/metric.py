from __future__ import division
from get_info import *

__author__ = 'root'

version_id = set_version_id()


def return_gini(data_list, num_attrib, iterated_attribs, sequence_of_option, index_for_gini):
    """
    Returns the gini index of the specified attribute
    :param data_list: List of all the data
    :param num_attrib: Total number of attributes
    :param iterated_attribs: Number of attributes on which split has been performed
    :param sequence_of_option: sequence of values required to be considered a part of current node
    :param index_for_gini: index on which gini index is to be calculated
    :return:
    """
    # Some error handling
    if len(iterated_attribs) != len(sequence_of_option):
        if version_id == 2:
            print "invalid sequence of options"
        else:
            print("invalid sequence of options")
        return -100

    # Actual code starts here
    # Find number of output classes
    output_class_list = get_possible_values(data_list, num_attrib)
    output_class_count = len(output_class_list)
    if log_level < CONST_LOG_LEVEL_NO_INFO:
        if version_id == 2:
            print "Output classes are : ", output_class_list
            print "Output class count : ", output_class_count
        else:
            print("Output classes are : ", output_class_list)
            print("Output class count : ", output_class_count)

    overall_gini = 0
    member_count = 0
    num_rows = len(data_list)
    for i in xrange(0, num_rows):
        row = data_list[i]
        row = row.split(',')
        # if log_level < CONST_LOG_LEVEL_NO_DEBUG:
            # if version_id == 2:
                # print "row after split = ", row
            # else:
                # print("row after split = ", row)
        flag = True
        iterated_count = len(iterated_attribs)
        for j in xrange(0, iterated_count, 1):
            idx = iterated_attribs[j]
            print "idx = ", idx
            if row[idx] != sequence_of_option[j]:
                flag = False
                break
        if flag:
            member_count += 1
    if log_level < CONST_LOG_LEVEL_NO_INFO:
        if version_id == 2:
            print "number of members in the given node : ", member_count
        else:
            print("number of members in the given node : ", member_count)

    # We now have the count of items belonging to this particular node.
    # We now find the number of possible values of the split index

    value_list = get_possible_values(data_list, index_for_gini)
    # Find gini for each possible value
    values_count = len(value_list)
    gini_values = []
    for i in xrange(0, values_count, 1):
        gini_values.append(0)
    if log_level < CONST_LOG_LEVEL_NO_INFO:
        if version_id == 2:
            print "gini_values(initialized) is : ", gini_values
        else:
            print("gini_values(initialized) is : ", gini_values)
    occurences = []
    for var in xrange(0, values_count, 1):
        occurences.append(0)
    for i in xrange(0, values_count, 1):
        num_classes = []
        for var in xrange(0, output_class_count, 1):
            num_classes.append(0)
        if log_level < CONST_LOG_LEVEL_NO_INFO:
            if version_id == 2:
                print "num_classes(initialized) is : ", num_classes
            else:
                print("num_classes(initialized) is : ", num_classes)
        for j in xrange(0, num_rows, 1):
            row = data_list[j]
            row = row.split(',')
            if row[index_for_gini] == value_list[i]:
                occurences[i] += 1
                # TODO : Remove this print statement
                # print "row = ", row
                for k in xrange(0, output_class_count, 1):
                    # print "k = ", k
                    # print "output class = ", output_class_list[k]
                    # print "class for this row = ", row[num_attrib]
                    if row[num_attrib].rstrip() == output_class_list[k]:
                        num_classes[k] += 1
                        # print "num_classes[", k, "] = ", num_classes[k]
        if log_level < CONST_LOG_LEVEL_NO_INFO:
            if version_id == 2:
                print "num_values = ", occurences[i]
                print "num_classes = ", num_classes
            else:
                print("num_values = ", occurences[i])
                print("num_classes = ", num_classes)
        gini_values[i] = 1
        for j in xrange(0, output_class_count, 1):
            gini_values[i] -= (num_classes[j] / occurences[i]) * (num_classes[j] / occurences[i])
            if log_level < CONST_LOG_LEVEL_NO_DEBUG:
                if version_id == 2:
                    print "at j = ", j
                    print "gini_value[i] is : ", gini_values[i]
                else:
                    print("at j = ", j)
                    print("gini_value[i] is : ", gini_values[i])
    for i in xrange(0, values_count, 1):
        overall_gini += (occurences[i]/num_rows)*gini_values[i]
        if log_level < CONST_LOG_LEVEL_NO_DEBUG:
            if version_id == 2:
                print "value of i ", i
                print "overall_gini ", overall_gini
            else:
                print("value of i ", i)
                print("overall_gini ", overall_gini)
    return overall_gini