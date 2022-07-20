from mesa import Agent
import random

class TreeCell(Agent):
    """
    A tree cell. 

    Attributes:
        x, y: Grid coordinates
        condition: Can be "Fine", "On Fire", or "Burned Out"
        unique_id: (x,y) tuple.

    unique_id isn't strictly necessary here, but it's good
    practice to give one to each agent anyway.
    """

    def __init__(self, pos, model):
        """
        Create a new tree.
        Args:
            pos: The tree's coordinates on the grid.
            model: standard model reference for agent.
        """
        super().__init__(pos, model)
        self.save = 0
        self.pos = pos
        self.condition = "Fine"
        self.rain = random.uniform(-0.40, 0.25) + model.rain
        

    def step(self):
        """
        If the tree is on fire, spread it to fine trees nearby.
        """
        if self.condition == "On Fire":
            for neighbor in self.model.grid.neighbor_iter(self.pos):
                if neighbor.condition == "Fine":
                    neighbor.condition = "On Fire"
                    if self.rain>0.6 and neighbor.condition == "On Fire":                       
                        for neighbor2 in self.model.grid.neighbor_iter(self.pos):
                            if neighbor2.condition == "On Fire":
                                neighbor2.condition = "Fine"
                                neighbor2.save = 1
                            

            self.condition = "Burned Out"
