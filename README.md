# TensorDeleter

After creating embeddings you may no longer require a Document's tensor. This Executor simply sets `doc.tensor` to `None`, thus reducing storage space for indexed data.


## Usage

#### via Docker image (recommended)

```python
from jina import Flow
	
f = Flow().add(uses='jinahub+docker://TensorDeleter')
```

#### via source code

```python
from jina import Flow
	
f = Flow().add(uses='jinahub://TensorDeleter')
```

- To override `__init__` args & kwargs, use `.add(..., uses_with: {'key': 'value'})`
- To override class metas, use `.add(..., uses_metas: {'key': 'value})`
