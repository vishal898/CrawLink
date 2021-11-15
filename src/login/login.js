const { ipcRenderer } = require('electron');




document.getElementById("submit").addEventListener('click',()=>{
    console.log('button clicked')
    u = document.getElementById("username").value
    p = document.getElementById("password").value
    console.warn(`login-${u}`);
    console.warn(`login-${p}`);
    if(u!=="" && p !==""){
        ipcRenderer.send("setValue",["username", u]);
        ipcRenderer.send("setValue",["password", p]);
        ipcRenderer.send("renderPage",[{page:'home/home.html'}]);
    }
});





