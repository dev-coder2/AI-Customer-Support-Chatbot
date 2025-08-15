import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

def create_embeddings(faq_csv="data/faq.csv", embed_file="data/faq_embeddings.pkl"):
    df = pd.read_csv(faq_csv)
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(df['Question'].tolist())
    
    # FAISS index
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    
    # Save embeddings and index
    with open(embed_file, "wb") as f:
        pickle.dump({"index": index, "df": df, "model": model}, f)
    print("Embeddings and index saved.")
