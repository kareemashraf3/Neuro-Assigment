def tanh(x):
    e_pos = 2.718281828459045 ** x  
    e_neg = 2.718281828459045 ** (-x)  
    return (e_pos - e_neg) / (e_pos + e_neg)
                        
w1, w2, w3, w4, w5, w6, w7, w8 = 0.15, 0.2, 0.25, 0.3, 0.4, 0.45, 0.5, 0.55


b1, b2 = 0.5, 0.7


i1, i2 = 0.05, 0.10


net_h1 = (w1 * i1) + (w2 * i2) + (b1 * 1)
net_h2 = (w3 * i1) + (w4 * i2) + (b1 * 1)


out_h1 = tanh(net_h1)
out_h2 = tanh(net_h2)


net_o1 = (w5 * out_h1) + (w6 * out_h2) + (b2 * 1)
net_o2 = (w7 * out_h1) + (w8 * out_h2) + (b2 * 1)


out_o1 = tanh(net_o1)
out_o2 = tanh(net_o2)


print("Output O1:", out_o1)
print("Output O2:", out_o2)
