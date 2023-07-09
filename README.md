# Recomendacion-de-peliculas
Proyecto Individual Nº1 - Sistema de Recomendación de Películas
¡Bienvenido a mi proyecto individual Nº1! En este proyecto, asumo el rol de un MLOps Engineer y trabajaré en el desarrollo e implementación de un sistema de recomendación de películas. Estoy emocionado de mostrarte el trabajo que he realizado hasta ahora.

Contexto del problema
En este proyecto, me uní a una start-up que ofrece servicios de agregación de plataformas de streaming. La empresa necesita un sistema de recomendación de películas para mejorar la experiencia de sus usuarios. Sin embargo, me enfrenté a desafíos como datos sin procesar y sin estructurar, falta de automatización en la actualización de nuevos datos y otros problemas comunes en proyectos de este tipo.

Rol y objetivo
Mi rol principal en este proyecto es el de un Data Engineer. Mi objetivo es limpiar y preparar los datos existentes, desarrollar una API para acceder a los datos de la empresa y crear un sistema de recomendación de películas basado en la similitud de puntuación entre películas.

Desarrollo del proyecto
Transformaciones de datos
Realicé varias transformaciones de datos para limpiar y preparar el conjunto de datos:

Desanidé los campos anidados como belongs_to_collection, production_companies y otros.
Rellené los valores nulos de los campos revenue y budget con 0.
Eliminé las filas con valores nulos en el campo release_date.
Formateé las fechas en el formato AAAA-mm-dd y creé la columna release_year.
Creé la columna return para calcular el retorno de inversión como revenue / budget.
Eliminé las columnas no utilizadas.
Desarrollo de la API
Implementé una API utilizando el framework FastAPI para permitir el acceso a los datos de la empresa. La API cuenta con las siguientes funciones de endpoint:

peliculas_idioma(Idioma: str): Devuelve la cantidad de películas producidas en el idioma especificado.
peliculas_duracion(Pelicula: str): Devuelve la duración y el año de una película especificada.
franquicia(Franquicia: str): Devuelve la cantidad de películas, la ganancia total y la ganancia promedio de una franquicia especificada.
peliculas_pais(Pais: str): Devuelve la cantidad de películas producidas en el país especificado.
productoras_exitosas(Productora: str): Devuelve el revenue total y la cantidad de películas de una productora especificada.
get_director(nombre_director: str): Devuelve el éxito de un director especificado, incluyendo el nombre, fecha de lanzamiento, retorno, costo y ganancia de cada película en formato de lista.
Análisis exploratorio de los datos (EDA)
Realicé un análisis exploratorio de los datos para investigar las relaciones entre las variables, detectar outliers y patrones interesantes. Utilicé herramientas como gráficos y nubes de palabras para obtener información relevante.

Sistema de recomendación
Implementé un sistema de recomendación de películas basado en la similitud de puntuación entre películas. El sistema devuelve una lista de las 5 películas más similares a una película dada, ordenadas por score de similaridad.

Resultados y próximos pasos
Hasta ahora, he logrado limpiar los datos, desarrollar una API funcional y crear un sistema de recomendación de películas. Los resultados son prometedores y el sistema de recomendación puede proporcionar a los usuarios sugerencias relevantes para su experiencia de streaming.

Mis próximos pasos incluyen mejorar la eficiencia y escalabilidad de la API, realizar un análisis más detallado de los datos y explorar diferentes técnicas de recomendación para mejorar la precisión del sistema.
