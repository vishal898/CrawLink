const { ipcRenderer } = require('electron');
// import {ipcRenderer} from "electron";
// document.getElementById("messForm").addEventListener('submit',(e)=>{
//     e.preventDefault();
//     console.log('form submitted');
//     let username = document.getElementById('username').value
//     let password = document.getElementById('password').value
//     let connection = document.getElementById('connection').value
//     ipcRenderer.send("msg",[username,password,connection]);
//     ipcRenderer.on('rev', (event, arg) => {
//         console.log("exe file started") 
//     })
//     ipcRenderer.on('clo', (event, arg) => {
//         console.log(arg) 
//     })
// });
// const Cred = require('electron-store');

document.getElementById("submit").addEventListener('click',()=>{
    console.log('button clicked')
    u = document.getElementById("username").value
    p = document.getElementById("password").value
    console.log(u);
    console.log(p);
    ipcRenderer.send("setValue",["username", u]);
    ipcRenderer.send("setValue",["password", p]);
    ipcRenderer.send("renderPage",[{page:'home/home.html'}]);
});





