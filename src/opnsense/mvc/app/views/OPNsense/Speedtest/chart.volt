{# Copyright 2021 Miha Kralj 
    # Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at 
    # http://www.apache.org/licenses/LICENSE-2.0 
    # Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License. 
#}

<script src="{{ cache_safe('/ui/js/plotly.min.js') }}"></script>

<div id="chart">

</div>

<script>
    $(document).ready(function() {
        ajaxGet("/api/speedtest/service/stat", {}, function(data, status) {
            if (status == 'success') {
                let l = JSON.parse(data['response']);
                let dl = l['download'];
                var data = [
                    {
                        domain: { x: [0, 1], y: [0, 1] },
                        type: "indicator",
                        mode: "gauge+number+delta",
                        
                        value: parseFloat(l['download']['last']),
                        title: { text: "Download speed" },

                        delta: { reference: parseFloat(l['download']['avg']) },
                        gauge: {
                            axis: { range: [null, 1000] },
                            steps: [
                                { range: [0, parseFloat(l['download']['min'])], color: "lightgray" },
                                { range: [parseFloat(l['download']['min']), parseFloat(l['download']['max'])], color: "gray" }
                            ],
                            threshold: {
                                line: { color: "red", width: 10 },
                                thickness: 0.75,
                                value: parseFloat(l['download']['max'])
                            }
                        }
                    }
                    ];
                var layout = { width: 600, height: 400 };
                chart = document.getElementById('chart');
                Plotly.newPlot( chart, data, layout );
            };
        });
    });
</script>



