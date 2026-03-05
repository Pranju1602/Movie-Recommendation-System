import requests

API_KEY = "bbeb0a3c9bc7221b669fb9f621b9c78d"

def fetch_movie_details(movie_name):
    
    search_url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_name}"
    search_response = requests.get(search_url).json()
    
    if len(search_response['results']) == 0:
        return None
    
    movie_id = search_response['results'][0]['id']
    
    details_url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&append_to_response=credits"
    movie_data = requests.get(details_url).json()
    
    return movie_data
