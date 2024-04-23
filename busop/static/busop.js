// Dummy data for demonstration
const dailyAmount = 1500;
const dailyTravelers = 50;
const monthlyAmount = 45000;
const monthlyTravelers = 1500;

// Update daily statistics
document.getElementById('daily-amount').textContent = `${dailyAmount}`;
document.getElementById('daily-travelers').textContent = dailyTravelers;

// Update monthly statistics
document.getElementById('monthly-amount').textContent = `${monthlyAmount}`;
document.getElementById('monthly-travelers').textContent = monthlyTravelers;

// Create a sample chart using Chart.js
const ctx = document.getElementById('monthly-chart').getContext('2d');
const chart = new Chart(ctx, {
  type: 'line',
  data: {
    labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    datasets: [{
      label: 'Monthly Revenue',
      backgroundColor: 'rgba(75, 192, 192, 0.2)',
      borderColor: 'rgba(75, 192, 192, 1)',
      borderWidth: 1,
      data: [5000, 7000, 10000, 8000, 12000, 15000, 18000, 20000, 17000, 19000, 22000, 25000]
    }]
  },
  options: {
    scales: {
      yAxes: [{
        ticks: {
          beginAtZero: true
        }
      }]
    }
  }
});
