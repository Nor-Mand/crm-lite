
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
          'rgba(0, 255, 255)',
          'rgb(0,206,209)',
          'rgb(255,215,0)',
          'rgba(153, 102, 255)',
          'rgb(255,99,71)',
            ],
            borderColor: [
              'rgba(54, 162, 235, 0.2)',
                // 'rgba(255, 206, 86, 1)',
                // 'rgba(75, 192, 192, 1)',
                // 'rgba(153, 102, 255, 1)',
                // 'rgba(255, 99, 132, 1)',
                // 'rgba(255, 159, 64, 1)'
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
        },
           x: {  // not 'xAxes: [{' anymore (not an array anymore)
        ticks: {
          color: "white",  // not 'fontColor:' anymore
          //fontSize: 14,
          font: {
            size: 12 // 'size' now within object 'font {}'
          },
          stepSize: 1,
          beginAtZero: true
        }
      }
    },
   }
})
