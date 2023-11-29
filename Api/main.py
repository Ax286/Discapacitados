import requests
import numpy as np
import keras
from keras import layers
import tensorflowjs as tfjs

D,HD,MD,P=[],[],[],[]

peticion=requests.get('http://127.0.0.1:8000/Data/')

#Datos discapacitados (general)
if(peticion.status_code==200):
    data=peticion.json()
    for x in range(0,len(data['Discapacitados']['General'])):
        D.append(data['Discapacitados']['General'][x]['Discapacitados'])
        HD.append(data['Discapacitados']['General'][x]['HombresD'])
        MD.append(data['Discapacitados']['General'][x]['MujeresD'])

#Generacion de arreglo para el modelo MDiscapacitados
if(peticion.status_code==200):
    data=peticion.json()
    for x in range(0,len(data['Poblacion'])):
        P.append(data['Poblacion'][x]['Poblacion'])

#Metodo para Discapacitados por tipo
def DiscTipo(genero):
    if(peticion.status_code==200):
        data=peticion.json()
        ver,oir,caminar,recordar,banarse,hablar=[],[],[],[],[],[]
        for x in range(0,len(data['Discapacitados']['Tipo'][genero])):
            ver.append(data['Discapacitados']['Tipo'][genero][x]['Ver'])
            oir.append(data['Discapacitados']['Tipo'][genero][x]['Oir'])
            caminar.append(data['Discapacitados']['Tipo'][genero][x]['Caminar'])
            recordar.append(data['Discapacitados']['Tipo'][genero][x]['Recordar'])
            banarse.append(data['Discapacitados']['Tipo'][genero][x]['Banarse'])
            hablar.append(data['Discapacitados']['Tipo'][genero][x]['Hablar'])
    return np.array([ver,oir,caminar,recordar,banarse,hablar],dtype=float)

#Metodo para Discapacitados por edades
def DiscEdades(genero):
    #Generacion de arreglo para el modelo MHombresEdades
    if(peticion.status_code==200):
        data=peticion.json()
        _0a4,_5a9,_10a14,_15a19,_20a24,_25a29,_30a34,_35a39,_40a44,_45a49,_50a54,_55a59,_60a64,_65a69,_70a74,_75a79,_80a84,_85yMas=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
        for x in range(0,len(data['Discapacitados']['Edades'][genero])):
            _0a4.append(data['Discapacitados']['Edades'][genero][x]['_0a4'])
            _5a9.append(data['Discapacitados']['Edades'][genero][x]['_5a9'])
            _10a14.append(data['Discapacitados']['Edades'][genero][x]['_10a14'])
            _15a19.append(data['Discapacitados']['Edades'][genero][x]['_15a19'])
            _20a24.append(data['Discapacitados']['Edades'][genero][x]['_20a24'])
            _25a29.append(data['Discapacitados']['Edades'][genero][x]['_25a29'])
            _30a34.append(data['Discapacitados']['Edades'][genero][x]['_30a34'])
            _35a39.append(data['Discapacitados']['Edades'][genero][x]['_35a39'])
            _40a44.append(data['Discapacitados']['Edades'][genero][x]['_40a44'])
            _45a49.append(data['Discapacitados']['Edades'][genero][x]['_45a49'])
            _50a54.append(data['Discapacitados']['Edades'][genero][x]['_50a54'])
            _55a59.append(data['Discapacitados']['Edades'][genero][x]['_55a59'])
            _60a64.append(data['Discapacitados']['Edades'][genero][x]['_60a64'])
            _65a69.append(data['Discapacitados']['Edades'][genero][x]['_65a69'])
            _70a74.append(data['Discapacitados']['Edades'][genero][x]['_70a74'])
            _75a79.append(data['Discapacitados']['Edades'][genero][x]['_75a79'])
            _80a84.append(data['Discapacitados']['Edades'][genero][x]['_80a84'])
            _85yMas.append(data['Discapacitados']['Edades'][genero][x]['_85yMas'])
        return np.array([_0a4,_5a9,_10a14,_15a19,_20a24,_25a29,_30a34,_35a39,_40a44,_45a49,_50a54,_55a59,_60a64,_65a69,_70a74,_75a79,_80a84,_85yMas],dtype=float)

#Generacion de arreglos
arrDiscapacitados=np.array([P,D,HD,MD],dtype=float)
arrTipoHombres=DiscTipo('Hombres')
arrTipoMujeres=DiscTipo('Mujeres')
arrEdadesHombres=DiscEdades('Hombres')
arrEdadesMujeres=DiscEdades('Mujeres')

#Funcion para la creacion del modelo
def Modelo(input,output,x,y,epocas):
    
    #Creacion de modelo de prediccion para hombres
    modelo = keras.Sequential()
    modelo.add(keras.Input(shape=(input,)))
    modelo.add(layers.Dense(64, activation='relu',name='oculta1'))
    modelo.add(layers.Dense(64, activation='relu',name='oculta2'))
    modelo.add(layers.Dense(32, activation='relu',name='oculta3'))
    modelo.add(layers.Dense(output,name='oculta4'))

    modelo.compile(
        optimizer=keras.optimizers.Adam(learning_rate=0.0001),
        loss=keras.losses.MeanSquaredError()
    )

    #Entrenar modelo
    modelo.fit(x,y, epochs=epocas, verbose=0)

    return modelo

#Entrenar modelo de Discapacitados general
x=arrDiscapacitados[0]
y=arrDiscapacitados.T[:,1:4]
MDiscapacitados=Modelo(1,3,x,y,3500)

#Entrenar modelo de Discapacitados por tipo (Hombres)
x=arrDiscapacitados[2]
y=arrTipoHombres.T
MHombresTipo=Modelo(1,6,x,y,3500)

#Entrenar modelo de Discapacitados por tipo (Mujeres)
x=arrDiscapacitados[3]
y=arrTipoMujeres.T
MMujeresTipo=Modelo(1,6,x,y,3500)

#Entrenar modelo de Discapacitados por edad (Hombres)
x=arrDiscapacitados[2]
y=arrEdadesHombres.T
MHombresEdad=Modelo(1,18,x,y,3500)

#Entrenar modelo de Discapacitados por edad (Mujeres)
x=arrDiscapacitados[3]
y=arrEdadesMujeres.T
MMujeresEdad=Modelo(1,18,x,y,3500)

#"""
#Exportar modelos en formato H5
MDiscapacitados.save('./Api/Modelos_H5/General.h5')
MHombresTipo.save('./Api/Modelos_H5/MHombresTipo.h5')
MMujeresTipo.save('./Api/Modelos_H5/MMujeresTipo.h5')
MHombresEdad.save('./Api/Modelos_H5/MHombresEdad.h5')
MMujeresEdad.save('./Api/Modelos_H5/MMujeresEdad.h5')

#Cargar modelo en formato H5
General=keras.models.load_model('./Api/Modelos_H5/General.h5')
HombresTipo=keras.models.load_model('./Api/Modelos_H5/MHombresTipo.h5')
MujeresTipo=keras.models.load_model('./Api/Modelos_H5/MMujeresTipo.h5')
HombresEdad=keras.models.load_model('./Api/Modelos_H5/MHombresEdad.h5')
MujeresEdad=keras.models.load_model('./Api/Modelos_H5/MMujeresEdad.h5')

#Exportar modelos en formato js
tfjs.converters.save_keras_model(General, './Api/Modelos_js/General')
tfjs.converters.save_keras_model(HombresTipo,'./Api/Modelos_js/MHombresTipo')
tfjs.converters.save_keras_model(MujeresTipo,'./Api/Modelos_js/MMujeresTipo')
tfjs.converters.save_keras_model(HombresEdad,'./Api/Modelos_js/MHombresEdad')
tfjs.converters.save_keras_model(MujeresEdad,'./Api/Modelos_js/MMujeresEdad')

print('Completado')
#"""

print(MHombresTipo.predict([2904198]))