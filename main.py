import os
import requests
from dotenv import load_dotenv
from InquirerPy import inquirer
import webbrowser

load_dotenv()

API_KEY = os.getenv('api_key')

if not API_KEY:
    raise ValueError("API key not found. Please set it in the .env file.")

def search_google(query, start=0):
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "start": start,
        "api_key": API_KEY,
        "num": 10
    }
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        
        results = []
        for result in data.get("organic_results", []):
            title = result.get("title", "No title")
            link = result.get("link")
            results.append((title, link))
        
        return results
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return []

def main():
    while True:
        query = inquirer.text(message="Enter your search query: ").execute()
        if not query:
            print("Empty query. Exiting.")
            break
        
        start = 0
        while True:
            results = search_google(query, start)
            
            if not results:
                print("No results found or an error occurred.")
                break
            
            choices = [(f"{title} - {link}", link) for title, link in results]
            choices.append(("Next Page", "next"))
            choices.append(("New Search", "new_search"))
            choices.append(("Quit", "quit"))

            selected_text, selected_value = inquirer.select(message="Select an option:", choices=choices).execute()
            
            if selected_value == "quit":
                return
            elif selected_value == "new_search":
                break
            elif selected_value == "next":
                start += 10
            else:
                webbrowser.open(selected_value)

if __name__ == "__main__":
    main()
