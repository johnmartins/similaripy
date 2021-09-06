from typing import Dict, List

from array_similarity import jaccard_coefficient, cosine_similarity


def parameter_similarity(params_x: Dict, params_y: Dict, algorithm: str = 'jaccard'):
    """
    Compares two dictionaries of parameters using some array similarity comparison algorithm
    :param params_x: A dictionary of parameters
    :param params_y: Another dictionary
    :param algorithm:
    :return:
    """
    x_keys = set(params_x.keys())
    y_keys = set(params_y.keys())
    keys_union = x_keys.union(y_keys)

    if len(x_keys) != len(keys_union) or len(y_keys) != len(keys_union):
        raise ValueError('Parameter dicts needs to contain the same parameters')

    x = []
    y = []

    for key in keys_union:
        x.append(params_x[key])
        y.append(params_y[key])

    if algorithm == 'jaccard':
        return jaccard_coefficient(x, y)
    if algorithm == 'cosine':
        return cosine_similarity(x, y)

    raise ValueError('Unknown type')
