from model_loader import load_models
from recommender import smart_recommend

# Load models
knn, tfidf, tfidf_matrix, df = load_models()

while True:
    
    movie_name = input("\nEnter movie name (or type 'exit'): ")
    
    if movie_name.lower() == "exit":
        print("Goodbye 👋")
        break
    
    smart_recommend(movie_name,knn, tfidf, tfidf_matrix, df)
