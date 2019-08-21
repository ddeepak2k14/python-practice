__author__ = 'deepak.k'
import urllib.request


url = 'http://api.npr.org/query?apiKey='
key = 'API_KEY'
url = url + key
url += '&numResults=3&format=json&id='
url += input("Which NPR ID do you want to query?")

response =urllib.request.urlopen(url)
json_obj = response.read()
print(json_obj)
