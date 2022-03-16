from jina import Executor, DocumentArray, requests, Document


def process_doc(doc: Document):
    if hasattr(doc, "tensor"):
        doc.tensor = None

    return doc


class TensorDeleter(Executor):
    @requests
    def remove_tensor(self, docs: DocumentArray, **kwargs):
        docs.apply(process_doc)
