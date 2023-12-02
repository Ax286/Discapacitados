//Poblacion ejemplo 126014024

document.addEventListener('DOMContentLoaded',function(){
    obtenerPrediccion()
})

//Prediccion de discapacitados general (Hombres-Mujeres)
async function modeloGeneral(){
    const model = await tf.loadLayersModel('../Api/Modelos_js/General/model.json');
    const poblacion=document.getElementById('txtPoblacion').value
    const prediccion = model.predict(tf.tensor2d([parseFloat(poblacion)], [1, 1]));
    //Convertir el tensor 'prediccion' en un arreglo unidimencional
    return Array.from(prediccion.dataSync())
}

//Prediccion de tipo de discapacitadad (Hombres)
async function modeloHombresTipo(discapacitados){
    const model = await tf.loadLayersModel('../Api/Modelos_js/MHombresTipo/model.json');
    const prediccion = model.predict(tf.tensor2d([parseFloat(discapacitados)], [1, 1]));
    return Array.from(prediccion.dataSync())
}

//Prediccion de tipo de discapacitadad (Mujeres)
async function modeloMujeresTipo(discapacitados){
    const model = await tf.loadLayersModel('../Api/Modelos_js/MMujeresTipo/model.json');
    const prediccion = model.predict(tf.tensor2d([parseFloat(discapacitados)], [1, 1]));
    return Array.from(prediccion.dataSync())
}

//Prediccion rango de edad (Hombres)
async function modeloHombresEdad(discapacitados){
    const model=await tf.loadLayersModel('../Api/Modelos_js/MHombresEdad/model.json')
    const prediccion=model.predict(tf.tensor2d([parseFloat(discapacitados)],[1,1]))
    return Array.from(prediccion.dataSync())
}

//Prediccion rango de edad (Mujeres)
async function modeloMujeresEdad(discapacitados){
    const model=await tf.loadLayersModel('../Api/Modelos_js/MMujeresEdad/model.json')
    const prediccion=model.predict(tf.tensor2d([parseFloat(discapacitados)],[1,1]))
    return Array.from(prediccion.dataSync())
}

//Metodo principal
async function obtenerPrediccion(){
    //Obtencion de los arreglos
    const general=await modeloGeneral()
    const hombresTipo=await modeloHombresTipo(general[1])
    const mujeresTipo=await modeloMujeresTipo(general[2])
    const hombresEdad=await modeloHombresEdad(general[1])
    const mujeresEdad=await modeloMujeresEdad(general[2])

    //DESPLIEGUE DE INFORMACION
    GraficaGeneral(general)
    //GraficaHTipo(hombresTipo)
    //GraficaMTipo(mujeresTipo)
    GraficaTipoComparativa(hombresTipo,mujeresTipo)
    GraficaEdadComparacion(hombresEdad,mujeresEdad)
    GraficaTotalTipo(hombresTipo,mujeresTipo)
    GraficaTotalEdad(hombresEdad,mujeresEdad)
}

var graficaGeneral;
var graficaHTipo
var graficaMTipo
var graficaTipoComparacion
var graficaEdadComparacion
var graficaTotalTipo
var graficaTotalEdad

//GRAFICA GENERAL
function GraficaGeneral(datos) {
    var ctx = document.getElementById('GraficaGeneral').getContext('2d');

    // Datos para la gráfica de barras
    var datosGrafica = {
        labels: ['Total', 'Hombres', 'Mujeres'],
        datasets: [{
            data: datos,
            backgroundColor: ['rgba(255, 206, 86, 0.2)', 'rgba(54, 162, 235, 0.2)' ,'rgba(255, 99, 132, 0.2)'],
            borderColor: ['rgba(255, 206, 86, 1)', 'rgba(54, 162, 235, 1)','rgba(255,99,132,1)'],
            borderWidth: 2,
            borderRadius:5,
        }]
    };

    // Opciones de la gráfica
    var opciones = {
        responsive:false,
        maintainAspectRatio:true,
        scales: {
            y: {
                beginAtZero: true
            }
        },
        plugins: {
            legend: {
                display:false
            },
            title: {
              display: true,
              text: 'DISCAPACITADOS EN MÉXICO'
            }
          }
    };

    if (graficaGeneral) {
        graficaGeneral.data = datosGrafica;
        graficaGeneral.options=opciones;
        graficaGeneral.update();
    } else {
        graficaGeneral = new Chart(ctx, {
            type: 'bar',
            data: datosGrafica,
            options: opciones
        });
    }
}

//GRAFICA COMPARATIVA TIPO DE DISCAPACITAD
function GraficaTipoComparativa(hombres,mujeres){
    var ctx = document.getElementById('GraficaTipoComparativa').getContext('2d');
    // Datos para la gráfica de barras
    var datosGrafica = {
        labels: ['Ver', 'Oir', 'Caminar','Recordar','Bañarse','Hablar'],
        datasets: [{
            label:'Hombres',
            data: hombres,

            borderColor: 'rgba(54, 162, 235, 0.2)',
            backgroundColor: 'rgb(54, 162, 235)',
            borderWidth: 1
        },
        {
            label:'Mujeres',
            data: mujeres,
            borderColor: 'rgba(255, 99, 132, 0.2)',
            backgroundColor: 'rgb(255, 99, 132)',
            borderWidth: 1
        },
        
    ]
    };

    //Opciones de la grafica
    var opciones={
        indexAxis: 'y',
        // Elements options apply to all of the options unless overridden in a dataset
        // In this case, we are setting the border of each horizontal bar to be 2px wide
        elements: {
          bar: {
            borderWidth: 2,
          }
        },
        responsive: false,
        maintainAspectRatio:true,
        plugins: {
          legend: {
            position: 'right',
          },
          title: {
            display: true,
            text: 'COMPARACIÓN TIPO DE DISCAPACIDAD'
          }
        }
    }

    //Actualizar grafica
    if (graficaTipoComparacion) {
        graficaTipoComparacion.data = datosGrafica;
        graficaTipoComparacion.options = opciones;
        graficaTipoComparacion.update();
    } else {
        graficaTipoComparacion = new Chart(ctx, {
            type: 'bar',
            data: datosGrafica,
            options: opciones
        });
    }
}

//GRAFICA DE TOTAL DE DISCAPACITADOS POR TIPO
function GraficaTotalTipo(hombres,mujeres){

    total=Suma2Arreglos(hombres,mujeres)

    var ctx = document.getElementById('GraficaTotalTipo').getContext('2d');

    // Datos para la gráfica de barras
    var datosGrafica = {
        labels: ['Ver', 'Oir', 'Caminar, subir o bajar','Recordar o concentrarse','Bañarse, vestirse o comer','Hablar o comunicarse'],
        datasets: [{
            data: total,
            backgroundColor: ['rgba(255, 99, 132, 0.2)','rgba(255, 159, 64, 0.2)','rgba(255, 205, 86, 0.2)',
            'rgba(75, 192, 192, 0.2)','rgba(54, 162, 235, 0.2)','rgba(153, 102, 255, 0.2)'],
            borderColor: ['rgb(255, 99, 132)','rgb(255, 159, 64)','rgb(255, 205, 86)','rgb(75, 192, 192)',
            'rgb(54, 162, 235)','rgb(153, 102, 255)'],
            borderWidth: 1
        }]
    };

    // Opciones de la gráfica
    var opciones = {
        responsive: false,
        maintainAspectRatio: true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'TOTAL DE DISCAPACITADOS POR TIPO',
            }
        }
      }

    if (graficaTotalTipo) {
        graficaTotalTipo.data = datosGrafica;
        graficaTotalTipo.options = opciones;
        graficaTotalTipo.update();
    } else {
        graficaTotalTipo = new Chart(ctx, {
            type: 'polarArea',
            data: datosGrafica,
            options: opciones
        });
    }
}

//GRAFICA RANGO DE EDAD COMPARACION
function GraficaEdadComparacion(hombres,mujeres){
    var ctx = document.getElementById('GraficaEdadComparativa').getContext('2d');

    var datosGrafica={
        labels: ['0 a 4','5 a 9','10 a 14','15 a 19','20 a 24','25 a 29','30 a 34','35 a 39','40 a 44','45 a 49',
    '50 a 54','55 a 59','60 a 64','65 a 69','70 a 74','75 a 79','80 a 84','85 y mas'],
        datasets: [
            {
            label: 'Hombres',
            data: hombres,
            borderColor: 'rgba(54, 162, 235, 0.2)',
            backgroundColor: 'rgb(54, 162, 235)',
            },
            {
            label: 'Mujeres',
            data: mujeres,

            borderColor: 'rgba(255, 99, 132, 0.2)',
            backgroundColor: 'rgb(255, 99, 132)',
            }
        ]
    }

    var opciones={
        responsive: false,
        maintainAspectRatio:true,
        plugins: {
            legend: {
                position: 'top',
            },
            title: {
                display: true,
                text: 'COMPARACIÓN ENTRE HOMBRES Y MUJERES DISCAPACITADOS POR RANGO DE EDAD'
            }
        }
    }

    if (graficaEdadComparacion) {
        graficaEdadComparacion.data = datosGrafica;
        graficaEdadComparacion.options = opciones;
        graficaEdadComparacion.update();
    } else {
        graficaEdadComparacion = new Chart(ctx, {
            type: 'line',
            data: datosGrafica,
            options: opciones
        });
    }
}

//GRAFICA DE TOTAL DE DISCAPACITADOS POR EDAD
function GraficaTotalEdad(hombres,mujeres){

    total=Suma2Arreglos(hombres,mujeres)

    var ctx = document.getElementById('GraficaTotalEdad').getContext('2d');

    // Datos para la gráfica de barras
    var datosGrafica = {
        labels: ['0 a 4','5 a 9','10 a 14','15 a 19','20 a 24','25 a 29','30 a 34','35 a 39','40 a 44','45 a 49',
        '50 a 54','55 a 59','60 a 64','65 a 69','70 a 74','75 a 79','80 a 84','85 y mas'],
        datasets: [
            {
            data: total,
            backgroundColor: 'rgba(255, 206, 86, 0.2)',
            borderColor: 'rgba(255, 206, 86, 1)',
            }
        ]
    };

    // Opciones de la gráfica
    var opciones = {
        responsive: false,
        maintainAspectRatio: true,
        plugins: {
          legend: {
            display:false,
          },
          title: {
            display: true,
            text: 'TOTAL DE DISCAPACITADOS POR RANGO DE EDAD'
          }
        }
      }

    if (graficaTotalEdad) {
        graficaTotalEdad.data = datosGrafica;
        graficaTotalEdad.options = opciones;
        graficaTotalEdad.update();
    } else {
        graficaTotalEdad = new Chart(ctx, {
            type: 'radar',
            data: datosGrafica,
            options: opciones
        });
    }
}

//FUNCION PARA SUMAR 2 ARREGLOS
function Suma2Arreglos(arr1,arr2){
    var total=[]
    if(arr1.length==arr2.length){
        for(let x=0;x<arr1.length;x++){
            total[x]=arr1[x]+arr2[x]
        }
        return total
    }else{
        return console.log('Ambos arreglos no miden los mismo')
    }
}






