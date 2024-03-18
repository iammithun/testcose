# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 18:24:31 2024

@author: iamrs
"""

import requests
from bs4 import BeautifulSoup

def get_planet_positions():
    url = "https://www.theplanetstoday.com/"
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        planet_positions = {}
        
        # Find the table containing planet positions
        table = soup.find('table', {'class': 'tableplanets'})
        if table:
            rows = table.find_all('tr')
            
            for row in rows[1:]:  # Skip header row
                cols = row.find_all('td')
                if len(cols) >= 3:
                    planet_name = cols[0].text.strip()
                    planet_degree = cols[2].text.strip()
                    planet_positions[planet_name] = planet_degree
        
        return planet_positions
    else:
        print("Failed to fetch website:", response.status_code)

def main():
    planet_positions = get_planet_positions()
    if planet_positions:
        print("Planet Positions:")
        for planet, position in planet_positions.items():
            print(f"{planet}: {position} degrees")

if __name__ == "__main__":
    main()
