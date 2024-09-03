import os
import requests
from dotenv import load_dotenv
from InquirerPy import inquirer
import webbrowser
import tldextract

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
            # Extract domain name and extension
            domain = tldextract.extract(link).domain
            ext = tldextract.extract(link).suffix
            domain_ext = f"{domain}.{ext}"
            results.append((title, domain_ext, link))
        
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
            
            # Format choices
            choices = [
                f"{title} - {domain_ext}"
                for title, domain_ext, link in results
            ]
            choices.append("Next Page")
            choices.append("New Search")
            choices.append("Quit")

            selected_option = inquirer.select(
                message="Select an option:",
                choices=choices
            ).execute()

            if selected_option == "Quit":
                return
            elif selected_option == "New Search":
                break
            elif selected_option == "Next Page":
                start += 10
            else:
                # Find the selected link based on the title
                for title, domain_ext, link in results:
                    if f"{title} - {domain_ext}" == selected_option:
                        webbrowser.open(link)
                        break

if __name__ == "__main__":
    main()
