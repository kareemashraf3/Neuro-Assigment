import random

def tanh(x):
    exp_pos = 2.718281828459045 ** x  
    exp_neg = 2.718281828459045 ** (-x)  
    return (exp_pos - exp_neg) / (exp_pos + exp_neg)

input_neurons = 2
hidden_neurons = 2
output_neurons = 2
weights_input_hidden = [[random.uniform(-0.5, 0.5) for _ in range(hidden_neurons)] for _ in range(input_neurons)]
weights_hidden_output = [[random.uniform(-0.5, 0.5) for _ in range(output_neurons)] for _ in range(hidden_neurons)]

b1 = 0.5
b2 = 0.7

inputs = [0.05, 0.1]

hidden_outputs = []
for j in range(hidden_neurons):
    net_h = sum(inputs[i] * weights_input_hidden[i][j] for i in range(input_neurons)) + b1
    hidden_outputs.append(tanh(net_h))


final_outputs = []
for k in range(output_neurons):
    net_o = sum(hidden_outputs[j] * weights_hidden_output[j][k] for j in range(hidden_neurons)) + b2
    final_outputs.append(tanh(net_o))

print("Hidden layer outputs:", hidden_outputs)
print("Output layer outputs:", final_outputs)
