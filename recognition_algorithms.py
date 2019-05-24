from collections import defaultdict
from typing import List, Tuple
from difflib import SequenceMatcher
from utils import parse_csv


def euclidean_distance(x1: str, x2: str) -> int:
    return 1 - SequenceMatcher(None, x1, x2).ratio()


def data_set_division(sample: List[tuple]) -> Tuple[dict, dict]:
    center_index =  int(7 * len(sample) / 10)
    training_data_set = defaultdict(list)
    testing_data_set = defaultdict(list)

    for pswd in sample[:center_index]:
        training_data_set[pswd[1]].append(pswd[0])

    for pswd in sample[center_index:]:
        testing_data_set[pswd[1]].append(pswd[0])

    return training_data_set, testing_data_set


def calc_similarity_vectors(x, data_set):
    similarity_vectors = defaultdict(list)

    for category, passwords in data_set.items():
        similarity_vectors[category].append(
            [euclidean_distance(x, el) for el in passwords]
        )
    return similarity_vectors


def calc_category_similarity(similarity_vectors):
    category_similarity = defaultdict()

    for category, s_vector in similarity_vectors.items():
        category_similarity[category] = min(s_vector)

    return category_similarity


def calc_decision(category_similarity):
    decision = defaultdict()
    max_sim = min(category_similarity.values())

    for category, similarity in category_similarity.items():
        if similarity == max_sim:
            decision[category] = 1
        else:
            decision[category] = 0

    return decision


def algorithm_quality():
    A = []
    sample = parse_csv('samples/smaller_data.csv')

    # Step 0
    training_data_set, testing_data_set = data_set_division(sample)

    #
    # # Step 1
    # similarity_vectors = calc_similarity_vectors(tmp_val, training_data_set)
    #
    # # Step 2
    # category_similarity = calc_category_similarity(similarity_vectors)
    #
    # # Step 3
    # decision = calc_decision(category_similarity)

    # Step 4
    m0 = 0

    loading_total = len(testing_data_set)
    loading_current = 0

    # Step 4.1
    for category, passw_arr in testing_data_set.items():
        for x in passw_arr:
            # a)
            similarity_vectors = calc_similarity_vectors(x, training_data_set)

            # b)
            category_similarity = calc_category_similarity(similarity_vectors)

            # c)
            decision = calc_decision(category_similarity)

            # d)
            if decision == category:
                m0 += 1

        loading_current += 1
        print(loading_current / loading_total)

    # Step 4.2
    quality = m0 / len(testing_data_set)

    return f'Quality: {quality}'
