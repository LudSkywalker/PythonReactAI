import numpy as np
import scipy as sc


class NeuralLayer():
    def __init__(self, nConnections, nNeuron, fActivation):
        self.fActivation = fActivation
        self.b = (np.random.rand(1, nNeuron) * 2)-1
        self.w = (np.random.rand(nConnections, nNeuron) * 2)-1


def NetCreation(distribution, fActivation):
    neuralNet = []
    for i, layer in enumerate(distribution[:-1]):
        neuralLayer = NeuralLayer(
            distribution[i], distribution[i+1], fActivation)
        neuralNet.append(neuralLayer)
    return neuralNet


def predict(neuralNet, X, Y, fCost):

    results = [(None, X)]
    for i, layer in enumerate(neuralNet):
        z = results[-1][1] @ neuralNet[i].w + neuralNet[i].b
        a = neuralNet[i].fActivation[0](z)
        results.append((z, a))
    coste = fCost[0](results[-1][1], Y)
    prediction = (coste, results)
    return prediction

def train(neuralNet, X, Y, fCost, learningLevel):
    prediction = predict(neuralNet, X, Y, fCost)
    deltas = []
    for i in reversed(range(1, len(neuralNet)+1)):
        z = prediction[1][i][0]
        a = prediction[1][i][1]
        if i == (len(neuralNet)):
            deltas.insert(0, fCost[1](a, Y)*neuralNet[i-1].fActivation[1](a))
        else:
            deltas.insert(0, deltas[0] @ W.T *
                          neuralNet[i-1].fActivation[1](a))

        W = neuralNet[i-1].w

        neuralNet[i-1].b = neuralNet[i-1].b - \
            (np.mean(deltas[0], axis=0, keepdims=True) * learningLevel)
        neuralNet[i-1].w = neuralNet[i-1].w - \
            ((prediction[1][i-1][1].T @ deltas[0]) * learningLevel)


sigmoide = (lambda x: 1 / (1 + np.e ** (-x))), lambda x: x * (1-x)
def relu(x): return np.maximum(0, x)

fCost = (lambda Yp, Yr: np.mean((Yp-Yr)**2), lambda Yp, Yr: (Yp-Yr))
distribution = [2, 8, 10, 1]

def FullyConnect(X, Y):
    neuralNet = NetCreation(distribution, sigmoide)
    error = []
    resolucion = 100
    for i in range(5000):
        train(neuralNet, X, Y, fCost, 0.015)
        if (i % 50) == 0:
            prediction = predict(neuralNet, X, Y, fCost)[0]
            error.append(prediction)
            xcero = np.linspace(-1.5, 1.5, resolucion)
            xuno = np.linspace(-1.5, 1.5, resolucion)
            y = np.zeros((resolucion, resolucion))

            for icero, xceros in enumerate(xcero):
                for iuno, xunos in enumerate(xuno):
                    y[icero, iuno] = predict(neuralNet, np.array(
                        [[xceros, xunos]]), Y, fCost)[1][-1][1][0][0]
