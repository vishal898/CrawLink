const { ipcRenderer } = require('electron');



function detailssubmit() {
    document.getElementById("count").required = true
    let cnt=document.getElementById("count").value;
    console.log(cnt);
    if(cnt<=30)
    {
        console.log(cnt);
        //ipcRenderer.send("accept",cnt);
    }
}