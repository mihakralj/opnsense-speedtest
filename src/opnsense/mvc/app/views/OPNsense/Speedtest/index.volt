
<h2>Statistics:</h2>
 <table class="table table-condensed">
     <tbody>
         <tr>
             <td style="width:30%">Speedtest probes:</td>
             <td><div id="stat_samples">0</div></td>
         </tr>
         <tr>
             <td>Average Latency:</td>
             <td id="stat_latency">0.00 ms (min: 0.00 ms, max: 0.00 ms)</td>
         </tr>
        <tr>
            <td>Average Download speed:</td>
            <td id="stat_download">0 Mbps (min: 0 Mbps, max: 0 Mbps)</td>
        </tr>
        <tr>
            <td>Average Upload speed:</td>
            <td id="stat_upload">0 Mbps (min: 0 Mbps, max: 0 Mbps)</td>
        </tr>
     </tbody>
 </table>

 <hr>
 <h2>Diagnostics:</h2>

<select id="speedlist" name="serverid">
    <option value="12345">Fetching list of Speedtest servers...</option>
</select>


<div class="content-box">
    <div class="content-box-main collapse in" id="system_information-container" style="display:inline">
      

<table class="table table-striped">
<tbody>
    <tr>
        <td style="width:30%"></td> 
        <td style="width:30%"><button class="btn btn-primary" id="reportAct" type="button">
            <b>{{ lang._('socket test') }}</b> <i id="reportAct_progress"></i></button></td>  
        <td style="width:30%"><button class="btn btn-primary" id="reportPyAct" type="button">
            <b>{{ lang._('http test') }}</b> <i id="reportPyAct_progress"></i></button></td>  
    </tr>    
<tr>
    <td>Latency (ping)</td> 
    <td id="latency">0 ms</td>  
    <td id="pylatency">0 ms</td>  
</tr>
<tr>
    <td>Download speed</td> 
    <td id="dlspeed">0 Mbps</td>  
    <td id="pydlspeed">0 Mbps</td>  
</tr>
<tr>
    <td>Upload speed</td> 
    <td id="ulspeed">0 Mbps</td>  
    <td id="pyulspeed">0 Mbps</td>  
</tr>
<tr>
    <td>Speedtest server</td>
    <td><div id="host1"></div>
        <div id="ISP1"></div>
        <div id="ISP2"></div>
        <div id="ISP3"></div>
    </td>
    <td><div id="pyhost1"></div>
        <div id="pyhost3"></div>
        <div id="pyhost4"></div>
        <div id="pyhost5"></div>
    </td>
</tr>
<tr>
    <td>Client</td>
    <td><div id="client4"></div>
        <div id="client5"></div>
    </td>
    <td><div id="pyclient"></div></td>
</tr>
<tr>
    <td>Result id</td>
    <td><div id="result"></div></td>
    <td><div id="pyresult">
    </div></td>
    </td>
</tr>
</tbody>
</table>
</div>

<script>
    $(document).ready(function() {
        ajaxCall(url="/api/speedtest/service/list", sendData={}, callback=function(data,status) {
            let l = JSON.parse(data['response']).servers
            let list = ""
            $('#speedlist').text("")
            for (var i = 0; i < l.length; i++) {
                $('#speedlist').append("<option value=\""+ l[i].id +"\">" + l[i].host + "<\/option>");
            }
       });
       ajaxCall(url="/api/speedtest/service/stat", sendData={}, callback=function(data,status) {
            let l = JSON.parse(data['response'])
            $('#stat_samples').text(l.samples+" (since "+l.timestamp.oldest+" GMT)")
            $('#stat_latency').text(l.latency.avg+" ms (min: "+l.latency.min+" ms, max: "+l.latency.max +" ms)")
            $('#stat_download').text(l.download.avg+" Mbps (min: "+l.download.min+" Mbps, max: "+l.download.max +" Mbps)")
            $('#stat_upload').text(l.upload.avg+" Mbps (min: "+l.upload.min+" Mbps, max: "+l.upload.max +" Mbps)")
       });
    });
    $(function() {
        // python button
        $("#reportPyAct").click(function(){
            $("#reportPyAct_progress").addClass("fa fa-spinner fa-pulse");
            $("#debug").text($('#speedlist').val());
            ajaxCall(url="/api/speedtest/service/pytest/"+$('#speedlist').val(), sendData={}, callback=function(data,status) {
                    let py = JSON.parse(data['response'])
                    $("#pylatency").text(py.ping+" ms");
                    $("#pydlspeed").text((py.download/1000000).toFixed(2)+" Mbps");
                    $("#pyulspeed").text((py.upload/1000000).toFixed(2)+" Mbps");
                    $("#reportPyAct_progress").removeClass("fa fa-spinner fa-pulse");
                    $("#pyhost1").text(py.server.host);
                    $("#pyhost2").text("IPv4: ");
                    $("#pyhost3").text("id: "+py.server.id);
                    $("#pyhost4").text(py.server.name);
                    $("#pyhost5").text(py.server.country);
                    $("#pyclient").text("Public IP: "+py.client.ip);
                    let pyresulturl = py.share.slice(0,py.share.length-4)
                    let pyresult = pyresulturl.slice(pyresulturl.lastIndexOf("/")+1)
                    $("#pyresult").html("<a href=\""+pyresulturl+"\"  target=\"_blank\">"+pyresult+"</a>");
                });
            });
        // Oookla binary button
        $("#reportAct").click(function(){
                $("#reportAct_progress").addClass("fa fa-spinner fa-pulse");
                ajaxCall(url="/api/speedtest/service/test/"+$('#speedlist').val(), sendData={}, callback=function(data,status) {
                    let r = JSON.parse(data['response'])          
                    $("#latency").text(r.ping.latency+" ms ("+r.ping.jitter+" ms jitter)");  
                    $("#dlspeed").text((r.download.bandwidth/125000).toFixed(2)+" Mbps");
                    $("#ulspeed").text((r.upload.bandwidth/125000).toFixed(2)+" Mbps");
                    $("#host1").text(r.server.host+":"+r.server.port);  
                    $("#host2").text("IPv4: "+r.server.ip);  
                    $("#ISP1").text("id: "+r.server.id + " ("+r.server.name+")");
                    $("#ISP2").text(r.server.location);
                    $("#ISP3").text(r.server.country);    
                    $("#client4").text("Public IP: "+r.interface.externalIp);
                    $("#client5").text("VPN detected: "+r.interface.isVpn);
                    $("#result").html("<a href=\""+r.result.url+"\"  target=\"_blank\">"+r.result.id+"</a>");
                    $("#reportAct_progress").removeClass("fa fa-spinner fa-pulse");
                });

        });
    });
</script>
