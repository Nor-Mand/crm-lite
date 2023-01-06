
var ctx = document.getElementById('miniChart').getContext('2d');
var labels = [{% for stage in stages %} '{{stage.name}}',{% endfor %}]
var miniChart = new Chart(ctx,{
   type: 'bar',
   data: {
     labels: labels,
     datasets: [{
       data: [
           {% for stage in stages %} '{{stage.lead_set.all.count}}',{% endfor %}
       ],
        backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 99, 132, 0.2)',
            ],
            borderColor: [
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 99, 132, 1)',
                'rgba(255, 159, 64, 1)'
            ],
       borderWidth: 1
     }]
   },
   options: {
       plugins: {
          legend: {
              display: false,

          },
          tooltip: {
            callbacks: {
              title: () => null
            }
          }
        },
       scales: {
          y: {
            display: false
        }
    },
   }
})
