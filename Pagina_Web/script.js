document.addEventListener('DOMContentLoaded', function() {
  // Datos iniciales para la primera gráfica
  const data = {
    labels: ['Hombres', 'Mujeres'],
    datasets: [{
      data: [60, 40],
      backgroundColor: ['#0000AA', '#FF00FF']
    }]
  };

  // Configuración de la primera gráfica
  const config = {
    type: 'pie',
    data: data,
  };

  // Crear la primera gráfica en el canvas
  const ctx = document.getElementById('pieChart').getContext('2d');
  const pieChart = new Chart(ctx, config);
});

document.addEventListener('DOMContentLoaded', function() {
  // Datos iniciales para la segunda gráfica
  const data2 = {
    labels: ['0 a 4', '5 a 9', '10 a 14', '15 a 19', '20 a 25', '...', '85 y mas'],
    datasets: [{
      data: [10, 10, 10, 10, 10, 10, 40],
      backgroundColor: ['#0000FF', '#008000', '#FF0000', '#FFFF00', '#FF69B4', '#800080', '#40E0D0']
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
});

document.addEventListener('DOMContentLoaded', function() {
  // Datos iniciales para la tercera gráfica
  const data3 = {
    labels: ['0 a 4', '5 a 9', '10 a 14', '15 a 19', '20 a 25', '...', '85 y mas'],
    datasets: [{
      data: [10, 10, 10, 10, 10, 10, 40],
      backgroundColor: ['#0000FF', '#008000', '#FF0000', '#FFFF00', '#FF69B4', '#800080', '#40E0D0']
    }]
  };

  // Configuración de la tercera gráfica
  const config3 = {
    type: 'pie',
    data: data3,
  };

  // Crear la tercera gráfica en el canvas
  const ctx3 = document.getElementById('pieChart3').getContext('2d');
  const pieChart3 = new Chart(ctx3, config3);
});

document.addEventListener('DOMContentLoaded', function() {
  // Datos iniciales para la cuarta gráfica
  const data4 = {
    labels: ['0 a 4', '5 a 9', '10 a 14', '15 a 19', '20 a 25', '...', '85 y mas'],
    datasets: [{
      data: [10, 10, 10, 10, 10, 10, 40],
      backgroundColor: ['#0000FF', '#008000', '#FF0000', '#FFFF00', '#FF69B4', '#800080', '#40E0D0']
    }]
  };

  // Configuración de la cuarta gráfica
  const config4 = {
    type: 'pie',
    data: data4,
  };

  // Crear la cuarta gráfica en el canvas
  const ctx4 = document.getElementById('pieChart4').getContext('2d');
  const pieChart4 = new Chart(ctx4, config4);
});

// Función para actualizar la gráfica con nuevos datos (simulación de una API)
function actualizarGrafica(nuevosDatos) {
  pieChart.data.datasets[0].data = nuevosDatos;
  pieChart.update();
}

// Ejemplo de cómo utilizar la función para actualizar la gráfica con nuevos datos (simulación de una API)
const nuevosDatos = [40, 30, 30];
actualizarGrafica(nuevosDatos);
