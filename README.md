# forest_fire_moisture


Este novo modelo foi feito com base no modelo exemplo "Forest Fire Model", em que uma árvore vai queimar se pelo menos um vizinho estiver queimando, ele é usado para ilustrar o papel do mosaico de combustível no regime de incêndios florestais.

## Apresentação do novo modelo, em sua relação ao modelo original

Neste novo modelo é adicionado uma variável chamada "rain", quando a quantidade de chuva é suficiente as árvores que estavam queimando são salvas e elas voltam a cor verde.

## Descrição da hipótese causal que deseja comprovar

Quero comprovar que ocorre a diminuição de áreas queimadas quando a quantidade de chuva é alta e o aumento do tempo para a queima total da área caso a quantidade de chuva não for muito alta.

## Justificativa para as mudanças feitas, em relação ao código original

Para que o resultado fique mais dinâmico foi colocado uma função random em que os valores variam de -0.40 a 0.25, mostrando que a variável não apresenta sempre o mesmo valor durante a execução do programa (fazendo uma simulção da realidade uma vez que a chuva não cai na mesma quantidade ao longo do tempo).

A variável "save" guarda qual árvore foi salva, valor 1 para as salvas e valor 0 para as que não foram salvas (estas também podem não ter sido queimadas por causa da distância delas em relação às outras).

O parâmetro/variável de controle "rain" varia de 0 a 1, quando ela possui um valor maior que 0.6 a área que está queimando é salva, note que apenas os pontos "On Fire" podem ser salvos.
 
As variáveis "density" e "rain" são guardadas para que sejam usadas na nomeação dos arquivos .csv.

Foi adicionado as funções em Phyton que criam arquivos .csv e colocam os valores necessários neles. 

## Orientação sobre como usar o simulador

Executar o comando $ mesa runserver forest_fire_out

## Descrição das variáveis armazenadas no arquivo CSV

Nos arquivos .csv quando "rain = 0" podemos ver que a área é quase totalmente ou totalmente queimada, dependendo da variável densidade (quanto menor a densidade menos árvores queimadas).

Com a variável "rain" cada vez mais próximo do valor 0.6, mais áreas verdes aparecem e mais há mais árvores salvas.

Por fim, com a variável "rain" acima de 0.6, as áreas queimadas são baixas e a quantidade de árvores salvas também é baixa, uma vez que é difícil o fogo espalhar com o valor de "rain" alto.

## Summary original model

The [forest fire model](http://en.wikipedia.org/wiki/Forest-fire_model) is a simple, cellular automaton simulation of a fire spreading through a forest. The forest is a grid of cells, each of which can either be empty or contain a tree. Trees can be unburned, on fire, or burned. The fire spreads from every on-fire tree to unburned neighbors; the on-fire tree then becomes burned. This continues until the fire dies out.

## How to Run

To run the model interactively, run ``mesa runserver`` in this directory. e.g.

```
    $ mesa runserver
```

Then open your browser to [http://127.0.0.1:8521/](http://127.0.0.1:8521/) and press Reset, then Run.

To view and run the model analyses, use the ``Forest Fire Model`` Notebook.

## Files

### ``forest_fire/model.py``

This defines the model. There is one agent class, **TreeCell**. Each TreeCell object which has (x, y) coordinates on the grid, and its condition is *Fine* by default. Every step, if the tree's condition is *On Fire*, it spreads the fire to any *Fine* trees in its [Von Neumann neighborhood](http://en.wikipedia.org/wiki/Von_Neumann_neighborhood) before changing its own condition to *Burned Out*.

The **ForestFire** class is the model container. It is instantiated with width and height parameters which define the grid size, and density, which is the probability of any given cell having a tree in it. When a new model is instantiated, cells are randomly filled with trees with probability equal to density. All the trees in the left-hand column (x=0) are set to *On Fire*.

Each step of the model, trees are activated in random order, spreading the fire and burning out. This continues until there are no more trees on fire -- the fire has completely burned out.


### ``forest_fire/server.py``

This code defines and launches the in-browser visualization for the ForestFire model. It includes the **forest_fire_draw** method, which takes a TreeCell object as an argument and turns it into a portrayal to be drawn in the browser. Each tree is drawn as a rectangle filling the entire cell, with a color based on its condition. *Fine* trees are green, *On Fire* trees red, and *Burned Out* trees are black.

## Further Reading

Read about the Forest Fire model on Wikipedia: http://en.wikipedia.org/wiki/Forest-fire_model

This is directly based on the comparable NetLogo model:

Wilensky, U. (1997). NetLogo Fire model. http://ccl.northwestern.edu/netlogo/models/Fire. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.
