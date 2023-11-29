import * as tf from '@tensorflow/tfjs'
const model = await tf.loadLayersModel('./Modelos_js/General/model.json');

prediccion=model.predict([2904198])
console.log(prediccion)