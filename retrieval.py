import pickle
import numpy as np

def load_embeddings(embed_file="data/faq_embeddings.pkl"):
    with open(embed_file, "rb") as f:
        data = pickle.load(f)
    return data["index"], data["df"], data["model"]

def retrieve_answer(query, threshold=0.75):
    index, df, model = load_embeddings()
    q_emb = model.encode([query])
    D, I = index.search(np.array(q_emb), k=1)
    similarity = 1 - D[0][0]/2  # approximate cosine similarity
    if similarity >= threshold:
        return df.iloc[I[0][0]]['Answer']
    return None  # fallback to LLM
