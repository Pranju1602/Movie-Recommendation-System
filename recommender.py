from tmdb_api import fetch_movie_details
from util import create_tags_from_api

def smart_recommend(movie_name, knn, tfidf, tfidf_matrix, df):
    
    movie_name_lower = movie_name.lower()
    
    if movie_name_lower in df['title'].str.lower().values:
        
        print("Movie found in dataset ✅\n")
        
        movie_index = df[df['title'].str.lower() == movie_name_lower].index[0]
        
        distances, indices = knn.kneighbors(
            tfidf_matrix[movie_index],
            n_neighbors=6
        )
        
    else:
        
        print("Movie not in dataset ❌ Fetching from TMDB...\n")
        
        movie_data = fetch_movie_details(movie_name)
        
        if movie_data is None:
            print("Movie not found on TMDB")
            return
        
        tags = create_tags_from_api(movie_data)
        
        new_vector = tfidf.transform([tags])
        
        distances, indices = knn.kneighbors(new_vector, n_neighbors=6)
    
    print("Recommended Movies:\n")
    
    for idx in indices[0]:
        print(df.iloc[idx]['title'])
