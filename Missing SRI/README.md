This is a tool that you can use to test websites for Missing SRI Vulnerability. Missing SRI is common in websites with JavaScript misconfigurations that don't have an integrity hash set on them, which then allows malicious payloads to be injected by an attacker to the Web Application System.

NB: Hacking is illegal. Please obtain explicit permission from the owners before attempting to use this script. It's always good to adhere to performing White Hat Activities. This script is good for researchers who want to use it to perform Bug Bounty Hunting and for those who want to confirm that Missing RSI isn't there in their Web Applications of the endpoint they suspect the potential vulnerability is present.

To use this script:

1. Open the HTML File and direct it to the URL of the payload where it states that you should edit. Do not change the name of the endpoint. Just copy the entire vulnerable URI and paste it there then save.
2. Change the payload name to the same file name of the endpoint you're attacking.
3. Run the Injector on your browser.

You should get a dialog box opening to confirm the vulnerability. If, however, you find a problem with using the script and still want to test to confirm the Missing RSI Vulnerability, follow these steps:

1. Open Inspect Element and search for the word "Integrity" in the HTML (Without quotes)
2. If it's not there and tools like nuclei identified it to be a potential vulnerability tied to Missing RSI then you can confirm this with the last step
3. Use your Browser Debugger Console to run this script: alert("This is malicious script!") and if you see a dialog box then you've confirmed the presence of the vulnerability.

4. Please use this tool responsibly; I will not be responsible for any harm you perform using this tool. 
