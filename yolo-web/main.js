const { app, BrowserWindow } = require('electron');
const { spawn } = require('child_process');
const path = require('path');
const http = require('http');

let streamlitProcess = null;
let mainWindow = null;

function startStreamlit() {
  const pythonPath = path.join(__dirname, '.venv', 'Scripts', 'python.exe');
  const appPath = path.join(__dirname, 'app.py');

  streamlitProcess = spawn(pythonPath, [
    '-m', 'streamlit', 'run', appPath,
    '--server.headless=true',
    '--server.port=8501'
  ], {
    cwd: __dirname,
    stdio: 'ignore'
  });

  streamlitProcess.on('error', (err) => {
    console.error('启动 Streamlit 失败：', err);
  });
}

function waitForStreamlit(callback, retries = 60) {
  http.get('http://localhost:8501', () => {
    callback();
  }).on('error', () => {
    if (retries > 0) {
      setTimeout(() => waitForStreamlit(callback, retries - 1), 500);
    }
  });
}

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 1000,
    height: 800,
    webPreferences: {
      nodeIntegration: false,
      contextIsolation: true
    }
  });
  mainWindow.loadURL('http://localhost:8501');
}

app.whenReady().then(() => {
  startStreamlit();
  waitForStreamlit(() => createWindow());
});

function killStreamlit() {
  if (streamlitProcess) {
    streamlitProcess.kill();
    streamlitProcess = null;
  }
}

app.on('window-all-closed', () => {
  killStreamlit();
  if (process.platform !== 'darwin') app.quit();
});

app.on('before-quit', killStreamlit);