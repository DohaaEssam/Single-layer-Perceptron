# Single-layer-Perceptron
Task2 
Single layer perceptron using Adaptive Linear Neuron algorithm (Adaline) on penguins' data

## Task Overview
- The Adaline deviates from Perceptron because there is no cost function in Perceptron and without a cost function Perceptron is minimizing nothing. 
- The cost function in the Adaline Algorithm is mean square error.
- To minimize cost function, gradient descent is needed.
- The gradient decent should work with differentiable function (has derivative) as the weight update is on the slope’s opposite direction
- Use the penguins data in both your training and testing processes. (Each class has 50 samples: train NN with 30 non-repeated samples randomly selected, and test it with the remaining 20 samples)

## Dataset (Penguins)
- The data set consists of 50 samples from each of three species of Penguins (Adelie, Gentoo and Chinstrap).  
- Five features were measured from each sample: bill_length, bill_depth, flipper_length, gender and body_mass, (in millimeter).
