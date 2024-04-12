from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model

class Message(Model):
    message: str

weather_agent = Agent(
    name="Weather Data Agent",
    port=9000,
    seed="weather secret code",
    endpoint=["http://127.0.0.1:9000/submit"],
)

RECIPIENT_ADDRESS = "agent1qvrjy9qqv0q9vs9894mlrsaus9gr8esp88u24eymlplx8kemgy7aj388n62"
fund_agent_if_low(weather_agent.wallet.address())

@weather_agent.on_event("startup")
async def send_message(ctx: Context):
    await ctx.send(RECIPIENT_ADDRESS, Message(message="hello there weather bot"))

@weather_agent.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    message = input()
    await ctx.send(sender, Message(message = message))

if __name__ == "__main__":
    weather_agent.run()