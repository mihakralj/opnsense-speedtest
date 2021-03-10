<script src="/ui/js/d3.min.js"></script>
<script src="/ui/js/nv.d3.min.js"></script>
<link rel="stylesheet" type="text/css" href="/ui/css/nv.d3.css">

<div id="chart">yo</div>
<script>
    var chart = nv.models.pieChart();
    chart.width(500);
    chart.title('stuff').titleOffset(-10);
    chart.options({
        height: 500,
        donut: true
    });
</script>


<h1> hello world!</h1>