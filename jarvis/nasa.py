import requests

api_key = "boGYPKjK7cu65gX8WH8ChuvIzc37SmbYt7jBUnOc"

def nasaNews(Date):
    url = "https://api.nasa.gov/planetary/apod?api_key="+str(api_key)

    params={'date':str(Date)}
    r= requests.get(url,params=params)

    Data=r.json()
    title = Data['title']
    date = Data['date']
    explanation = Data['explanation']

    return Data