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
        self.PartiallyBurned = 0
        self.pos = pos
        self.condition = "Fine"
        self.Umidade = random.uniform(-0.40, 0.25) + model.Umidade
        self.TipoVegetacao = random.uniform(-0.1, 0.5) + model.TipoVegetacao
        

    def step(self):
        """
        If the tree is on fire, spread it to fine trees nearby.
        """
        count=0
        if self.condition == "On Fire":
            for neighbor in self.model.grid.neighbor_iter(self.pos):
                if neighbor.condition == "Fine" or neighbor.condition == "PartiallyBurned":
                    neighbor.condition = "On Fire"
                    ####
                    if self.Umidade>0.6 and neighbor.condition == "On Fire" and self.TipoVegetacao>0.5 or neighbor.condition == "PartiallyBurned":                       
                        for neighbor2 in self.model.grid.neighbor_iter(self.pos):
                            if neighbor2.condition == "On Fire":
                                neighbor2.condition = "Fine"
                                neighbor2.condition = "PartiallyBurned"
                                count=count+1
                                neighbor2.PartiallyBurned = count
                    ####        

            self.condition = "Burned Out"
