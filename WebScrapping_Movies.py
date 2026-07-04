import requests
from bs4 import BeautifulSoup
import pandas as pd

# Wikipedia URL
url = "https://en.wikipedia.org/wiki/List_of_highest-grossing_films"

# It simply identifies the request as coming from a normal browser.
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

table = soup.find("table", class_="wikitable")

rows = table.find_all("tr")

movies = []

for row in rows[1:]:

    cols = row.find_all(["th", "td"])

    if len(cols) >= 5:

        rank = cols[0].get_text(strip=True)

        title = cols[2].get_text(strip=True)

        worldwide_gross = cols[3].get_text(strip=True)

        year = cols[4].get_text(strip=True)

        movies.append([rank, title, worldwide_gross, year])

df = pd.DataFrame(
    movies,
    columns=[
        "Rank",
        "Movie",
        "Worldwide Gross",
        "Year"
    ]
)

print(df.head())

df.to_csv("highest_grossing_movies.csv", index=False)

print("\nTotal Movies:", len(df))
print("\nOldest Movie:")
print(df.sort_values("Year").head(1))

print("\nNewest Movie:")
print(df.sort_values("Year", ascending=False).head(1))

print("\nDataset saved successfully!")
