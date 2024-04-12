from uagents.setup import fund_agent_if_low
from uagents import Agent, Context, Model

class Message(Model):
    message: str

pump_agent = Agent(
    name="Pump Controlling Agent",
    port=8000,
    seed="pump secret code",
    endpoint=["http://127.0.0.1:8000/submit"],
)

RECIPIENT_ADDRESS = "agent1qtpjw3vfd0hx7a569c02pjnk3emn6vzatva3cgw5u4zhn46344pcszw5s2j"
fund_agent_if_low(pump_agent.wallet.address())

@pump_agent.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
    message = input()
    await ctx.send(sender, Message(message = message))

if __name__ == "__main__":
    pump_agent.run()

