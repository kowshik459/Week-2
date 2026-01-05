import random
from engine.order_book import OrderBook
from engine.matching_engine import MatchingEngine
from engine.event_loop import EventLoop
from agents.noise_agent import NoiseAgent
from analytics.tape import TradeTape
from analytics.snapshots import SnapshotRecorder
from analytics.metrics import compute_vwap, compute_average_spread

random.seed(42)

order_book = OrderBook()
engine = MatchingEngine(order_book)
event_loop = EventLoop(engine)

tape = TradeTape()
snapshots = SnapshotRecorder()

agents = [NoiseAgent(i) for i in range(10)]

timestamp = 0

for _ in range(50):
    timestamp += 1
    agent = random.choice(agents)
    order = agent.get_action(timestamp)
    event_loop.schedule_order(timestamp, order)

event_loop.run()

for trade in engine.trades:
    tape.record(trade)

print("VWAP:", compute_vwap(tape.trades))
