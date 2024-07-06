C R A W L E R v2

by: github.com/pxcs - Sulaiman
------------

**Crawler_v2** is a ( Remote access Trojan ) that gives the server/attacker full remote access to the user's command-line interpreter (cmd.exe). They are allowed to execute commands silently without the src/client/Crawler_v2 noticing. The server/attacker is also given the ability to download and execute files on the src/client/Crawler_v2's computer. This is also a silent and hidden process. Like most Remote Access Trojans, this download and execution ability helps distribute viruses and other pieces of malware.

This malware is distributed simply by running *Crawler_v2.exe*. This file name can be changed to whatever. There is no restriction. When run, it searches for the first two arguments (IP & Port). If neither is provided, the program doesn't run. With that being said, make sure you provide the server's IP and Port in the command-line arguments.

Bot && RCA features

- Remote command execution 
- Silent background process
- Download and run file (Hidden)
- Safe Mode startup
- Will automatically connect to the server
- Data sent and received is encrypted (substitution cipher)
- Files are hidden
- Installed Antivirus shown to server
- Easily spread malware through download feature
- Startup info doesn't show in msconfig or other startup checking programs like CCleaner
- Disable Task Manager

When starting the server, it will prompt for you a listening port. This is the port that you need to use in the command-line for Crawler_v2.exe. Once you provide the port, your server information will be provided and the menu will be down. The IP address provided is your external IP. With that being said, unless the src/client/Crawler_v2 is actively looking and tracking open connections, it will probably be smart to run this server under a remote location if you want to stay anonymous. If this does not interest you, simply renaming Crawler_v2.exe and/or changing the assembly information using a tool will likely fool the src/client/Crawler_v2.

**Note**: This project was only made for education purposes and research only, thankyou for all the supports and sources codes