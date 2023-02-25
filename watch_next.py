import spacy

# Loads the spaCy model with medium language model
nlp = spacy.load('en_core_web_md')


# Creates function that will return which movie a user should watch next based on a particular description of a
# movie. Function takes in description as parameter and returns title of most similar movie
def recommend_movie(description):
    # establishes empty dictionary
    movies = {}
    file = open("movies.txt", "r")
    for line in file:
        # splits key and value at the ':' and then writes to dictionary as key (movie name), item (movie description)
        f = line.split(":")
        movies.update({f[0].strip(): f[1].strip()})
    file.close()

    # sets max_similarity as -1, for each item in dictionary similarity will be compared to this and then similarity
    # updated
    max_similarity = -1
    recommended_movie = ''
    # iterate through movies in dictionary
    for title, movie_desc in movies.items():
        # calculates the similarity between the given description (parameter for function) and each movie description
        # which is the item in dictionary
        similarity = nlp(description).similarity(nlp(movie_desc))
        # loops through to find the max similarity (every time similarity is higher than the previous 'max_similarity'
        # the value will update, so the final value will be the highest
        if similarity > max_similarity:
            max_similarity = similarity
            recommended_movie = title
    return recommended_movie


# Calls the function using parameter description
description = "Will he save the world or destroy it? When the Hulk becomes too dangerous for the Earth, the " \
              "illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in " \
              "peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a " \
              "gladiator."
recommended_movie = recommend_movie(description)
print("You should watch", recommended_movie)
