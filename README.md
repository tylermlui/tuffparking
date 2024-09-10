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
{
  "Eastside North": {
    "availability": 169, Current spaces right now
    "fade_percentage": 0.0898936170212766, This is used for the color value for each circle
    "last_update": "9/10/2024 1:05:00 PM", The time it was last updated on CSUF's website
    "time": "20:05:26", The time it was updated from the last refresh
    "total_spaces": 1880
  },
  "Eastside South": {
    "availability": 63,
    "fade_percentage": 0.04697986577181208,
    "last_update": "9/10/2024 1:05:00 PM",
    "time": "20:05:26",
    "total_spaces": 1341
  },
  "Fullerton Free Church": {
    "availability": 544,
    "fade_percentage": 0.7771428571428571,
    "last_update": "08/26/2024 - 12/12/2024",
    "time": "20:05:26",
    "total_spaces": 700
  },
  "Lot A & G": {
    "availability": 709,
    "fade_percentage": 0.3369771863117871,
    "last_update": "9/10/2024 1:05:00 PM",
    "time": "20:05:26",
    "total_spaces": 2104
  },
  "Nutwood Structure": {
    "availability": 111,
    "fade_percentage": 0.04468599033816425,
    "last_update": "9/10/2024 1:05:00 PM",
    "time": "20:05:26",
    "total_spaces": 2484
  },
  "State College Structure": {
    "availability": 53,
    "fade_percentage": 0.03860160233066278,
    "last_update": "9/10/2024 1:05:00 PM",
    "time": "20:05:26",
    "total_spaces": 1373
  }
}
```
**availability:** Current spaces right now <br>
**fade_percentage:** This is used for the color value for each circle <br>
**last_update:** The time it was last updated on CSUF's website <br>
**time:** The time it was updated from the last refresh<br>
**total_spaces:** Total spaces that are in the structure
