The purpose of this file is to help penetration testers and ethical hackers to test for Cross Origin Resource Sharing Vulnerability on their Web Application System or during Bug Bounties. Please don't use this tool for anything irresponsible. Hacking is illegal, please obtain necessary permissions or test this on your own lab environment or an environment you're permitted to test this on. You have been warned.

This file contians a JavaScript Code that logs an API Key of an Admin Account that has a Web Server proven to have a CORS Vulnerability. You may modify this file to your own advantage to further help you in your exercise and exploits to help you in your Bug Bounties or testing in your own Web Applications. Don't misuse this tool for anything irresponsible.

To use this tool, do the following:

1. Edit the HTML file to include the vulnerable endpoint and host, configure ngrok and setup the ngrok URL as well (If using a web hosting server, configure it to use that instead of ngrok)
2. Save the file and upload it to a web server, hosting or use ngrok to tunnel it
3. Attempt some Social Engineering with the Admin to make him open the link
4. The API key should be returned back to you once the Admin opens the link and should also display on their screen

NOTE: In most cases, CORS can be reported if RCE can be performed, but in cases where Social Engineering is involved, it's highly not recommended to take part of Bug Bounty Program and such attacks are mostly out of scope as they involve exploiting human weaknesses rather than actually hacking the Web Application itself without any kind of Social Engineering. It's highly recommended that if you find CORS and want to do this for a Bug Bounty that you find an endpoint that isn't really involving Social Engineering Attacks. In some cases where a RCE can be exploited using this method and this HTML Document to upload a reverse shell (You can modify the code however you want to do this), you may be able to get a bounty and have this reported to HackerOne. Nonetheless, this would require testing other CORS headers on your vulnerable endpoint such as Origin Header. 
