from abc import ABC, abstractmethod

class Agent(ABC):
    def __init__(self, agent_id, cash=100000, inventory=0):
        self.agent_id = agent_id
        self.cash = cash
        self.inventory = inventory

    @abstractmethod
    def get_action(self, snapshot):
        pass
