# SimilariPy

Methods for measuring the similarity of different types of information/data.

- Normal Compression Distance: Compare large chunks of unstructured data
- Jaccard Distance: Compare non-numeric sets of data 
- Jaccard Coefficient: Compare numeric arrays
- Cosine Similarity: Compare numeric arrays

# Examples
```
# Array similarity
from similaripy import jaccard_coefficient, cosine_similarity

v1 = [0, 1, 5, 10, 3, 2, 1]
v2 = [0, 2, 5, 12, 1, 1, 0]

r_jac = jaccard_coefficient(v1, v2)   # 0 = different, 1 = the same
r_cos = cosine_similarity(v1, v2)     # 0 = different, 1 = the same
```

```
# File similarity
from similaripy import ncd

file_1 = "war-and-peace.txt"
file_2 = "lyrics-fresh-prince-of-bel-air.txt"

r = ncd(f1, f2) # 0 = similar, 1 = different
```

