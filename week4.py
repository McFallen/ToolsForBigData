import os
import pickle
from scipy.sparse import csr_matrix
from scipy.spatial.distance import jaccard, pdist, squareform
import time

def scan(filename, epsilon, min_size):
    pkl_file = open(filename, 'rb')
    data = pickle.load(pkl_file)

    dataset = [{
        "data": x,
        "visited": False,
        "in_cluster": False,
        "is_noise": False
    } for x in squareform(pdist(csr_matrix(data).todense(), 'jaccard'))]

    clusters = []

    for datapoint in dataset:
        if datapoint['visited']:
            continue
        datapoint['visited'] = True
        neighbour_points = region_query(dataset, datapoint, epsilon)

        if len(neighbour_points) < min_size:
            datapoint['is_noise'] = True
        else:
            cluster = expand_cluster(dataset, datapoint, neighbour_points, epsilon, min_size)
            clusters.append(cluster)

    noise_cluster = {'datapoints': [], 'is_noise': True}

    for datapoint in dataset:
        if datapoint['is_noise']:
            noise_cluster['datapoints'].append(datapoint)

    clusters.append(noise_cluster)

    return clusters

def expand_cluster(dataset, datapoint, neighbour_points, epsilon, min_size):
    """
    Expands cluster with epsilon-neighbouring datapoints not belonging to an existing cluster
    :param datapoint:
    :param neighbour_points:
    :param cluster:
    """
    cluster = {'datapoints': [datapoint], 'is_noise': False}
    datapoint['in_cluster'] = True

    for new_datapoint in neighbour_points:

        if not new_datapoint['visited']:
            new_datapoint['visited'] = True
            new_neighbour_points = region_query(dataset, new_datapoint, epsilon)

            if len(new_neighbour_points) >= min_size:
                neighbour_points += new_neighbour_points

        if not new_datapoint['in_cluster']:
            cluster['datapoints'].append(new_datapoint)
            new_datapoint['is_noise'] = False
            new_datapoint['in_cluster'] = True

    return cluster


def region_query(dataset, datapoint, epsilon):
    """
    Returns a list of new datapoints in datapoint's epsilon-neigbourhood
    :param datapoint:
    :return:
    """
    neighbours = []

    for i, distance in enumerate(datapoint['data']):
        if distance <= epsilon:
            neighbours.append(dataset[i])

    return neighbours

if "__main__" == __name__:
    start_time = time.time()
#    print len(scan(os.path.dirname(__file__) + "/input/data_10points_10dims.dat", 0.4, 2))
 #   print len(scan(os.path.dirname(__file__) + "/input/data_100points_100dims.dat", 0.3, 2))
 #   print len(scan(os.path.dirname(__file__) + "/input/data_1000points_1000dims.dat", 0.15, 2))
    print len(scan(os.path.dirname(__file__) + "/input/data_10000points_10000dims.dat", 0.15, 2))
    print("--- %s seconds ---" % (time.time() - start_time))