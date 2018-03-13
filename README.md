# vector-field-based-neural-network
This is a repo for re-create the experiment is paper: vector field based neural networks. 
Link: https://arxiv.org/abs/1802.08235

Main steps:
1. create the sin, moons and circle datasets
2. create the vector field layers
3. construct the vector field based network
4. plot vector field 
5. plot transformed space
6. plot space distortion
7. check the result
8. work with iris dataset

cli-cmds:

git clone https://github.com/gitathrun/vector-field-based-neural-network.git
cd vector-field-based-neural-network

data is already in data directory
figures are in figure directory
if you want to generate the data by yourself, try the cmd
make sure you are in python 3.5 envionment
python artificial_data_generate.py

Useful material for figure drawing:
1. vector field: https://matplotlib.org/api/_as_gen/matplotlib.pyplot.quiver.html
	https://matplotlib.org/examples/pylab_examples/quiver_demo.html
	https://scipython.com/blog/visualizing-a-vector-field-with-matplotlib/
2. space distortion: https://stackoverflow.com/questions/47295473/how-to-plot-using-matplotlib-python-colahs-deformed-grid
