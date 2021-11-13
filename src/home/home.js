const { ipcRenderer } = require('electron');
//ipcRenderer.send("renRam");

console.log('home page');
document.getElementById("1").addEventListener('click',()=>{
    console.log('card cliked');
    ipcRenderer.send("renderPage",[{page:'connection/connection.html'}]);
});
document.getElementById("2").addEventListener('click',()=>{
    console.log('card cliked');
    ipcRenderer.send("renderPage",[{page:'withdraw/withdraw.html'}]);
});
document.getElementById("3").addEventListener('click',()=>{
    console.log('card cliked');
    ipcRenderer.send("renderPage",[{page:'accept/accept.html'}]);
});
document.getElementById("4").addEventListener('click',()=>{
    console.log('card cliked');
    ipcRenderer.send("renderPage",[{page:'notification/notification.html'}]);
});
document.getElementById("5").addEventListener('click',()=>{
    console.log('card cliked');
    ipcRenderer.send("renderPage",[{page:'connection/connection.html'}]);
});
document.getElementById("6").addEventListener('click',()=>{
    console.log('card cliked');
    ipcRenderer.send("renderPage",[{page:'connection/connection.html'}]);
});
document.getElementById("7").addEventListener('click',()=>{
    console.log('card cliked');
    ipcRenderer.send("renderPage",[{page:'connection/connection.html'}]);
});
document.getElementById("8").addEventListener('click',()=>{
    console.log('card cliked');
    ipcRenderer.send("renderPage",[{page:'endorse/endorse.html'}]);
});


document.querySelector('#lgout').addEventListener('click', (e) => {
    e.preventDefault();
    let p = document.querySelector('#lgout').getAttribute("href");
    console.log(p);
    let un ="",pw="";
    ipcRenderer.send("setValue",["username", un]);
    ipcRenderer.send("setValue",["password", pw]);
    console.log(`default username -> ${un}`);
    console.log(`default password -> ${pw}`);

    ipcRenderer.send("renderPage", [{
        page: p
    }]);
});