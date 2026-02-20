import faiss
import numpy as np

class FAISSStore:
    def __init__(self, dimension):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)  # Using L2 distance

    def add_embeddings(self, embeddings):
        """Add embeddings to the FAISS index."""
        self.index.add(np.array(embeddings).astype('float32'))

    def search(self, query_embedding, k=5):
        """Search for the top k nearest neighbors for a query embedding."""
        distances, indices = self.index.search(np.array([query_embedding]).astype('float32'), k)
        return distances, indices

    def save_index(self, index_path):
        """Save the FAISS index to a file."""
        faiss.write_index(self.index, index_path)

    def load_index(self, index_path):
        """Load the FAISS index from a file."""
        self.index = faiss.read_index(index_path)