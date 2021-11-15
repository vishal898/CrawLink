const {app,BrowserWindow,ipcMain,Notification} = require('electron');
const path = require('path');
const {contextIsolated} = require('process');
const { remote } = require('electron');
const fs = require('fs');
const csv = require('papaparse');

const Cred = require('electron-store');
cred = new Cred();


// set key and value pair to use it later 
ipcMain.on('setValue', (event, [key, value]) => {
  cred.set(key, value);
});
// get the value of key 
ipcMain.on('getValue', (event, [key, value]) => {
  cred.get(key, value);
});

// run the exe file 

// ipcMain.on("runexefile", (event, args) => {
//   args.unshift(cred.get('password'));
//   args.unshift(cred.get('username'));
//   console.warn(args);
//   const python = require("child_process").execFile(require('path').normalize('./py/sendMessToPeopleOld.exe'), args, (err, data) => {
//     if (err) {
//       console.warn(err);
//     }else{
//       console.warn(data);
//     }
//       // mainWindow.webContents.send('clo', err);
//   });
//   python.on('exit',()=>{
//     event.reply('filltable', 'started');
//   });
// });

ipcMain.on("runexefile", (event, args) => {
  let path = args[0];
  console.warn(path);
  args.shift();
  args.unshift(cred.get('password'));
  args.unshift(cred.get('username'));
  console.warn(args);
  const python = require("child_process").execFile(require('path').normalize(`${path}`), args, (err, data) => {
    if (err) {
      console.warn(err);
    }else{
      console.warn(data);
    }
      // mainWindow.webContents.send('clo', err);
  });
  python.on('spawn',()=>{
    console.warn('script started');
    new Notification({
      title:"Script Started",
      body:"Selenium script has started",
    }).show();
  });
  python.on('exit',()=>{
    event.reply('filltable', 'started');
  });
  
});

// Handle creating/removing shortcuts on Windows when installing/uninstalling.
if (require('electron-squirrel-startup')) { // eslint-disable-line global-require
  app.quit();
}

const createWindow = () => {
  // Create the browser window.
  const mainWindow = new BrowserWindow({
    width: 800,
    height: 600,
    webPreferences: {
      nodeIntegration: true,
      contextIsolation: false
    }
  });
  
  mainWindow.maximize();

  // and load the index.html of the app.
  console.warn(cred.get('username'));
  console.warn(cred.get('password'));
  
  if(cred.get('username')==="" || cred.get('password')==="") mainWindow.loadFile(path.join(__dirname, 'login/login.html'));
  else mainWindow.loadFile(path.join(__dirname,'home/home.html'));

  // ipcMain.on("renRam", (event, args) => {
  //   // console.warn(`rendered ${args.page}`);
  //   // mainWindow.loadFile(path.join(__dirname,'connection.html'));
  //   mainWindow.loadFile(path.join(__dirname,'withdraw/withdraw.html'));
  //   // mainWindow.reload();
  // });
  // }
  // else{
  //     console.warm('rendered Connection.html');
  //     // mainWindow.loadFile(path.join(__dirname,'connection.html'));
  //     mainWindow.loadFile(path.join(__dirname,'connection/connection.html'));
  //     // mainWindow.reload();
  // }

  ipcMain.on("renderPage", (event, args) => {
    // console.warn(`rendered ${args.page}`);
    // mainWindow.loadFile(path.join(__dirname,'connection.html'));
    mainWindow.loadFile(path.join(__dirname,args[0].page));
    // mainWindow.reload();
  });
  
  ipcMain.on("readCsvFile", (event, args) => {
    console.warn('Csv started reading')
    // console.warn(args[0]);
    const file = fs.createReadStream(args[0]);
    let csvData=[];
    csv.parse(file, {
      header: true,
      step: function(result) {
        // console.warn(result.data);
        csvData.push(result.data);
      },
      complete: function(results, file) {
          console.warn('Complete', csvData, 'records.'); 
          event.reply('tableData', csvData);
      }
    });
  });

  // Open the DevTools.
  // mainWindow.webContents.openDevTools();
};

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (BrowserWindow.getAllWindows().length === 0) {
    createWindow();
  }
});



// ipcMain.on("msg", (event, args) => {
//   console.warn(args);
//   const python = require("child_process").execFile(require('path').normalize('./py/LinkedinBot.exe'), args, (err, data) => {
//     console.warn(args);
//     if (err) {
//       mainWindow.webContents.send('clo', err);
//       return
//     } else mainWindow.webContents.send('clo', data);
//   });
//   event.reply('rev', 'started');
// })