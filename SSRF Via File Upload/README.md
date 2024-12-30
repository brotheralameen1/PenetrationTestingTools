This program contains XML Markup Language Code saved in the form of a .svg file that can be used to test for SSRF (Server-Side Request Forgery) Vulnerabilities within a Web Application System with a File Upload Functionality. 

Please note that this file is specifically used for Penetration Testing, Web Application Security, Security Research and Ethical Hacking, use of this file in any manner that's unauthorized is strictly prohibited by international law. Obtain permissions before using this file; I will not be responsible for your misuse of this file. You have been warned.

To use this file:

1. Edit the file using any kind of text editor
2. Change the BACKLINK_URL to any URL that can send back information to you (You can use Burp Suite Collaborator if you have Burp Suite Professional or you can use interactsh by ProjectDiscovery, which is also a good tool to test for SSRF Vulnerabilities and has the same functionality as Burp Suite Collaborator).
3. Save the file
4. Upload the file to the server with a file upload
5. Check for any requests being sent back from the remote server to confirm that it's vulnerable to SSRF.

You can also change and save the file as other file formats. For example, if you're testing SSRF in a File Upload Functionality that supports PNG and JPEG Files. You can edit the SVG File and use the 'Save As' Functionality to save the it as PNG or JPEG then upload after changing the "BACKLINK_URL" and saving the file.
