import pandas as pd
import numpy as np
from fastapi import FastAPI
import sklearn
from sklearn.metrics.pairwise import cosine_similarity


app= FastAPI()

#Abrir dataset limpio
df_movies= pd.read_csv("Dataset.csv", sep=',', encoding='utf-8')

df_movies.head()


#http://127.0.0.1:8000
@app.get("/")
def index():
    return {'mensaje':'Hola'}

@app.get('/peliculas_idioma')
def peliculas_idioma(idioma: str):
    cantidad = len(df_movies[df_movies['original_language'] == idioma])
    return f"{cantidad} películas fueron producidas en {idioma}"

@app.get('/peliculas_duracion')
def peliculas_duracion(pelicula: str):
    pelicula = df_movies[df_movies['title'] == pelicula]
    if len(pelicula) > 0:
        duracion = pelicula['runtime'].values[0]
        anio = pelicula['release_year'].values[0]
        return f"{pelicula['title'].values[0]}. Duración: {duracion}. Año: {anio}"
    else:
        return f"No se encontró la película '{pelicula}'"
    

@app.get('/franquicia')
def franquicia(franquicia: str):
    peliculas = df_movies[df_movies['belongs_to_collection'] == franquicia]
    cantidad_peliculas = len(peliculas)
    ganancia_total = peliculas['revenue'].sum()
    ganancia_promedio = peliculas['revenue'].mean()
    
    return f"La franquicia '{franquicia}' posee {cantidad_peliculas} película(s), una ganancia total de {ganancia_total} y una ganancia promedio de {ganancia_promedio}"


@app.get('/peliculas_pais')
def peliculas_pais(pais: str):
    peliculas = df_movies[df_movies['production_countries'].apply(lambda x: pais in str(x))]
    cantidad_peliculas = len(peliculas)
    
    return f"Se produjeron {cantidad_peliculas} película(s) en el país '{pais}'"


@app.get('/productoras_exitosas')
def productoras_exitosas(productora: str):
    peliculas = df_movies[df_movies['production_companies'].str.contains(productora, na=False)]
    cantidad_peliculas = len(peliculas)
    revenue_total = peliculas['revenue'].sum()

    return f"La productora '{productora}' ha tenido un revenue de {revenue_total} y ha realizado {cantidad_peliculas} película(s)"



@app.get('/get_director')
def get_director(nombre_director):
    movies_list = []
    total_return = 0
    count = 0

    for _, movie in df_movies.iterrows():
        directors = movie['directors']

        if nombre_director in directors:
            title = movie['title']
            release_date = movie['release _date']
            individual_return = movie['return']
            costo = movie['budget']
            ganancia = movie['revenue']

            movie_details = {
                'title': title,
                'release _date': release_date,
                'individual_return': individual_return,
                'costo': costo,
                'ganancia': ganancia
            }

            total_return += individual_return
            count += 1

            movies_list.append(movie_details)

    exito_director = total_return / count if count > 0 else 0
    movies_list.insert(0, {'exito_director': exito_director})

    return movies_list


@app.get("/recomendacion/{titulo}")
def recomendacion(titulo: str):
    pelicula_referencia = df_movies[df_movies['title'] == titulo]
    
    if pelicula_referencia.empty:
        return "No se encontró la película de referencia."
    
    # Obtener la puntuación de la película de referencia
    puntuacion_referencia = pelicula_referencia['vote_average'].iloc[0]

    # Eliminar filas con valores faltantes en la columna de puntuación
    df_cleaned = df_movies.dropna(subset=['vote_average'])

    # Calcular la similitud de puntuación entre la película de referencia y el resto de películas
    df_cleaned['similarity'] = df_cleaned['vote_average'].apply(lambda x: cosine_similarity([[puntuacion_referencia]], [[x]])[0][0])

    # Ordenar las películas por score de similaridad en orden descendente
    peliculas_similares = df_cleaned.sort_values('similarity', ascending=False)

    # Excluir la película de referencia de las recomendaciones
    peliculas_similares = peliculas_similares[peliculas_similares['title'] != titulo]

    # Obtener los 5 nombres de las películas con mayor puntaje de similaridad
    peliculas_recomendadas = peliculas_similares.head(5)['title'].tolist()

    return peliculas_recomendadas

