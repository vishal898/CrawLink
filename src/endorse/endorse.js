const {
    ipcRenderer
} = require('electron');
const path = require('path');

document.querySelector('a').addEventListener('click', (e) => {
    e.preventDefault();
    let p = document.querySelector('a').getAttribute("href");
    console.log(p);
    // setInterval(()=>{
    ipcRenderer.send("renderPage", [{
        page: p
    }]);
    // },10000);
});

let list = [
    [],
    [],
]
// document.getElementById("txtFileSubmit").addEventListener('click',()=>{
//     console.log('file submit button clicked');
//     document.getElementById("txtFile").click();
// });

document.getElementById("txtFileSubmit").addEventListener('click',()=>{
    console.log('file button clicked');
    // if(document.getElementById("txtFile").value){
    //     console.log(document.getElementById("txtFile"));
    // }
    ipcRenderer.send('openFile');
    ipcRenderer.on('fileData', (event, datas) => { 
        console.log(datas);
        document.getElementById("fileSpan").innerHTML = path.parse(datas[1]).base;
        let data = datas[0];
        data = data.trim().split('\r\n');
        data = data.join();
        data = data.split(' ');
        data = data.join();
        data = data.split(',');
        data = data.join();
        list[1] = data.trim().split(',');
        let tempList = list[1].filter((ele)=>{
            return ele.length >1;
        });
        list[1]=tempList;
        console.log(list[1]);
        renderList1(list[1]);
        // data = data.replace('\n',' ');
        // console.log(data);    
        // list[1] = data.trim().split('\r',' ','\r\n');
        // list[1] = data.trim().split();
        // console.log(list[1]);
        // data = list[1].join();
        // console.log(data);
    });
});

function sub (event)  {
    event.preventDefault();
    document.getElementById("submit").disabled = true;
    console.log('form submitted');

    let profLinks = [];
    document.getElementById("ul1").querySelectorAll('li').forEach((item, index) => {
        profLinks.push(item.innerText);
    });

    profLinks = JSON.stringify(profLinks);
    console.log(profLinks);

    ipcRenderer.send("runexefile", ['./py/autoEndorser.exe',profLinks]);
    ipcRenderer.on('filltable', (event, arg) => {
        console.log("exe file execution is over");
        const title = "Endorsed successfully";
        const bodyText = "All your connections are endorsed successfully.";
        const notification = new Notification(title,{
            body:bodyText,
        });
    });
} 

document.getElementById("refresh",()=>{
    let p = document.querySelector('a').getAttribute("href");
    console.log(p);
    // setInterval(()=>{
    ipcRenderer.send("renderPage", [{
        page: p
    }]);
});


document.getElementById("submit").addEventListener('click',sub );


document.getElementById("b1").addEventListener("click", add1);
document.getElementById("c1").addEventListener("click", clearList1);
document.getElementById("ul1").addEventListener("click", remove1);

function renderList1(lst) {
    let lt = "";
    for (let i = 0; i < lst.length; i++) {
        lt += `<li class="tag" value="${i}" >${lst[i]}</li>`;
    }
    if (lt) document.getElementById("ul1").innerHTML = lt;
    else document.getElementById("ul1").innerHTML = "";
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



// // add row to table

// document.getElementById("submit").addEventListener('click',(e)=>{

//     let down = document.createElement("a");
//     down.href = "sendMessToPeopleOld.csv";
//     down.innerHTML ="Download";
//     down.type = "text/csv";
//     down.download = "sendMessToPeopleOld.csv";
//     document.querySelector('.table-wrapper').appendChild(down);

//     let table = document.createElement('table');
//     let thead = document.createElement('thead');
//     let tbody = document.createElement('tbody');
//     table.appendChild(thead);
//     table.appendChild(tbody);
//     // Adding the entire table to the body tag
//     document.querySelector('.table-wrapper').appendChild(table);

//     // add heading to table 
//     let row_1 = document.createElement('tr');
//     let heading_1 = document.createElement('th');
//     heading_1.innerHTML = "No.";
//     let heading_2 = document.createElement('th');
//     heading_2.innerHTML = "Name";
//     let heading_3 = document.createElement('th');
//     heading_3.innerHTML = "Profile Link";
//     row_1.appendChild(heading_1);
//     row_1.appendChild(heading_2);
//     row_1.appendChild(heading_3);
//     thead.appendChild(row_1);


//     // add download csv file button 

//     // read csv file 

//     const csvFilePath = 'sendMessToPeopleOld.csv'
//     ipcRenderer.send('readCsvFile',[csvFilePath]);
//     ipcRenderer.on('tableData', (event, arg) => {
//         console.log("got table data");
//         console.log(arg);
//         arg.forEach((row,index)=>{
//             let row_2 = document.createElement('tr');
//             let row_2_data_1 = document.createElement('td');
//             row_2_data_1.innerHTML = index+1;
//             let row_2_data_2 = document.createElement('td');
//             row_2_data_2.innerHTML = row.Name;
//             let row_2_data_3 = document.createElement('td');
//             row_2_data_3.innerHTML = row.Email;
//             row_2.appendChild(row_2_data_1);
//             row_2.appendChild(row_2_data_2);
//             row_2.appendChild(row_2_data_3);
//             tbody.appendChild(row_2);

//             // tbody.appendChild(`<tr><th>${index}<th><th>${row.Name}<th><th>${row.Email}<th></tr>`);
//         });

//     })


//     // let myTbody = document.querySelector("table>tbody");
//     // let newRow = myTbody.insertRow();
//     // newRow.insertCell().append("New data");
//     // newRow.insertCell().append("New data");
// });











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