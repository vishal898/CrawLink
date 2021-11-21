const { ipcRenderer } = require('electron');
const path = require('path');

document.querySelector('a').addEventListener('click',(e)=>{
    e.preventDefault()
    let p = document.querySelector('a').getAttribute("href");
    console.log(p);
    // setInterval(()=>{
        ipcRenderer.send("renderPage",[{page:p}]);
    // },10000);
});
let cnt;

document.getElementById("submit").addEventListener('click',(e)=>{
    e.preventDefault();
    console.log('form submitted');
    document.getElementById("submit").disabled = true;
    document.getElementById("count").required = true
    cnt=document.getElementById("count").value;
    console.log(cnt);
    
    if(cnt<=25)
    {
        console.log(cnt);
        //ipcRenderer.send("count",cnt);
    }
    ipcRenderer.send("runexefile", ['./py/accept.exe',cnt]);
    ipcRenderer.on('filltable', (event, arg) => {
        console.log("exe file execution is over");
        const title = "Table is Created";
        const bodyText = "Table is Created";
        const notification = new Notification(title,{
        body:bodyText,
        });
        let down = document.createElement("a");
        down.href =  "accept.csv";
        down.innerHTML ="Download";
        down.type = "text/csv";
        down.download = "accept.csv";
        down.style.color = "white";
        down.style.textDecoration = "inherit";
        let btn = document.createElement("button");
        btn.className = "btn btn-success";
        btn.style.marginBottom = "25px";
        btn.appendChild(down);
        document.querySelector('.table-wrapper').appendChild(btn);
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
        heading_2.innerHTML = "Profile Link";
        row_1.appendChild(heading_1);
        row_1.appendChild(heading_2);
        thead.appendChild(row_1);


        // add download csv file button 

        // read csv file 

        // const csvFilePath = 'connection/sendMessToPeopleOld.csv';
        const csvFilePath = path.join(__dirname, 'accept.csv');
        ipcRenderer.send('readCsvFile', [csvFilePath]);
        ipcRenderer.on('tableData', (event, arg) => {
            console.log("got table data");
            console.log(arg);
            arg.forEach((row, index) => {
                let row_2 = document.createElement('tr');
                let row_2_data_1 = document.createElement('td');
                row_2_data_1.innerHTML = index + 1;
                let row_2_data_2 = document.createElement('td');
                row_2_data_2.innerHTML = row.Link;
                row_2.appendChild(row_2_data_1);
                row_2.appendChild(row_2_data_2);
                tbody.appendChild(row_2);
                // tbody.appendChild(`<tr><th>${index}<th><th>${row.Name}<th><th>${row.Email}<th></tr>`);
            });
        });
    });

    
  
});

