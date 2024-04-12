from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model, Protocol

#incoming data; from interface agent
class FarmData(Model):
    crop_type: str
    farm_size: int
    soil_type: str
    stage_of_growth: str
    crop_density: int
    soil_moisture: int

#incoming data; from weather-agent
class WeatherData(Model):
    temperature: float
    humidity: float
    rainfall: float

#outgoing data; to weather-agent
class QueryWeather(Model):
    requester_address: str
    lon : float
    lat : float
    unit: str
    prod: str

#outgoing data; to pump-agent
class PumpingInformation(Model):
    quantity: float
    routines: int
    per: str

class Message(Model):
    msg: str

decider_agent = Agent(
    name="Decision Making Agent",
    port=8002,
    seed="decision secret code",
    endpoint=["http://127.0.0.1:8002/submit"],
)

PUMP_ADDRESS = "agent1qvrjy9qqv0q9vs9894mlrsaus9gr8esp88u24eymlplx8kemgy7aj388n62"
WEATHER_ADDRESS = "agent1qtpjw3vfd0hx7a569c02pjnk3emn6vzatva3cgw5u4zhn46344pcszw5s2j"
fund_agent_if_low(decider_agent.wallet.address())

@decider_agent.on_message(model=FarmData)
async def farm_data_handler(ctx: Context, sender: str,fd: FarmData):
    ctx.logger.info(f"Recieved farm data {fd} from {sender}")
    ctx.logger.info("Fetching weather information from 7timer API via weather agent")
    await ctx.send(WEATHER_ADDRESS,QueryWeather(requester_address=sender,lon=1,lat=1,unit="Metric",prod="civil"))

@decider_agent.on_message(model=WeatherData)
async def weather_data_handler(ctx: Context,sender: str,wd: WeatherData):
    ctx.logger.info(f"Received weather data {wd} from {sender}")
    await ctx.send(PUMP_ADDRESS,PumpingInformation(quantity=1,routines=1,per=1))

if __name__ == "__main__":
    decider_agent.run()