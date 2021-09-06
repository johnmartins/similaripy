from typing import Sequence, Union
import numpy as np
import numpy.linalg as linalg


def jaccard_coefficient(v1: Sequence[Union[int, float]], v2: Sequence[Union[int, float]]) -> float:
    """
    Calculates jaccard coefficient based on two equally long lists
    :param v1: A list
    :param v2: Another list
    :return:
    """
    if len(v1) != len(v2):
        raise ValueError('Lists needs to be of equal length')

    if len(v1) == 0:
        raise ValueError('Lists needs to be longer than 1')

    expr_num = 0.0
    expr_den = 0.0

    for i in range(0, len(v1)):
        expr_num = expr_num + min(v1[i], v2[i])
        expr_den = expr_den + max(v1[i], v2[i])

    return float(expr_num / expr_den)


def jaccard_distance(v1: Sequence[str], v2: Sequence[str]) -> float:
    """
    Returns the distance between two sets
    :param v1: List of strings
    :param v2: List of strings to which v1 is compared
    :return:
    """
    s1 = set(v1)
    s2 = set(v2)

    expr_num = s1.intersection(s2)
    expr_den = s1.union(s2)

    res = float(len(expr_num) / len(expr_den))

    return res


def cosine_similarity(v1: Sequence[Union[int, float]], v2: Sequence[Union[int, float]]) -> float:
    """
    Returns the cosine similarity of two numeric lists with the same length
    :param v1: A list
    :param v2: Another list
    :return:
    """
    if len(v1) != len(v2):
        raise ValueError('Lists needs to be of equal length')

    if len(v1) == 0:
        raise ValueError('Lists needs to be longer than 1')

    expr_num = np.dot(np.array(v1), np.transpose(np.array(v2)))
    expr_den = linalg.norm(v1) * linalg.norm(v2)

    return expr_num/expr_den
