# Tuffparking🐘
A better and more intuitive website and interface for Cal State Fullerton's parking structures. This is created with a flask backend and vanilla JavaScript, CSS, and HTML as the front end. Planning on making a react front end.
# Clone the repository
`git clone https://github.com/tylermlui/tuffparking.git`
# Run App
`python server.py`
# API
You can access scraping data from Cal State Fullerton's website in JSON format 

## Local Development: <br> 
If you're running the Flask application locally, you can access the data by navigating to http://localhost:3000/scrape in your web browser.

## Live Deployment: <br>
You can access the API through the live deployment URL: https://tuffparking.up.railway.app/scrape

## Example of JSON Data Format: <br>
Once you visit the /scrape route, you’ll get a JSON response. Here’s an example of what the data should look like:

```json
{
  "Eastside North": {
    "availability": 787,
    "fade_percentage": 1,
    "last_update": "9/9/2024 11:51:00 AM",
    "time": "10:33:31",
    "total_spaces": 1880
  },
  "Eastside South": {
    "availability": 467,
    "fade_percentage": 1,
    "last_update": "9/9/2024 11:51:00 AM",
    "time": "10:33:31",
    "total_spaces": 1341
  },
  "Fullerton Free Church": {
    "availability": null,
    "fade_percentage": 0,
    "last_update": "08/26/2024 - 12/12/2024",
    "time": "10:33:31",
    "total_spaces": 700
  },
  "Lot A & G": {
    "availability": 457,
    "fade_percentage": 1,
    "last_update": "9/9/2024 11:51:00 AM",
    "time": "10:33:31",
    "total_spaces": 2104
  },
  "Nutwood Structure": {
    "availability": 2441,
    "fade_percentage": 1,
    "last_update": "9/10/2024 3:33:00 AM",
    "time": "10:33:31",
    "total_spaces": 2484
  },
  "State College Structure": {
    "availability": 1156,
    "fade_percentage": 1,
    "last_update": "9/10/2024 3:33:00 AM",
    "time": "10:33:31",
    "total_spaces": 1373
  }
} 
