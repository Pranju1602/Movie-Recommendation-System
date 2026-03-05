import pickle

def load_models():
    knn = pickle.load(open('knn_model.pkl', 'rb'))
    tfidf = pickle.load(open('tfidf.pkl', 'rb'))
    tfidf_matrix = pickle.load(open('tfidf_matrix.pkl', 'rb'))
    df = pickle.load(open('movies_df.pkl', 'rb'))
    
    return knn, tfidf, tfidf_matrix, df
