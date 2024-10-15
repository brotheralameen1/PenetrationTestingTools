This tool is used to test for an open redirect vulnerability on a Web Application System. Please use this tool wisely. 

I will not be responsible for any harm or misuse of this tool. This tool has been specifically coded to test for the vulnerability and is meant to be used by cybersecurity analyst and security researchers such as bug bounty hunters who report to HackerOne and hasn't been coded with anything malicious to cause destruction to a system.

NB: Hacking is illegal. Please obtain explicit permissions from the owners of where you decide to test this tool before testing it and use this tool ethically.

How to use it?

Open the Python Script using a Text Editor and change the domains as shown at the bottom of the script then run the tool:

python3 test.py

If you receive a response "Website is vulnerable" with the site it's redirected to then you've confirmed Open Redirect Vulnerability. Nonetheless, if you still doubt the tool, you can try perform the Open Redirect manually on your browser by adding a link to redirect to at the end of the endpoint that is vulnerable and checking if it redirects. In some cases, the WAF could be blocking the entry as well, so be sure to use filters to filer the URL to bypass the WAF.

Good luck.
