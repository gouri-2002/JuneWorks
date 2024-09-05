

movies = [
    {
        "title": "Drishyam",
        "year": 2013,
        "language": "Malayalam",
        "genres": ["Crime", "Drama", "Thriller"],
        "rating": 8.6
    },
    {
        "title": "Premam",
        "year": 2015,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    {
        "title": "Bangalore Days",
        "year": 2014,
        "language": "Malayalam",
        "genres": ["Comedy", "Drama", "Romance"],
        "rating": 8.3
    },
    # Tamil Movies
    {
        "title": "Kaala",
        "year": 2018,
        "language": "Tamil",
        "genres": ["Action", "Drama"],
        "rating": 7.3
    },
    {
        "title": "Vikram Vedha",
        "year": 2017,
        "language": "Tamil",
        "genres": ["Action", "Crime", "Thriller"],
        "rating": 8.4
    },
    {
        "title": "Super Deluxe",
        "year": 2019,
        "language": "Tamil",
        "genres": ["Drama", "Mystery", "Thriller"],
        "rating": 8.3
    },
    # Hindi Movies
    {
        "title": "Dangal",
        "year": 2016,
        "language": "Hindi",
        "genres": ["Action", "Biography", "Drama"],
        "rating": 8.4
    },
    {
        "title": "3 Idiots",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Comedy", "Drama"],
        "rating": 8.4
    },
    {
        "title": "Gully Boy",
        "year": 2019,
        "language": "Hindi",
        "genres": ["Drama", "Music"],
        "rating": 8.0
    }
]


# q1 total_number of movies

movies_count=len(movies)
print("movie count =",movies_count)

# q2 movies with genre Drama

genre_fliter=[m.get("title") for m in movies if "Drama" in m.get("genres")]
print(genre_fliter)


# q3 latest movie

def get_year(mov):
    return mov.get("year")

latest_movie_data=max(movies,key=get_year)
latest_movie=[m.get("title") for m in movies if m.get("year")==latest_movie_data.get("year")]
print(latest_movie)


# q4 top movie(moive with highest rating)

def get_rating(mov):
    return mov.get("rating")
top_rating_data=max(movies,key=get_rating)
top_rating_movies=[m.get("title") for m in movies if m.get("rating")==top_rating_data.get("rating")]
print(top_rating_movies)


# q5 moive with lanuage malayalm

malaylm_movies=[m.get("title") for m in movies if m.get("language")=="Malayalam"]
print(malaylm_movies)

# q6 moivies released after year 2016

year_fliter=[m.get("title") for m in movies if m.get("year")>2016]
print(year_fliter)

# q7 moive with lowest rating

def get_rating(mov):
    return mov.get("rating")
low_rating_data=min(movies,key=get_rating)
low_rating_movies=[m.get("title") for m in movies if m.get("rating")==low_rating_data.get("rating")]
print(low_rating_movies)


# q8 malayalm moives with genre drama

malayalam_action_movies=[m.get("title") for m in movies if "Drama" in m.get("genres") and m.get("language")=="Malayalam"]
print(malayalam_action_movies)

# q9  moives released in same year 

movie_dictionary={}
for m in movies:
    release_year=m.get("year")
    if release_year in movie_dictionary:
        movie_dictionary.get(release_year).append(m.get("title"))
    else:
        movie_dictionary[release_year]=[m.get("title")]

print(movie_dictionary)

# q10 oldest movie

oldest_movie_data=min(movies,key=get_year)
oldest_movie=[m.get("title") for m in movies if m.get("year")==oldest_movie_data.get("year")]
print(oldest_movie)

# q11 moive name with genre either drama or comedy

#number of movies relesed in each year

years=[m.get("year") for m in movies]
print(years)

years_count={ y:years.count(y) for y in years}
print(years_count)

#sort moives

def get_title(m):
    return m.get("title")
sorted_movies=sorted(movies,key=get_title)
print([m.get("title") for m in sorted_movies])





 

