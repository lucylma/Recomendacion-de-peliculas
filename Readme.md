<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

¡Bienvenido a mi proyecto individual Nº1! En este proyecto, asumo el rol de un MLOps Engineer y trabajaré en el desarrollo e implementación de un sistema de recomendación de películas. Estoy emocionado de mostrarte el trabajo que he realizado hasta ahora.

<hr>  

## **Contexto del problema**

Se desea desarrollar un proyecto para una empresa que ofrece servicios de agregación de plataformas de streaming. La empresa necesita un sistema de recomendación de películas para mejorar la experiencia de sus usuarios. El proyecto incluye limpiar y preparar los datos existentes, desarrollar una API para acceder a los datos de la empresa y crear un sistema de recomendación de películas basado en la similitud de puntuación entre películas.


## **Desarrollo del proyecto**

## **1.1 Transformaciones de datos**

Se realizaron varias transformaciones de datos para limpiar y preparar el conjunto de datos:<br>
<br>
1) Desanidar los campos anidados como belongs_to_collection, production_companies y otros.<br>
2) Rellenar los valores nulos de los campos revenue y budget con 0.<br>
3) Eliminar las filas con valores nulos en el campo release_date.<br>
4) Formatar las fechas en el formato AAAA-mm-dd y crear la columna release_year.<br>
5) Crear la columna return para calcular el retorno de inversión como revenue / budget.<br>
6) Eliminar las columnas no utilizadas.<br>

## **1.2 Desarrollo de la API**

Implementar una API utilizando el framework FastAPI para permitir el acceso a los datos de la empresa. La API cuenta con las siguientes funciones de endpoint: <br>
<br>
1) **peliculas_idioma(Idioma: str):** Devuelve la cantidad de películas producidas en el idioma especificado.<br>
2) **peliculas_duracion(Pelicula: str):** Devuelve la duración y el año de una película especificada.<br>
3) **franquicia(Franquicia: str):** Devuelve la cantidad de películas, la ganancia total y la ganancia promedio de una franquicia especificada.<br>
4) **peliculas_pais(Pais: str):** Devuelve la cantidad de películas producidas en el país especificado.<br>
5) **productoras_exitosas(Productora: str):** Devuelve el revenue total y la cantidad de películas de una productora especificada.<br>
6) **get_director(nombre_director: str):** Devuelve el éxito de un director especificado, incluyendo el nombre, fecha de lanzamiento, retorno, costo y ganancia de cada película en formato de lista.<br>

## **1.3 Análisis exploratorio de los datos (EDA)**

Realizar un análisis exploratorio de los datos para investigar las relaciones entre las variables, detectar outliers y patrones interesantes. Se utilizaron herramientas como gráficos y nubes de palabras para obtener información relevante.

## **1.4 Sistema de recomendación**

Se implementó un sistema de recomendación de películas basado en la similitud de puntuación entre películas. El sistema devuelve una lista de las 5 películas con mayor similaridad a una película dada, ordenadas por score de similaridad. Para implementar el sistema de recomendación se utilizó la similitud del coseno como medida de distancia

<p align="center">
<img src="https://miro.medium.com/v2/resize:fit:640/format:webp/0*4IVXlcZV8Sm29h79.png"  height=300>
</p>

## **Resultados y próximos pasos**

Hasta ahora, he logrado limpiar los datos, desarrollar una API funcional y crear un sistema de recomendación de películas. Los resultados son prometedores y el sistema de recomendación puede proporcionar a los usuarios sugerencias relevantes para su experiencia de streaming.

Mis próximos pasos incluyen mejorar la eficiencia y escalabilidad de la API, realizar un análisis más detallado de los datos y explorar diferentes técnicas de recomendación para mejorar la precisión del sistema.

