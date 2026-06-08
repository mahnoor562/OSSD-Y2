import requests
from bs4 import BeautifulSoup
import csv


def get_cars_data(car):
    url = f'https://www.pakwheels.com/new-cars/pricelist/{car}'
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
    }
    
    response = requests.get(url, headers=headers)

    cars = []

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        tables = soup.find_all('table')

        for table in tables:
            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                if len(cols) >= 2:
                    name = cols[0].get_text(strip=True)
                    price = cols[1].get_text(strip=True)
                    cars.append({'name': name, 'price': price})
    else:
        print("Failed to retrieve the webpage.")

    return cars


def save_to_file(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'price'])
        writer.writeheader()
        writer.writerows(data)


def scrapper():
    car = input("Enter car name: ")
    data = get_cars_data(car)

    if data:
        filename = f"{car}_cars.csv"
        save_to_file(data, filename)
        print(f"Data saved successfully in {filename}")
    else:
        print("No data found.")


# IMPORTANT: prevents auto-run when importing in GUI
if __name__ == "__main__":
    scrapper()