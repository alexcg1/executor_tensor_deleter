from jina import Document, DocumentArray, Flow
from executor import TensorDeleter
import numpy as np


docs = DocumentArray(
    [
        Document(tensor=np.zeros([3, 3])),
        Document(tensor=np.zeros([3, 3])),
    ]
)

flow = Flow().add(uses=TensorDeleter)

with flow:
    response = flow.index(docs)

for doc in response:
    print(doc.tensor)
