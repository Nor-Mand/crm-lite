
    var ctx = document.getElementById('polarChart').getContext('2d');
    var labels = [{% for stage in stages %} '{{stage}}',{% endfor %}]
    var polarChart = new Chart(ctx, {
        type: 'polarArea',
        data: {
              labels: labels,
              datasets: [
                {
                  data: [
                      {{ total_stage_new }},
                    {{ total_stage_qualified }},
                    {{ total_stage_preposition }},
                    {{ total_stage_won }},
                    {{ total_stage_lost }},
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
                }
              ]
            },
        options: {
          plugins:{
            legend:{
                labels:{
                    color: "#F3F4F6",
                    padding: 50,
                }
            }
          },
        responsive: true,
        scales: {
          r: {
            pointLabels: {
              display: true,
              centerPointLabels: true,
              font: {
                size: 13
              },
              color: "#F3F4F6",
            }
          },
          
        },
        
        },
    })


