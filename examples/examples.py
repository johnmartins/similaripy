from data_similarity import ncd
from array_similarity import jaccard_coefficient, jaccard_distance, cosine_similarity


def example_text_file_similarity():
    print('File similarity example..')
    f1 = 'example_assets/file1.txt'
    f2 = 'example_assets/file2.txt'

    r = ncd(f1, f2)

    print('File 1:\t'+f1)
    print('File 2:\t'+f2)
    print('Similarity:\t'+str(r))
    print('Close to 0 is similar, close to 1 is completely different.\n\n')


def example_array_similarity():
    v1 = [0, 1, 5, 10, 3, 2, 1]
    v2 = [0, 2, 5, 12, 1, 1, 0]

    r_jac = jaccard_coefficient(v1, v2)
    r_cos = cosine_similarity(v1, v2)

    print('Array 1: '+str(v1))
    print('Array 2: '+str(v2))
    print('Jaccard coefficient: '+str(r_jac))
    print('Cosine similarity: '+str(r_cos))
    print('1: The same. 0: Radically different.\n\n')


example_text_file_similarity()
example_array_similarity()
