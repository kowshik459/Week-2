from collections import deque
from engine.order import Order

class MomentumAgent:
    def __init__(self, agent_id, window=5):
        self.agent_id = agent_id
        self.window = window
        self.prices = deque(maxlen=window)

    def observe(self, price):
        if price is not None:
            self.prices.append(price)

    def get_action(self, timestamp):
        if len(self.prices) < self.window:
            return None

        if self.prices[-1] > sum(self.prices) / len(self.prices):
            return Order(self.agent_id, "BUY", None, 5, timestamp, "MARKET")
        else:
            return Order(self.agent_id, "SELL", None, 5, timestamp, "MARKET")
