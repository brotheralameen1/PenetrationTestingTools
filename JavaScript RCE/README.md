This tool is used to test for the presence of an arbitrary code execution within the ua_parser_js endpoint within a Web Application System. 

The first folder called test has the program required to test for the vulnerable endpoint to make sure the endpoint is vulnerable. The second folder called RCE has the code required to upload a reverse shell to the target vulnerable system which can be used after confirming the vulnerability from the first code. 

NOTE: Although the ua_parser_js commonly has CVE's tied to DOS (Denial of Service) attacks, it even has vulnerable code tied to performing Remote Code Execution.

CVE's tied to ua_parser_js:

CVE-2022-25927 CVE-2021-27292 CVE-2020-7733 CVE-2020-7793 (All which are used for Denial of Service Attacks)

This tool can be helpful when it comes to performing your bug hunting and bug bounty programs. Please note that hacking is illegal, so please use this in a system you are permitted to test on. Don't use this for any unauthorized purposes.
