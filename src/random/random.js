const {
    ipcRenderer
} = require('electron');
document.getElementById("submit").addEventListener('click',(e)=>{
    e.preventDefault();
    console.log('form submitted');
    let conns =[];
    let comps = [];
    let locs = [];
    for(let i=1;i<=3;i++){
        if (document.getElementById(`${i}`).checked){
            conns.push(document.getElementById(`${i}`).value);
        }
    }
    
    document.getElementById("ul1").querySelectorAll('li').forEach((item, index) => {
      locs.push(item.innerText);
    });
    
    document.getElementById("ul2").querySelectorAll('li').forEach((item, index) => {
        comps.push(item.innerText);
    });
    conns = JSON.stringify(conns);
    locs = JSON.stringify(locs);
    comps = JSON.stringify(comps);
    console.log(conns);
    console.log(locs);
    console.log(comps);
    ipcRenderer.send("runexefile",[conns,locs,comps]);
    // ipcRenderer.on('ver', (event, arg) => {
    //     console.log("exe file started");
    // })
    // ipcRenderer.on('clo', (event, arg) => {
    //     console.log(arg);
    // })
});
let list = [
    [],
    [],
    [],
]
document.getElementById("b1").addEventListener("click", add1);
document.getElementById("c1").addEventListener("click", clearList1);
document.getElementById("ul1").addEventListener("click", remove1);

function renderList1(lst) {
    let lt = "";
    for (let i = 0; i < lst.length; i++) {
        lt += `<li value="${i}" >${lst[i]}</li>`;
    }
    if (lt) document.getElementById("ul1").innerHTML = lt;
    else document.getElementById("ul1").innerHTML = "Nothing Added Yet";
}

function add1() {
    word = document.getElementById("w1");
    console.log(list[1]);
    if (word.value)
        list[1].push(word.value.trim());
    word.value = '';
    renderList1(list[1]);
}

function remove1(e) {
    console.log("del");
    if (list[1].length) {
        list[1].splice(e.target.value, 1);
        renderList1(list[1]);
    }
}

function clearList1() {
    console.log("del-all");
    if (list[1].length) {
        list[1] = [];
        renderList1(list[1]);
    }
}

document.getElementById("b2").addEventListener("click", add2);
document.getElementById("c2").addEventListener("click", clearList2);
document.getElementById("ul2").addEventListener("click", remove2);

function renderList2(lst) {
    let lt = "";
    for (let i = 0; i < lst.length; i++) {
        lt += `<li value="${i}" >${lst[i]}</li>`;
    }
    if (lt) document.getElementById("ul2").innerHTML = lt;
    else document.getElementById("ul2").innerHTML = "Nothing Added Yet";
}

function add2() {
    word = document.getElementById("w2");
    console.log(list[2]);
    if (word.value)
        list[2].push(word.value.trim());
    word.value = '';
    renderList2(list[2]);
}

function remove2(e) {
    console.log("del");
    if (list[2].length) {
        list[2].splice(e.target.value, 1);
        renderList2(list[2]);
    }
}

function clearList2() {
    console.log("del-all");
    if (list[2].length) {
        list[2] = [];
        renderList2(list[2]);
    }
}


// document.getElementById("messForm").addEventListener('submit',(e)=>{
//     e.preventDefault();
//     console.log('form submitted');
//     let connection = document.getElementById('connection').value
//     ipcRenderer.send("runexefile",[connection]);
//     ipcRenderer.on('ver', (event, arg) => {
//         console.log("exe file started");
//     })
//     ipcRenderer.on('clo', (event, arg) => {
//         console.log(arg);
//     })
// });