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
// const path = require('path');
// const bgImgPath = path.join(__dirname, '../bglink.png');
// console.log(__dirname);

// document.body.style.backgroundImage ="url("+bgImgPath+")";

let cnt,br,newListItem;


// add row to table
function sub (event)  {
    event.preventDefault();
    document.getElementById("submit").disabled = true;
    console.log('form submitted');
    document.getElementById("count").required = true
    cnt=document.getElementById("count").value;
    if(cnt>25)
    {
        cnt = 25;
        document.getElementById("count").value = cnt;
    }
    if(cnt<1)
    {
        cnt = 1;
        document.getElementById("count").value = cnt;
    }
    console.log(cnt);

    ipcRenderer.send("runexefile", ['./py/notifLike.exe',cnt]);
    let down = document.createElement("a");
    down.href =  "withdraw.csv";
    down.innerHTML ="Download";
    down.type = "text/csv";
    down.download = "withdraw.csv";
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
    heading_2.innerHTML = "Name";
    let heading_3 = document.createElement('th');
    heading_3.innerHTML = "Profile Link";
    row_1.appendChild(heading_1);
    row_1.appendChild(heading_2);
    row_1.appendChild(heading_3);
    thead.appendChild(row_1);


    // add download csv file button 

    // read csv file 

    const csvFilePath = 'withdraw.csv'
    ipcRenderer.send('readCsvFile',[csvFilePath]);
    ipcRenderer.on('tableData', (event, arg) => {
        console.log("got table data");
        console.log(arg);
        arg.forEach((row,index)=>{
            let row_2 = document.createElement('tr');
            let row_2_data_1 = document.createElement('td');
            row_2_data_1.innerHTML = index+1;
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
    });
    // ipcRenderer.on('clo', (event, arg) => {
    //     console.log(arg);
    // })
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


