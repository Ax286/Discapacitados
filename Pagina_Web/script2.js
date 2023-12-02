// Datos iniciales para la segunda gráfica
const data2 = {
  labels: ['Etiqueta A', 'Etiqueta B', 'Etiqueta C'],
  datasets: [{
    data: [20, 30, 50],
    backgroundColor: ['#FF5733', '#33FF57', '#5733FF']
  }]
};
// Configuración de la segunda gráfica
const config2 = {
  type: 'pie',
  data: data2,
};
// Crear la segunda gráfica en el canvas
const ctx2 = document.getElementById('pieChart2').getContext('2d');
const pieChart2 = new Chart(ctx2, config2);