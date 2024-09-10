from flask import Flask, redirect
from scrape import scrape
from datetime import datetime
import os

app = Flask(__name__)

structure_coordinates = { 
        "Nutwood Structure" : [33.87900170185511, -117.88865432488892],
        "State College Structure" : [33.88189, -117.88927],
        "Eastside North" : [33.88213842742955, -117.88163836042212],
        "Eastside South" : [33.88053842742955, -117.88163836042212],
        "Lot A & G" : [33.8873, -117.88846],
        "Fullerton Free Church" : [33.900814131707214, -117.9094761801681]
}

def indexPage():
    # Fetch the latest parking info every time the page is loaded
    parkingInfo = scrape()

    structureHTML = "<div class='lot-container'>\n"
    for location, data in parkingInfo.items():
        availability = data['availability']
        last_update = data['last_update']    
        latitude = structure_coordinates[location][0]
        longitude = structure_coordinates[location][1]
        
        structureHTML += f"""
        <div class="lot-info" style="display: flex; justify-content: space-between;">
            <h2 style="margin: 0;">{location}
            <p style="font-size:25px; color:red"> <span style="color:white">Updated: </span>{last_update}</p>
            <a href="https://www.google.com/maps?saddr=My+Location&daddr={latitude},{longitude}" style="font-size: 20px; color: cyan;">Directions</a></h2>
            <p style="margin: 0;">{availability} spaces</p>
        </div>
        <br>
        """
    structureHTML += "</div>\n"

    return f"""
    <body>
        <meta http-equiv="refresh" content="60">
        <h1 style="font-size: 100px;">Tuff-Parking</h1>
        <div class="container">
            <div class="info-box">
                {structureHTML}
                <div class="last-update"> Updated: {parkingInfo['Nutwood Structure']['time']} </div>
            </div>
            <div id="map"></div>
        </div>
    </body>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" integrity="sha256-p4NxAoJBhIIN+hmNHrzRCf9tD/miZyoHS5obTRR9BMY=" crossorigin="" />
        <link rel="stylesheet" href="./static/index.css" />
        <link rel="stylesheet" href="https://use.typekit.net/szi4gim.css">
        <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js" integrity="sha256-20nQCchB9co0qIjJZRGuk2/Z9VM+kNiyxNV1lvTlZBo=" crossorigin=""></script>
        <script src="static/index.js"></script>
    """

@app.route("/")
def main():
    return indexPage()

@app.route("/scrape")
def scrapeRoute():
    print("scrape is running")
    return scrape()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host='0.0.0.0', port=port, debug=True)
