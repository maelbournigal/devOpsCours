<template>
  <div id="app">
    <!--<p>test</p>-->
    <LineChartContainer></LineChartContainer>
  </div>
</template>

<script>

import LineChartContainer from "./views/ChartContainer";
export default {
  name: 'app',
  components: {
    LineChartContainer,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
