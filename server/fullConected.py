import numpy as np
import scipy as sc

#Creacion de las funciones de activacion
sigmoide= (lambda x: 1 / (1 + np.power(np.e, (-x))), lambda x: np.array(x) * np.array(1-x))
relu = lambda x: np.maximum(0,x)

#Funcion de coste tipo error cuadratico medio
fCoste = (lambda Yp, Yr: np.mean(np.power((Yp-Yr),2)), lambda Yp, Yr: (Yp-Yr))


#Creacion de la topologia o distribucion de la red
distribucion = [ 2 ,8,10 , 1]
neuralNet =[]
#Creacion de una clase que da el comportamiento de una capa de neuronas
class capaNeuronal():
  def __init__(self, nConexiones, nNeurona, fActivacion):
    self.fActivacion=fActivacion
    self.b = (np.random.rand(1,nNeurona) * 2)-1
    self.w = (np.random.rand(nConexiones,nNeurona) * 2)-1

def creacionRed (distribucion, fActivacion ):
  redNeuronal =[]
  for i,capa in enumerate(distribucion[:-1]):
    capaNeural=capaNeuronal(distribucion[i], distribucion[i+1],fActivacion)
    redNeuronal.append(capaNeural)
  return redNeuronal

#Funcion de predicciones de la red
def predecir (redNeuronal,X,Y,fCoste):

  resultados = [(None, X)]
  #Analisis de datos(forward pass)
  for i, capa in enumerate(redNeuronal):
    z= resultados[-1][1] @ redNeuronal[i].w + redNeuronal[i].b
    a= redNeuronal[i].fActivacion[0](z)
    resultados.append((z,a))
  coste = fCoste[0](resultados[-1][1],Y)
  prediccion= (coste,resultados)
  return prediccion

#Funcion de entrenamiento de la red 
def entrenar(redNeuronal,X,Y,fCoste,nivelAprendizaje):
  prediccion = predecir(redNeuronal,X,Y,fCoste)
  #Creaciomn de seguimiento de error(Backward pass y back propagation)
  deltas= []
  for i in reversed(range(1,len(redNeuronal)+1)):
    z = prediccion[1][i][0]
    a = prediccion[1][i][1]
    if i == (len(redNeuronal)):
      #Calculo ultima capa
      deltas.insert(0,np.array(fCoste[1](a,Y))*np.array(redNeuronal[i-1].fActivacion[1](a)) )  
    else: 
      #Calculo capas restantes     
      deltas.insert(0,np.array(deltas[0] @ W.T) *np.array(redNeuronal[i-1].fActivacion[1](a)) )

    #Guardo la  w sin optimizar
    W= redNeuronal[i-1].w

    #Optimizacion por desenso del graciente( Gradient desend) 
    redNeuronal[i-1].b = redNeuronal[i-1].b - (np.mean(deltas[0], axis=0, keepdims=True) * nivelAprendizaje)
    redNeuronal[i-1].w = redNeuronal[i-1].w - ((prediccion[1][i-1][1].T @ deltas[0] ) * nivelAprendizaje)

neuralNet=creacionRed(distribucion,sigmoide)

def create(topology=distribucion, fActivation=sigmoide):
    global neuralNet
    neuralNet = creacionRed(topology, fActivation)

def graph(X, Y):
    X = np.asmatrix(X)
    Y = np.asmatrix(Y)
    error = []
    resolucion = 50
    for i in range(400):
        entrenar(neuralNet, X, Y, fCoste, 0.009)
        
    prediction =predecir(neuralNet, X, Y, fCoste)[0]
    error.append(prediction)
    xcero = np.linspace(-1.5, 1.5, resolucion)
    xuno = np.linspace(-1.5, 1.5, resolucion)
    y = np.zeros((resolucion, resolucion))
    for icero, xceros in enumerate(xcero):
        for iuno, xunos in enumerate(xuno):
            y[icero, iuno] = predecir(neuralNet, np.array([[xceros, xunos]]), Y, fCoste)[1][-1][1][0][0]
    return y.tolist()
