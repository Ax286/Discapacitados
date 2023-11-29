from keras.models import Model
from keras.layers import Input, Dense
import requests
import numpy as np

peticion=requests.get('http://127.0.0.1:8000/Data/')

if(peticion.status_code==200):
    data=peticion.json()
    ver,oir,caminar,recordar,banarse,hablar=[],[],[],[],[],[]
    for x in range(0,len(data['Discapacitados']['Tipo']['Hombres'])):
        ver.append(data['Discapacitados']['Tipo']['Hombres'][x]['Ver'])
        oir.append(data['Discapacitados']['Tipo']['Hombres'][x]['Oir'])
        caminar.append(data['Discapacitados']['Tipo']['Hombres'][x]['Caminar'])
        recordar.append(data['Discapacitados']['Tipo']['Hombres'][x]['Recordar'])
        banarse.append(data['Discapacitados']['Tipo']['Hombres'][x]['Banarse'])
        hablar.append(data['Discapacitados']['Tipo']['Hombres'][x]['Hablar'])
    ver= np.array([ver],dtype=float)
    oir= np.array([oir],dtype=float)
    caminar= np.array([caminar],dtype=float)
    recordar= np.array([recordar],dtype=float)
    banarse= np.array([banarse],dtype=float)
    hablar= np.array([hablar],dtype=float)

"""
X=[]

#Datos discapacitados (general)
if(peticion.status_code==200):
    data=peticion.json()
    for x in range(0,len(data['Discapacitados']['General'])):
        X.append(data['Discapacitados']['General'][x]['HombresD'])
X=np.array([X],dtype=float)



D=[]
HD=[]
MD=[]
P=[]

#Datos discapacitados (general)
if(peticion.status_code==200):
    data=peticion.json()
    for x in range(0,len(data['Discapacitados']['General'])):
        D.append(data['Discapacitados']['General'][x]['Discapacitados'])
        HD.append(data['Discapacitados']['General'][x]['HombresD'])
        MD.append(data['Discapacitados']['General'][x]['MujeresD'])

"""
P=[]
#Generacion de arreglo para el modelo MDiscapacitados
if(peticion.status_code==200):
    data=peticion.json()
    for x in range(0,len(data['Poblacion'])):
        P.append(data['Poblacion'][x]['Poblacion'])
P=np.array([P],dtype=float)
"""
D=np.array([D],dtype=float)
HD=np.array([HD],dtype=float)
MD=np.array([MD],dtype=float)
P=np.array([P],dtype=float)
"""

# Número de variables de entrada y salida
num_input_features = 1
num_output_features = 6  # Por ejemplo, 3 variables de salida

# Definir la capa de entrada
input_layer = Input(shape=(num_input_features,))

# Agregar capas ocultas o de procesamiento
hidden_layer = Dense(units=64, activation='relu')(input_layer)
# Puedes agregar más capas ocultas según la complejidad del problema

# Definir las capas de salida
ol1 = Dense(units=1, name='output1')(hidden_layer)
ol2 = Dense(units=1, name='output2')(hidden_layer)
ol3 = Dense(units=1, name='output3')(hidden_layer)
ol4 = Dense(units=1, name='output4')(hidden_layer)
ol5 = Dense(units=1, name='output5')(hidden_layer)
ol6 = Dense(units=1, name='output6')(hidden_layer)

# Crear el modelo especificando las capas de entrada y salida
model = Model(inputs=input_layer, outputs=[ol1, ol2, ol3,ol4,ol5,ol6])

# Compilar el modelo
model.compile(optimizer='adam', loss='mean_squared_error')

model.fit(P.T,[ver.T,oir.T,caminar.T,recordar.T,banarse.T,hablar.T],epochs=1000)

tipos=model.predict([126014024])
tipos=np.array([tipos],dtype=int)

print('Discapacitados ',tipos)

"""
print(P.shape)
print(oir.shape)
print(ver.shape)
print(caminar.shape)
print(recordar.shape)
print(banarse.shape)
"""