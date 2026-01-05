import random
from engine.order import Order

class NoiseAgent:
    def __init__(self, agent_id):
        self.agent_id = agent_id

    def get_action(self, timestamp):
        side = random.choice(["BUY", "SELL"])
        quantity = random.randint(1, 10)

        if side == "BUY":
            return Order(self.agent_id, "BUY", None, quantity, timestamp, "MARKET")
        else:
            return Order(self.agent_id, "SELL", None, quantity, timestamp, "MARKET")

