import requests

# URL of the API endpoint
url = "http://www.7timer.info/bin/api.pl?lon=113.17&lat=23.09&product=civillight&output=json"

try:
    # Send a GET request to the API
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()

        # Print the JSON data
        print(data)
    else:
        # Print an error message if the request was not successful
        print("Error:", response.status_code)

except requests.exceptions.RequestException as e:
    # Print an error message if there was a problem with the request
    print("Error:", e)
