import numpy as np
from pprint import pprint

integers = np.zeros(10, dtype=np.int8)
integers = np.ones(10, dtype=np.int8)
integers = np.arange(10,20,2)
integers = np.linspace(10,20,5)
integers = np.random.rand(4,4,4)
integers = np.random.randint(1,6, 10)
integers = np.empty((4,4), dtype=np.int8)
integers.fill(12)

integers = np.full((4,4), 10)

pprint(integers)
pprint(np.shape(integers))
pprint(np.size(integers))