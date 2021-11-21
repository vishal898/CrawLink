const {
    ipcRenderer
} = require('electron');
const path = require('path');

document.querySelector('a').addEventListener('click',(e)=>{
    e.preventDefault()
    let p = document.querySelector('a').getAttribute("href");
    console.log(p);
    // setInterval(()=>{
        ipcRenderer.send("renderPage",[{page:p}]);
    // },10000);
});

ipcRenderer.send('email-request', 'hello');

ipcRenderer.on('email-reply', function (event, args) {
    console.log(args); 
    var email=args;
    document.getElementById('email').innerHTML=args
  });

  document.querySelector('#logout').addEventListener('click', (e) => {
    e.preventDefault();
    let p = document.querySelector('#logout').getAttribute("href");
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

