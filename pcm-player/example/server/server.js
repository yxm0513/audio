const WebSocket = require('ws');
const fs = require('fs');

const pcm_file = './16bit-8000.raw';
let interval = 0,
    sampleRate = 8000,
    bytePerSample = 2,
    channels = 2,
    bytesChunk = (sampleRate * bytePerSample * channels),
    offset = 0,
    pcmData,
    wss;

fs.readFile(pcm_file, (err, data) => {
    if (err) throw err;
    pcmData = data;
    openSocket();
});


function openSocket() {
  wss = new WebSocket.Server({ port: 8080 });
  console.log('Server ready...');
  wss.on('connection', function connection(ws) {
        console.log('Socket connected. sending data...');
        if (interval) {
            clearInterval(interval);
        }
        interval = setInterval(function() {
          sendData();
        }, 500);
  });
}

function sendData() {
    let payload;
    if (offset >= pcmData.length) {
       clearInterval(interval);
       offset = 0;
       return;
    }
    
    payload = pcmData.subarray(offset, (offset + bytesChunk));
    offset += bytesChunk;
    wss.clients.forEach(function each(client) {
      if (client.readyState === WebSocket.OPEN) {
          client.send(payload);
      }
    });
}