from copy import deepcopy
# Exercise 2.1


def read_matrix(file_name, delimiter = " "):
    """
    Reads in a matrix as string and return it as a list of lists.
    Takes the file name as a parameter.
    :param file_name:
    :return:
    """

    handle = file(file_name, "r")

    matrix = []

    # Loop over each line in the file
    for line in handle:
        entry = []
        # Clean up trailing newlines
        for number in line.strip("\n").split(delimiter):
            entry.append(float(number))
        matrix.append(entry)

    return matrix

#print read_matrix("input/exercise2_1_input.txt")

def write_matrix(input_matrix, file_name):
    """
    Does the inverse as method_1, namely take, as input, a list of lists and save it in a file with same format as the initial file.

    :param input_matrix:
    :param file_name:
    """
    handle = file(file_name, "w")

    output_matrix = []
    for line in input_matrix:
        # Append all the numbers together
        output_matrix.append(' '.join(line))
    # Join all the lines together, separated by newlines and write to file
    handle.write('\n'.join(output_matrix))


#matrix = method2_1_1("input/exercise2_1_input.txt")
#method2_1_2(matrix, "output/exercise2_1_output.txt")


# Exercise 2.2
def bin_lists(n):

    bin_matrices = [[0] * n]

    # Loop n amount of times
    for i in xrange(n):

        # Loop through permutation (this
        for permutation in bin_matrices:
            permutation_iter = deepcopy(permutation)

            for j in xrange(n):
                # Create new permutation by inserting 0 at j's index
                permutation_iter.pop(j)
                permutation_iter.insert(j, 0)

                # Add permutaion if it doesn't exist
                if not bin_matrices.__contains__(permutation_iter):
                    bin_matrices.append(deepcopy(permutation_iter))

                # Create new permutation by inserting 1 at j's index
                permutation_iter.pop(j)
                permutation_iter.insert(j, 1)

                # Add permutaion if it doesn't exist
                if not bin_matrices.__contains__(permutation_iter):
                    bin_matrices.append(deepcopy(permutation_iter))


    return bin_matrices

#print (bin_lists(3))


# Exercise 2.3
import json
import re
"""
def bagg_of_words(file_name):

    bag_of_bags = []
    words_that_exists = {}
    # Loads JSON from filename into variable
    with open(file_name) as json_data:
        data = json.load(json_data)

    # Loop over each data entry
    for entry in data:
        bag_of_words = {}
        # Find and
        words = entry['request_text'].replace("\n", " ").lower().split(" ")
        for word in words:
            if word not in words_that_exists.keys():
                words_that_exists[word] = 0

    print len(words_that_exists)

    the_whole_shebang = []

    for bow in bag_of_bags:
        break
        whole_text_bag = deepcopy(words_that_exists)

        for word in bow:
            whole_text_bag[word] = bow[word]

        the_whole_shebang.append(whole_text_bag)

"""



#bag_of_words("input/pizza-train.json")
#print len(bagg_of_words("input/pizza-train.json"))
#method2_3_1('input/pizza-train.json')