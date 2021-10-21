const { ipcRenderer } = require('electron');

document.querySelector('a').addEventListener('click',(e)=>{
    e.preventDefault()
    let p = document.querySelector('a').getAttribute("href");
    console.log(p);
    // setInterval(()=>{
        ipcRenderer.send("renderPage",[{page:p}]);
    // },10000);
});

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