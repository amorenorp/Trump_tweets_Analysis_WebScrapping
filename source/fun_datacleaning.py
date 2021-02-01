import pandas as pd
import datetime
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")



### Limpiar Tump Tweets

def clean_dataframe(archivo):

    data = pd.read_csv(f'input/{archivo}')
    df = pd.DataFrame(data)
    df = df[['date','retweets','favorites','content']]
    df['date'] = pd.to_datetime(df['date'])
    df['year'] = df['date'].dt.year
    df2016 = df[df["year"]>2015]
    df2016["date2"]= pd.to_datetime(df2016['date']).dt.date
    #df2016['Time'] = pd.to_datetime(df2016['date']).dt.time
    df2016.reset_index()
    dfcount = df2016['date2'].value_counts().reset_index(name = "tweet_count")
    dfcount.reset_index()
    dfcount['index'] = pd.to_datetime(dfcount['index'])

    return dfcount
    

## Limpiar CSV Descargado

def descargaclean(archivo_nasdaq):
    
    data = pd.read_csv(f'output/{archivo_nasdaq}')
    df = pd.DataFrame(data)
    df["crecimiento"] = df["Close"]-df["Open"]
    df["%"]= (df["crecimiento"]*100)/df["Close"]
    df = df[["Date","Open","Close","crecimiento","%"]]
    df.to_csv('output/nasdaq_clean.csv', index=False,)

    return ".csv guardado"


### Funcion para despues del Merge , nueva columna
def tweets_count(x):
    if x > 34: 
        return "Más de 35"
    elif x < 6:
        return "Menos de 6"
    else:
        return "Resto"


### 
def unir_tablas(csvnasdaq,csvtrump):
    
    data_nasdaq = pd.read_csv(f'output/{csvnasdaq}')

    df_nasdaq = pd.DataFrame(data_nasdaq)
    df_nasdaq['Date'] = pd.to_datetime(df_nasdaq['Date'])
    dfcount = clean_dataframe(csvtrump)
    
    df_resultado = dfcount.merge(df_nasdaq, left_on="index", right_on="Date")

    ##### Añadir neuva columna con la funcion de tweets_count que está arriba. 

    df_resultado["tweets"] = df_resultado["tweet_count"].apply(tweets_count)
    
    return df_resultado