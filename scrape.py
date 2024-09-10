import httpx
from datetime import datetime 
from bs4 import BeautifulSoup


def scrape():
    time = datetime.now().strftime('%H:%M:%S')
    html = httpx.get("https://parking.fullerton.edu/parkinglotcounts/mobile.aspx").text
    soup = BeautifulSoup(html,features="lxml")
    table = soup.find("table")
    rows = table.find_all("tr")
    areas = {}

    for i in range(0, len(rows)):
        row = rows[i]
        cols = row.find_all("td")
        structure_info = cols[0].find_all("p")
        structure_availability = cols[1]
        availability_str = structure_availability.find_all('span')[0].text

        if availability_str == "Closed" or availability_str == "Full":
            availability = None 
        elif availability_str == "Open":
            availability = "Open"
        else:
            availability = int(availability_str)

        try:
            name = structure_info[0].find('span').text 
        except AttributeError:
            name = structure_info[0].find("a").text

        total_spaces = int(structure_info[1].find_all('span')[1].text)
        last_update = structure_info[2].find("span").text

        try:
            fade_percentage = 0 if availability == None else max(0,min(1, availability))
        except: 
            availability = "Open"

        areas[name] = {
            "availability": availability
            , "total_spaces": total_spaces
            , "last_update": last_update
            , "fade_percentage": fade_percentage
            , "time": time
        }
    return areas
