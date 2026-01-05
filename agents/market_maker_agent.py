from engine.order import Order

class MarketMakerAgent:
    def __init__(self, agent_id, spread=1):
        self.agent_id = agent_id
        self.spread = spread

    def get_orders(self, mid_price, timestamp):
        if mid_price is None:
            return []

        bid = Order(self.agent_id, "BUY", mid_price - self.spread, 5, timestamp, "LIMIT")
        ask = Order(self.agent_id, "SELL", mid_price + self.spread, 5, timestamp, "LIMIT")
        return [bid, ask]
