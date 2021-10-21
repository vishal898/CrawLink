const {
    ipcRenderer
} = require('electron');

document.querySelector('a').addEventListener('click', (e) => {
    e.preventDefault()
    let p = document.querySelector('a').getAttribute("href");
    console.log(p);
    // setInterval(()=>{
    ipcRenderer.send("renderPage", [{
        page: p
    }]);
    // },10000);
});

document.getElementById("submit").addEventListener('click', (e) => {
    e.preventDefault();
    console.log('form submitted');
    let conns = [];
    let comps = [];
    let locs = [];
    for (let i = 1; i <= 3; i++) {
        if (document.getElementById(`${i}`).checked) {
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
    ipcRenderer.send("runexefile", [conns, locs, comps]);
    ipcRenderer.on('ver', (event, arg) => {
        console.log("exe file started");
        // add row to table

        // document.getElementById("submit").addEventListener('click', (e) => {

            let down = document.createElement("a");
            down.href = "sendMessToPeopleOld.csv";
            down.innerHTML = "Download";
            down.type = "text/csv";
            down.download = "sendMessToPeopleOld.csv";
            document.querySelector('.table-wrapper').appendChild(down);

            let table = document.createElement('table');
            let thead = document.createElement('thead');
            let tbody = document.createElement('tbody');
            table.appendChild(thead);
            table.appendChild(tbody);
            // Adding the entire table to the body tag
            document.querySelector('.table-wrapper').appendChild(table);

            // add heading to table 
            let row_1 = document.createElement('tr');
            let heading_1 = document.createElement('th');
            heading_1.innerHTML = "No.";
            let heading_2 = document.createElement('th');
            heading_2.innerHTML = "Name";
            let heading_3 = document.createElement('th');
            heading_3.innerHTML = "Profile Link";
            row_1.appendChild(heading_1);
            row_1.appendChild(heading_2);
            row_1.appendChild(heading_3);
            thead.appendChild(row_1);


            // add download csv file button 

            // read csv file 

            const csvFilePath = 'sendMessToPeopleOld.csv'
            ipcRenderer.send('readCsvFile', [csvFilePath]);
            ipcRenderer.on('tableData', (event, arg) => {
                console.log("got table data");
                console.log(arg);
                arg.forEach((row, index) => {
                    let row_2 = document.createElement('tr');
                    let row_2_data_1 = document.createElement('td');
                    row_2_data_1.innerHTML = index + 1;
                    let row_2_data_2 = document.createElement('td');
                    row_2_data_2.innerHTML = row.Name;
                    let row_2_data_3 = document.createElement('td');
                    row_2_data_3.innerHTML = row.Email;
                    row_2.appendChild(row_2_data_1);
                    row_2.appendChild(row_2_data_2);
                    row_2.appendChild(row_2_data_3);
                    tbody.appendChild(row_2);

                    // tbody.appendChild(`<tr><th>${index}<th><th>${row.Name}<th><th>${row.Email}<th></tr>`);
                });

            })


            // let myTbody = document.querySelector("table>tbody");
            // let newRow = myTbody.insertRow();
            // newRow.insertCell().append("New data");
            // newRow.insertCell().append("New data");
        // });

    })
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
        lt += `<li class="tag" value="${i}" >${lst[i]}</li>`;
    }
    if (lt) document.getElementById("ul1").innerHTML = lt;
    // else document.getElementById("ul1").innerHTML = "Nothing Added Yet";
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
        lt += `<li class="tag" value="${i}" >${lst[i]}</li>`;
    }
    if (lt) document.getElementById("ul2").innerHTML = lt;
   // else document.getElementById("ul2").innerHTML = "Nothing Added Yet";
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