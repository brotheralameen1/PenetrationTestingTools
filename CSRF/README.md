This file is meant to be used by White Hat Hackers and Penetration Testers who perform Bug Bounty and Vulnerability Disclosure Programs to perform Ethical Hacking, I will not by any means be responsible for your misuse of this tool. Please be sure to use this tool wisely in your works.

This tool is basically a form that is used to send CSRF Queries to a Web Application System. You can modify this form in your behalf to suit your need for the site you're testing this on whether it be for a BBP, VDP or to test on your own lab environment or your own website. Please obtain necessary permissions before using this tool on anyones else and do remember to perform your actions ethically.

To use this form, simply:

1. Clone this repository
2. Edit the HTML File to include the URL of the endpoint vulnerable to CSRF
3. Edit the form to your desired need to send queries to the remote vulnerable endpoint
4. Save the file
5. Open the file on the browser and use burpsuite to check the HTTP Proxy History Section to check the response received from attempting the CSRF Attack

If you get a 200 OK with the form data being submitted successfully and the form being filled as accordingly then the site is vulnerable to CSRF and you can report this issue to HackerOne or other BBP or VDP Program you're using to test and report the vulnerabilities.
