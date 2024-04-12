from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model

class FarmData(Model):
    city: str
    crop_type: str
    farm_size: int
    soil_type: str
    stage_of_growth: str
    crop_density: int
    soil_moisture: int


user = Agent(
    name="USER1",
    port=8003,
    seed="user secret code",
    endpoint=["http://127.0.0.1:8003/submit"],
)

fund_agent_if_low(user.wallet.address())

DECIDER_ADDRESS = "agent1qw29fkzs8jesevtd4wc5du7av9l24rf6vjswaz6krk20j449ar302m958ly"

@user.on_event("startup")
async def start(ctx: Context):
    await ctx.send(DECIDER_ADDRESS,FarmData(city="Kolkata",crop_type="sugarcane",farm_size=1000,soil_type="clayey",stage_of_growth="InitialStage",crop_density=10,soil_moisture=0))
    
if __name__ == "__main__":
    user.run()