
import numpy as np
# Simple tokenization for educational porpose.
def tokenize(corpus): return corpus.lower().replace('.','').split()  

# SoftMax function: f(x) = e^x/(sum(e^xi))
def softmax(x):
    exp_x = np.exp(x)
    # exp_x = np.exp(x- np.max(x)) this is numerically stable.
    return exp_x / exp_x.sum(axis=0)
