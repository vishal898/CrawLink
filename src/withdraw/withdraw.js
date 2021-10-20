const { ipcRenderer } = require('electron');
ipcRenderer.send("renRam");



let cnt,br,newListItem;
function detailSubmit() {
    document.getElementById("w1").required = true
    cnt=document.getElementById("w1").value;
    console.log(cnt);
    if(cnt<=25)
    {
        console.log(cnt);
        //ipcRenderer.send("accept",cnt);
    }

    for (var i = 0; i < cnt; i++) {
        newListItem = document.createElement('a');
        br=document.createElement('br')
        newListItem.setAttribute('href', 'http://newurl.com');
        newListItem.textContent = 'http://newurl.com';
        document.querySelector('.links').appendChild(newListItem);
        document.querySelector('.links').appendChild(br);
    }
}
const form = document.getElementById('submit');
form.addEventListener('click', detailSubmit);

