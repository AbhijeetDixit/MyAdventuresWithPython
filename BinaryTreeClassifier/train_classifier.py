from __future__ import division
__author__ = 'root'

from metric import *

version_id = set_version_id()


def do_split(data_list, iterable_attribs, iterated_attribs, sequence, num_attribs, gini_parent):
    """
    do_split performs the split on appropriate attribute.
    :param data_list: The read data_list from the data set : 2D list[String]
    :param iterable_attribs: attribute indices which are yet to be iterated : list[Integer]
    :param iterated_attribs: attribute indices which have been iterated : list[Integer]
    :param sequence: sequence of values for iterated attribs : list[string]
    :param num_attribs: total number of attributes : Integer
    :param gini_parent: gini of parent for which do split is called : Floating point
    :return: rules_list: list of generated rules : list[String]
    """
    loop_var = 0
    min_gini_attrib = -1
    min_gini = gini_parent
    # Add while loop for calculating the gini
    if log_level <= CONST_LOG_LEVEL_NO_INFO:
        if version_id == 2:
            print "Performing split. Inside do_split"
        else:
            print("Performing split. Inside do_split")
    if log_level <= CONST_LOG_LEVEL_NO_DEBUG:
        if version_id == 2:
            print "iterated attribs = ", iterated_attribs
            print "iterable attribs = ", iterable_attribs
            print "sequence = ", sequence
            print "gini_parent = ", gini_parent
        else:
            print("iterated attribs = ", iterated_attribs)
            print("iterable attribs = ", iterable_attribs)
            print("sequence = ", sequence)
            print("gini_parent = ", gini_parent)
    while loop_var < num_attribs:
        if log_level <= CONST_LOG_LEVEL_NO_DEBUG:
            if version_id == 2:
                print "for loop_var = ", loop_var
            else:
                print("for loop_var = ", loop_var)
        if loop_var in iterable_attribs:
            current_gini = return_gini(data_list, num_attribs, iterated_attribs, sequence, loop_var)
            if log_level <= CONST_LOG_LEVEL_NO_DEBUG:
                if version_id == 2:
                    print "current gini = ", current_gini
                else:
                    print("current gini = ", current_gini)
            if current_gini <= min_gini:
                min_gini = current_gini
                min_gini_attrib = loop_var
            if log_level <= CONST_LOG_LEVEL_NO_DEBUG:
                if version_id == 2:
                    print "min gini = ", min_gini
                    print "min gini attrib = ", min_gini_attrib
                else:
                    print("min gini = ", min_gini)
                    print("min gini attrib = ", min_gini_attrib)
        loop_var += 1
    iterated_attribs.append(min_gini_attrib)
    iterable_attribs.remove(min_gini_attrib)
    if log_level <= CONST_LOG_LEVEL_NO_DEBUG:
        if version_id == 2:
            print "iterable attribs = ", iterable_attribs
            print "iterated attribs = ", iterated_attribs
        else:
            print("iterable attribs = ", iterable_attribs)
            print("iterated attribs = ", iterated_attribs)
    possible_attribs = get_possible_values(data_list, min_gini_attrib)
    if log_level <= CONST_LOG_LEVEL_NO_DEBUG:
        if version_id == 2:
            print "possible attribs = ", possible_attribs
        else:
            print("possible attribs = ", possible_attribs)
    rules_list = []
    for i in xrange(0, len(possible_attribs), 1):
        print "possible_attribs[i] = ", possible_attribs[i]
        print "sequence = ", sequence
        temp_sequence = [value for value in sequence]
        temp_sequence.append(possible_attribs[i])
        if log_level <= CONST_LOG_LEVEL_NO_DEBUG:
            if version_id == 2:
                print "temp sequence = ", temp_sequence
            else:
                print("temp sequence = ", temp_sequence)
        gini_parent = return_gini(data_list, num_attribs, iterated_attribs, temp_sequence, min_gini_attrib)
        if log_level <= CONST_LOG_LEVEL_NO_DEBUG:
            if version_id == 2:
                print "gini parent = ", gini_parent
            else:
                print("gini parent = ", gini_parent)
        rules_list.append(do_split(data_list, iterable_attribs, iterated_attribs, temp_sequence,
                                   num_attribs, gini_parent))
        if log_level <= CONST_LOG_LEVEL_NO_INFO:
            if version_id == 2:
                print "returning from doSplit"
                print "rule_list = ", rules_list
            else:
                print("returning from doSplit")
                print("rule_list = ", rules_list)
    return rules_list


def train_classifier():
    """
    The function is used to train the tree based classifier
    :return: NA
    """
    print "version id in train_classifier : ", version_id
    filename = raw_input("Enter the training filename\n")
    if log_level < CONST_LOG_LEVEL_NO_INFO:
        if version_id == 2:
            print "Filename is: ", filename
        else:
            print("Filename is: ", filename)
    data_list = read_data(filename)		# storing all the data as a list
    if log_level < CONST_LOG_LEVEL_NO_INFO:
        if version_id == 2:
            print "Data read is: ", data_list
        else:
            print("Data read is: ", data_list)
    num_attrib = get_num_attr(data_list)		# Know the number of attributes
    if log_level < CONST_LOG_LEVEL_NO_INFO:
        if version_id == 2:
            print "Number of attributes is: ", num_attrib
        else:
            print("Number of attributes is: ", num_attrib)
    pass
    row_count = len(data_list)
    output_classes_list = get_possible_values(data_list, num_attrib)
    output_classes_count = len(output_classes_list)
    class_occurrences = []
    for i in xrange(0, output_classes_count, 1):
        class_occurrences.append(0)
    for i in xrange(0, row_count, 1):
        row = data_list[i].split(',')
        if log_level < CONST_LOG_LEVEL_NO_DEBUG:
            if version_id == 2:
                print "row after split ", row
            else:
                print("row after split ", row)
        for j in xrange(0, output_classes_count, 1):
            if row[num_attrib].rstrip() == output_classes_list[j].rstrip():
                class_occurrences[j] += 1
    if log_level < CONST_LOG_LEVEL_NO_INFO:
        if version_id == 2:
            print "class_occurrences : ", class_occurrences
        else:
            print("class_occurences : ", class_occurrences)
    gini_parent = 1
    for i in xrange(0, output_classes_count, 1):
        temp = class_occurrences[i]/row_count
        if log_level < CONST_LOG_LEVEL_NO_DEBUG:
            if version_id == 2:
                print "temp = ", temp
            else:
                print("temp = ", temp)
        gini_parent -= temp*temp
        if log_level < CONST_LOG_LEVEL_NO_DEBUG:
            if version_id == 2:
                print "at i = ", i
                print "gini_parent = ", gini_parent
            else:
                print("at i = ", i)
                print("gini_parent = ", gini_parent)
    if log_level < CONST_LOG_LEVEL_NO_INFO:
        if version_id == 2:
            print "gini_parent : ", gini_parent
        else:
            print("gini_parent : ", gini_parent)
    # Calculated gini of parent. Now calling Do_Split to actually perform
    # the splitting of data.
    iterable_attribs = []
    iterated_attribs = []
    sequence = []
    for i in xrange(0, num_attrib, 1):
        iterable_attribs.append(i)
    rules_list = do_split(data_list, iterable_attribs, iterated_attribs, sequence, num_attrib, gini_parent)
    if version_id == 2:
        print "rules list is\n", rules_list
    else:
        print("rules list is\n", rules_list)

train_classifier()