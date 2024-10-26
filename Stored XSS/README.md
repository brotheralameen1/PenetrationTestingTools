This is a file used to check for Stored XSS in a Web Application's Upload System for files that allow PDFs. This file works when a Web Application doesn't have the ability to filter malicious code from uploaded PDF Documents and only checks the type of document uploaded as PDF which it allows into the system, then executes the malicious embedded JavaScript File that's injected into the file to execute the stored XSS vulnerability everytime someone opens the endpoint link to access the file.

NOTE: This file is to be used for educational purposes only. This file is used to help Ethical Hackers and Penetration Testers ease their work of finding vulnerabilities in a Vulnerable Web Application System so they can report it to be patched. Please don't use this knowledge for ill intent or to attack people, I will not be responsible for any harms or attacks done by you using this file.

To use this file, simply follow these steps:

1. Clone the repository
2. Navigate to: https://github.com/cornerpirate/JS2PDFInjector/ and clone the repository
3. Copy the JS and PDF file from this the cloned directory for Stored XSS and add it to the directory of where you cloned the Injector
4. Use Java to execute the Injector as shown in the above repository
5. Use the poisoned PDF Document to upload the PDF with the malicious payload online to the Vulnerable Web Application System and wait for the dialog box to appear to confirm stored XSS. If you don't get a dialog box then the Web Application isn't vulnerable.

Or

1. Clone this repository
2. Take the Injected XSS Document
3. Upload it to a Web Server you suspect to have an upload system that doesn't filter any malicious code and accepts only PDF Files, filters for only files as PDFs.
4. Check for a dialog box and confirm XSS

Finally, once you confirm the XSS Vulnerability. You can then report it to the appropriate Bug Bounty Program.
