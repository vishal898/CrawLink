const {app,BrowserWindow,ipcMain} = require('electron');
const path = require('path');
const {contextIsolated} = require('process');
const { remote } = require('electron')

const Cred = require('electron-store');
cred = new Cred();


// set key and value pair to use it later 
ipcMain.on('setValue', (event, [key, value]) => {
  console.warn(key);
  console.warn(value);
  cred.set(key, value);
});
// get the value of key 
ipcMain.on('getValue', (event, [key, value]) => {
  cred.get(key, value);
});

// run the exe file 

ipcMain.on("runexefile", (event, args) => {
  args.unshift(cred.get('password'));
  args.unshift(cred.get('username'));
  console.warn(args);
  const python = require("child_process").execFile(require('path').normalize('./py/sendMessToPeople.exe'), args, (err, data) => {
    if (err) {
      mainWindow.webContents.send('clo', err);
      return
    } else mainWindow.webContents.send('clo', data);
  });
  
  event.reply('ver', 'started');
})

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
  
  // if(cred.get('username')===null || cred.get('password')===null){
  mainWindow.loadFile(path.join(__dirname, 'login/login.html'));


  ipcMain.on("renRam", (event, args) => {
    console.log('rendered Random.html');
    // mainWindow.loadFile(path.join(__dirname,'random.html'));
    mainWindow.loadFile(path.join(__dirname,'home/home.html'));
    // mainWindow.reload();
  });
  // }
  // else{
  //     console.log('rendered Random.html');
  //     // mainWindow.loadFile(path.join(__dirname,'random.html'));
  //     mainWindow.loadFile(path.join(__dirname,'random/random.html'));
  //     // mainWindow.reload();
  // }
  
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