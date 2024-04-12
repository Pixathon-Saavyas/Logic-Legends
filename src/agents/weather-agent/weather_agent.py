from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model
import requests

class Message(Model):
    message: str

class QueryWeather(Model):
    requester_address: str
    lon : float
    lat : float
    unit: str
    prod: str

class WeatherData(Model):
    temperature: float
    humidity: float
    rainfall: float

weather_agent = Agent(
    name="Weather Data Agent",
    port=8001,
    seed="weather secret code",
    endpoint=["http://127.0.0.1:8001/submit"],
)
 
def fetch_json_from_api(url):
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            json_data = response.json()
            return json_data
        else:
            print(f"Error: Unable to fetch data from API. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    
DECIDER_ADDRESS = "agent1qw29fkzs8jesevtd4wc5du7av9l24rf6vjswaz6krk20j449ar302m958ly"
fund_agent_if_low(weather_agent.wallet.address())

@weather_agent.on_message(model=QueryWeather)
async def query_handler(ctx: Context,sender: str,msg: QueryWeather):
    query = f"http://www.7timer.info/bin/api.pl?lon={msg.lon}&lat={msg.lat}&product={msg.prod}&output=json"
    ctx.logger.info(f"Received Weather Request From {sender} details: {query}")
    ctx.logger.info(f"Processing Data......")
    ctx.logger.info(f"Fetching weather information.....")
    # data = fetch_json_from_api(query)
    # ctx.logger.info(f"{data}")
    await ctx.send(sender,WeatherData(temperature=2,humidity=2,rainfall=2))

if __name__ == "__main__":
    weather_agent.run()
