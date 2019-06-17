
<script>
    import {Line} from 'vue-chartjs'

    export default {
        extends: Line,
        props: {
            chartdata: {
                type: Object,
                required: true
            },
            chartLabels: {
                type: Array,
                required: true
            }
        },
        data() {
          return {
              options: {
                  scales: {
                      yAxes: [{
                          ticks: {
                              beginAtZero: true
                          },
                          gridLines: {
                              display: true
                          }
                      }],
                      xAxes: [{
                          gridLines: {
                              display: false
                          }
                      }]
                  },
                  legend: {
                      display: true
                  },
                  responsive: true,
                  maintainAspectRatio: false
              }
          }
        },
        mounted () {
            let labels = [];

            this.chartLabels.forEach(label => {
                const data = new Date(label)
                labels.push(data.getUTCHours() + ':' + data.getUTCMinutes() +  ':' + data.getUTCSeconds())
            });

            if (this.chartdata.salmonelle !== undefined) {
                this.renderChart({
                    labels: labels,
                    datasets: [
                        {
                            label: 'Salmonelle',
                            borderColor: '#FF5684',
                            borderWidth: 1,
                            backgroundColor: 'transparent',
                            data: this.chartdata.salmonelle
                        },
                        {
                            label: 'Chlorure de sodium',
                            borderColor: '#00FF58',
                            borderWidth: 1,
                            backgroundColor: 'transparent',
                            data: this.chartdata.chlorureDeSodium
                        },
                        {
                            label: 'ecoli',
                            borderColor: '#6589FF',
                            borderWidth: 1,
                            backgroundColor: 'transparent',
                            data: this.chartdata.ecoli
                        },
                        {
                            label: 'listeria',
                            borderColor: '#A05F8F',
                            borderWidth: 1,
                            backgroundColor: 'transparent',
                            data: this.chartdata.listeria
                        },
                        {
                            label: 'pH',
                            borderColor: '#FFF985',
                            borderWidth: 1,
                            backgroundColor: 'transparent',
                            data: this.chartdata.ph
                        },
                        {
                            label: 'potasium',
                            borderColor: '#000',
                            borderWidth: 1,
                            backgroundColor: 'transparent',
                            data: this.chartdata.potasium
                        },
                    ]
                }, this.options)
            }
            if (this.chartdata.poidMilkCuve !== undefined)  {
                this.renderChart({
                    labels: labels,
                    datasets: [
                        {
                            label: 'poids du lait dans la cuve',
                            borderColor: '#00FF58',
                            borderWidth: 1,
                            backgroundColor: 'transparent',
                            data: this.chartdata.poidMilkCuve
                        },
                        {
                            label: 'Poids du produits fini',
                            borderColor: '#A05F8F',
                            borderWidth: 1,
                            backgroundColor: 'transparent',
                            data: this.chartdata.productEnd
                        }
                    ]
                }, this.options)
            }
            if (this.chartdata.tempCuve !== undefined)  {
                this.renderChart({
                    labels: labels,
                    datasets: [
                        {
                            label: 'Température de la cuve',
                            borderColor: '#00FF58',
                            borderWidth: 1,
                            backgroundColor: 'transparent',
                            data: this.chartdata.tempCuve
                        },
                        {
                            label: 'Température extérieur',
                            borderColor: '#6589FF',
                            borderWidth: 1,
                            backgroundColor: 'transparent',
                            data: this.chartdata.tempExt
                        }
                    ]
                }, this.options)
            }
        }
    }
</script>

<style scoped>
    h3 {
        margin: 40px 0 0;
    }
    ul {
        list-style-type: none;
        padding: 0;
    }
    li {
        display: inline-block;
        margin: 0 10px;
    }
    a {
        color: #42b983;
    }
</style>
