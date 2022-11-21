
    var ctx = document.getElementById('polarChart').getContext('2d');
    var labels = [{% for stage in stages %} '{{stage.stage_id}}',{% endfor %}]
    var polarChart = new Chart(ctx, {
        type: 'polarArea',
        data: {
              labels: labels,
              datasets: [
                {
                  label: 'Dataset 1',
                  data: [
                      {{ total_stage_new }},
                    {{ total_stage_qualified }},
                    {{ total_stage_preposition }},
                    {{ total_stage_won }},
                    {{ total_stage_lost }},
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
                }
              ]
            },
        options: {
        responsive: true,
        scales: {
          r: {
            pointLabels: {
              display: true,
              centerPointLabels: true,
              font: {
                size: 18
              }
            }
          }
        },
        },
    })


