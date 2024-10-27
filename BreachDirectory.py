import requests
import json
from typing import Dict, Any

class BreachDirectoryFetcher:
    def __init__(self, apiKey: str):
        self.apiKey = apiKey
        self.baseUrl = "https://breachdirectory.p.rapidapi.com/"
        self.headers = {
            "X-RapidAPI-Key": self.apiKey,
            "X-RapidAPI-Host": "breachdirectory.p.rapidapi.com"
        }

    def fetchData(self, term: str) -> Dict[str, Any]:
        querystring = {"func": "auto", "term": term}
        response = requests.get(self.baseUrl, headers=self.headers, params=querystring)
        
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            raise Exception(f"API request failed with status code {response.status_code}")

    def processResults(self, data: Dict[str, Any]) -> None:
        if not data["success"]:
            print("No results found")
            return

        for result in data["result"]:
            print(f"Source: {result['sources']}")
            print(f"Password: {result['password']}")
            print(f"SHA1: {result['sha1']}")
            print(f"Hash: {result['hash']}")
            print("---")

def main():
    apiKey = "api key goes here"
    fetcher = BreachDirectoryFetcher(apiKey)

    while True:
        term = input("Enter email or username to search (or 'q' to quit): ")
        if term.lower() == 'q':
            break

        try:
            data = fetcher.fetchData(term)
            fetcher.processResults(data)
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
