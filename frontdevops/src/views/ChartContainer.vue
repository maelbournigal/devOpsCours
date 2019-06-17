<template>
    <div class="container">
        <form
                id="app"
                @submit="checkForm"
                method="get"
        >
            <label for="unite">Numéro d'unité</label>
            <select id="unite"
                    v-model="unite"
                    name="unite"
            >
                <option value="1">unité 1</option>
                <option value="2">unité 2</option>
                <option value="3">unité 3</option>
                <option value="4">unité 4</option>
                <option value="5">unité 5</option>
            </select>
            <label for="automate">Numéro d'automate</label>
            <select id="automate"
                    v-model="automateNum"
                    name="automate"
            >
                <option value="1">automate 1</option>
                <option value="2">automate 2</option>
                <option value="3">automate 3</option>
                <option value="4">automate 4</option>
                <option value="5">automate 5</option>
                <option value="5">automate 6</option>
                <option value="5">automate 7</option>
                <option value="5">automate 8</option>
                <option value="5">automate 9</option>
                <option value="5">automate 10</option>
            </select>
            <input type="submit" value="Submit">
        </form>
        <chart
                v-if="loaded"
                :chartdata="chartdata"
                :chartLabels="labels"/>

        <chart
            v-if="loaded"
            :chartdata="dataTemp"
            :chart-labels="labels"
        />
        <chart
            v-if="loaded"
            :chartdata="dataPoids"
            :chart-labels="labels"
        />
    </div>
</template>

<script>
    import Chart from '../components/Chart';
    import axios from 'axios';

    export default {
        name: 'LineChartContainer',
        components: { Chart },
        data() {
            return {
                unite: 1,
                automateNum: 1,
                period: 'last-hour',
                loaded: false,
                chartdata: {
                    chlorureDeSodium: [],
                    patasium: [],
                    ecoli: [],
                    listeria: [],
                    salmonelle: [],
                    ph: [],
                },
                dataTemp: {
                    tempCuve: [],
                    tempExt: [],
                },
                dataPoids: {
                    poidMilkCuve: [],
                    productEnd: [],
                },
                labels: [],
            }
        },
        mounted () {
            this.getData();
            this.interval = setInterval(() => this.getData(), 60000);
        },
        methods: {
            getData() {
                this.loaded  = false;
                axios
                    .get(`http://192.168.213.128:4000/mesures/${this.unite}/${this.automateNum}`)
                    .then(res =>  {
                        this.chartdata = {};
                        let tz = new Date().getTimezoneOffset()/60;
                        this.labels =  res.data.map(mesure => new Date(new Date(mesure.dateMesure).setHours(new Date(mesure.dateMesure).getHours() - tz)).toISOString())
                        this.chartdata.chlorureDeSodium = res.data.map(mesure => mesure.chlorureDeSodium)
                        this.chartdata.potasium = res.data.map(mesure => mesure.ionPotassium)
                        this.chartdata.ecoli = res.data.map(mesure => mesure.niveauEColi)
                        this.chartdata.listeria = res.data.map(mesure => mesure.niveauListeria)
                        this.chartdata.salmonelle = res.data.map(mesure => mesure.niveauSalmonelle)
                        this.chartdata.ph = res.data.map(mesure => mesure.pH)
                        this.dataPoids.poidMilkCuve = res.data.map(mesure => mesure.poidsLaitCuve)
                        this.dataPoids.productEnd = res.data.map(mesure => mesure.poidsProduitFini)
                        this.dataTemp.tempCuve = res.data.map(mesure => mesure.tempCuve)
                        this.dataTemp.tempExt = res.data.map(mesure => mesure.tempExterieure)
                        this.loaded = true
                    })
                    .catch(e => {
                        console.log(e)
                    })
            },
            checkForm(e) {
                e.preventDefault();
                this.getData();
            }
        }
    }
</script>
