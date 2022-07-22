from mesa import Model
from mesa.datacollection import DataCollector
from datetime import datetime
from mesa.time import RandomActivation
from mesa.space import Grid
from .agent import TreeCell


class ForestFire(Model):
    """
    Simple Forest Fire model.
    """

    def __init__(self, width=100, height=100, density=0.65, Umidade=0.3, TipoVegetacao=0.5):
        """
        Create a new forest fire model.

        Args:
            width, height: The size of the grid to model
            density: What fraction of grid cells have a tree in them.
        """
        # Set up model objects
        self.schedule = RandomActivation(self)
        self.grid = Grid(width, height, torus=False)
        self.Umidade = Umidade
        self.density = density
        self.TipoVegetacao = TipoVegetacao

        #Variável independente:Umidade e TipoVegetacao
        #Variável dependente:Fine, On Fire, Saved, Burned Out
        self.datacollector = DataCollector(
            model_reporters={
                "Fine": lambda m: self.count_type(m, "Fine"),
                "On Fire": lambda m: self.count_type(m, "On Fire"),
                "Saved": lambda m: self.count_type(m, "Saved"),
                "Burned Out": lambda m: self.count_type(m, "Burned Out"),
                "Umidade":  lambda m: Umidade,
                "TipoVegetacao": lambda m: TipoVegetacao,
                "Saved index": lambda m: self.percentage(m)
            },
            
            agent_reporters={
                "Recuperate": lambda x: x.save
            },
        )
        

        # Place a tree in each cell with Prob = density
        for (contents, x, y) in self.grid.coord_iter():
            if self.random.random() < density:
                # Create a tree
                
                new_tree = TreeCell((x, y), self)
                
                
                # Set all trees in the first column on fire.
                if x == 0:
                    new_tree.condition = "On Fire"
                    new_tree.save=0
                self.grid._place_agent((x, y), new_tree)
                self.schedule.add(new_tree)

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        """
        Advance the model by one step.
        """
        self.schedule.step()
        # collect data
        self.datacollector.collect(self)

        # Halt if no more fire
        if self.count_type(self, "On Fire") == 0:
            self.running = False
             
	#imprimir csv 
    """
            time = str(datetime.now().date())
            model = self.datacollector.get_model_vars_dataframe()
            agent = self.datacollector.get_agent_vars_dataframe()
            name = ("dens=" + str(self.density) + "Umidade=" + str(self.Umidade) + time)
            model.to_csv("data/model_data_steps_" + name + ".csv")
            agent.to_csv("data/agent_data_steps_" + name + ".csv")
      """  
    @staticmethod
    def count_type(model, tree_condition):
        """
        Helper method to count trees in a given condition in a given model.
        """
        count = 0
        for tree in model.schedule.agents:
            if tree.condition == tree_condition:
                count += 1
        return count

    def percentage(self, model):
            total = self.count_type(self, "Burned Out") + self.count_type(self, "Saved")
            saved = self.count_type(self, "Saved")
            if total > 0:
                percentage = saved / total
                return percentage
            if total ==0:
                return 0
