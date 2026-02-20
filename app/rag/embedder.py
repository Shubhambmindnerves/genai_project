from sentence_transformers import SentenceTransformer

# Load the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to generate embeddings for a list of sentences
def generate_embeddings(sentences):
    return model.encode(sentences)

# Example usage
if __name__ == '__main__':
    sentences = ['This is an example.', 'Sentence transformers are great for embedding generation.']
    embeddings = generate_embeddings(sentences)
    print(embeddings)