import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# nltk.download('stopwords')
# nltk.download('wordnet')
# nltk.download('omw-1.4') 

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    words = text.split()
    words = [word for word in words if word not in stop_words]
    words = [lemmatizer.lemmatize(word) for word in words]
    return " ".join(words)

def create_tags_from_api(movie_data):
    
    genres = " ".join([g['name'] for g in movie_data['genres']])
    overview = movie_data.get('overview', '')
    tagline = movie_data.get('tagline', '')
    cast = " ".join([c['name'] for c in movie_data['credits']['cast'][:5]])
    
    crew = ""
    for member in movie_data['credits']['crew']:
        if member['job'] == "Director":
            crew += member['name'] + " "

    print("Genre:",genres)
    print("overview:",overview)
    print("tagline:",tagline)
    print("cast:",cast)
    print("Crew:",crew)
    
    raw_tags = f"{genres} {overview} {tagline} {cast} {crew}"
    
    # 🔥 APPLY SAME CLEANING
    cleaned_tags = preprocess_text(raw_tags)
    
    return cleaned_tags

def find_movie_index(df, movie_name):
    
    movie_name = movie_name.lower()
    
    if movie_name in df['title'].str.lower().values:
        return df[df['title'].str.lower() == movie_name].index[0]
    
    return None

