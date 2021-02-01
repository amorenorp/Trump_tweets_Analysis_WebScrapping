#   Trump tweets Analysis WebScrapping project

![img_don](https://github.com/amorenorp/Trump_tweets_Analysis_WebScrapping/blob/main/Img/img_don.jpg)

En este proyecto he utlizado el documento [Trump Tweets](https://www.kaggle.com/austinreese/trump-tweets) descargado de Kaggle.




# Descripción
La idea del projecto es enriquecer una base de datos ya existente añadiendole más informacion utilizando web scrapping. 

En esta caso utilizaré una base de datos de todos los tweets de Donald Trump desde el 2009. 

Tenía entendido que cada vez que el bueno de Donald estaba muy activo en esta red social los mercados financieros se veian repercutidos. 

Me he propuesto ver que tal le fue al Nasdaq durante esos días e intentar sacar una conclusión parecida a esta: 

![img_tweet](https://github.com/amorenorp/Trump_tweets_Analysis_WebScrapping/blob/main/Img/img_tweet.png)


# Proceso

Para ello lo primero ha sido descargar el .csv con los tweets de Trump , realizar una pequeña limpieza quedandonos solo con los datos que necesitamos. 

Para enriquecer esa base de datos necesitaba otro .csv pero en este caso con los datos historicos del Nasdaq.

Para ello utlizando la herramienta `Selenium` pude automatizar el proceso y realizar la descarga. 

A ese nuevo .csv también le realizamos una limpieza y unos ajustes para despues poder unirlo a la base de datos de los tweets a través de un `merge` por la columna `date`.

Una vez unidas ambas bases de datos creamos unos gráficos para que sea más visual. 



## *Referencias y bibliotecas:*

 - https://www.kaggle.com/austinreese/trump-tweets
 - https://seaborn.pydata.org/#
 - https://pandas.pydata.org/
 - https://matplotlib.org/
 - https://selenium-python.readthedocs.io/getting-started.html
 - https://www.youtube.com


