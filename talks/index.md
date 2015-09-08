---
layout: page
title: Talks at Hack.lu 2015
excerpt: "Talks at Hack.lu 2015"
modified: 2015-05-14T19:44:38.564948-04:00
image:
  feature: talks-s.jpg
  credit: Alexandre Dulaunoy
  creditlink: https://www.flickr.com/photos/adulau/5129843510
---

Talks, workshops and presentations will be published after the [Call for Papers]({{ site.url }}/blog/Call-for-Paper/). Feel free to submit your presentations or researches to be part of the 2015 edition.

Talks
=====

Keynote - Unpatchable: Living with a Vulnerable Implanted Device
----------------------------------------------------------------
by Marie Moe

My life depends on the functioning of a medical device, a pacemaker that generates each and every beat of my heart. This computer inside of me may fail due to hardware and software issues, due to misconfigurations or network-connectivity.

Yes, you read that correctly. The pacemaker has a wireless interface for remote monitoring and I am forced to become a human part of the Internet-of-Things. As a seasoned security-professional I am worried about my heart's attack surface.

This talk will be focused on the problem that we have these life critical devices with vulnerabilities that can't easily be patched without performing surgery on patients, my personal experience with being the host of such a device, and how the hacker community can proceed to work with the vendors to secure the devices.


Bio: Marie Moe
--------------

Marie Moe is passionate about incident handling and information sharing, she cares about public safety and securing systems that may impact human lives, this is why she has joined the grassroots organisation “I Am The Cavalry". Marie is a research scientist at SINTEF ICT, and has a Ph. D. in information security. She has experience as a team leader at NorCERT, the Norwegian national CERT. Marie also teaches a class on incident management and contingency planning at Gjøvik University College in Norway. Marie loves to break crypto protocols, but gets angry when its in her own body.


Trusting Files Formats: Illusions or Reality?
---------------------------------------------
by Ange Albertini

What is our biggest fear when we double-click an icon, when our system opens an external file?
Being hacked! You know it, because this is what the medias would make their headlines about.

Crashing an app or your system is also a risk, but it's not that scary in comparison.

And besides... What else could happen? it's fine...

It's fine, because we always have the sweet illusion that by reading the specs of its file format, we'd get a clear understanding of what
that file is supposed to do.

As if... ;) Can we still trust file formats?

On top of that, while preservationists want to store reliably information for ever, infosec people are ready to ban a file format if it doesn't match
security standards...

Can we trust their future?

Bio: Ange Albertini
-------------------

Reverse engineering & visual documentations. [Corkami](https://github.com/corkami)

How Mobile Applications Are Redefining Information Controls Inside of Iran
--------------------------------------------------------------------------
by Mahsa Alimardani

As Internet users increasingly connect to the Internet through smartphones, this has transformed Iran’s Internet ecology towards an increasing reliance and production in apps. In Iran, a country that practises some of the most stringent censorship and surveillance techniques in the world has seen this transformation reshape the way the government implements information controls online. While applications with popular usage on browsers such as Facebook and Twitter remain blocked through their mobile applications, platforms that predominantly exist in app form such as WhatsApp, Viber, and Instagram remain unblocked in the country. This talk will look at how the government is counteracting these policies through various means, including local imitation apps, and new programs such as ‘intelligent filtering’, and the Revolutionary Guards' “Spider” program. Additionally, a discussion of how Iranian Internet users use these platforms, especially in reference to digital security awareness and practices will be included.

Bio: Mahsa Alimardani
---------------------

Mahsa Alimardani has been doing research and work on the politics of Iran’s Internet for the past four years. She is currently a graduate student at the University of Amsterdam, working as a researcher on digital activism in the Data J Lab. She also dabbles with editing, writing, and sometimes ranting about Iran as the Global Voices Iran editor.

Geek usages for your Fitbit Flex tracker
----------------------------------------
by Axelle Apvrille

Fitness Flex is a fitness wristband which records your fitness activity: walking, running - and also sleep efficiency.
Since prior infamous security and privacy issues - such as public web disclosure of sexual activity - Fitbit has made significant progress. While reverse engineering, we noticed trackers now use end to end encryption for their communications with Fitbit servers.
Is this good? or bad?
What happens if Fitbit servers are unreachable ? What can we possibly do with the wristband besides activity tracking?

I'll present two alternative geeky usages to your beloved fitness tracker.

Bio: Axelle Apvrille
--------------------

Anti-virus researcher with Fortinet, FortiGuard Labs.
The strange, advanded or unexpected non-desktop malware (e.g mobile, connected objects) get on my desk.

Key-Logger, Video, Mouse - How to turn your KVM into a raging key-logging monster
---------------------------------------------------------------------------------
by Yaniv Balmas, Lior Oppenheim

Key-Loggers are cool, really cool. It seems, however, that every conceivable aspect of key-logging has already been covered: from physical devices to hooking techniques. What possible innovation could be left in this field?
Well, that's what we used to think too. That is until we noticed that little grey box sitting there underneath a monitor, next to yesterday's dirty coffee cup. The little grey box that is most commonly known as 'KVM'.
The talk will tell the tale of our long journey to transform an innocent KVM into a raging key-logging monster.
We will safely guide you through the embedded wastelands, past unknown IC's, to explore uncharted serial protocols and unravel monstrous obfuscation techniques.
Walking along the misty firmware woods of 8051 assembly we will challenge ambiguous functions, and confront undebuggable environments.

Finally, we will present a live demo of our POC code and show you that air-gapped networks might not be as segregated as you imagined.
You will witness that malware code could actually reside outside your computer, persisting through reboots, wipes, formats, and even hardware replacements.
You might laugh, you might cry, but one thing is certain - you will never look at your KVM the same as before.

Bio: Yaniv Balmas
-----------------

Yaniv Balmas is a software engineer and a seasoned professional in the security field. He wrote his very first piece of code in BASIC on the new Commodore-64 he got for his 8th birthday. As a teenager, he spent his time looking for ways to hack computer games and break BBS software. This soon led to diving into more serious programming, and ultimately, the security field where he has been ever since. Yaniv is currently leading the malware research team at Check Point Software Technologies where he deals mainly with analyzing malware and vulnerability research.

Twitter: [@ynvb](https://www.twitter.com/ynvb)


Bio: Lior Oppenheim
-------------------

Lior Oppenheim is a vulnerability researcher in the Malware and Vulnerability Research group at Check Point Software Technologies. Oppenheim was trained and served in an elite technological unit performing security research in the IDF. In his spare time, he loves tap dancing, reversing, playing his guitar and pwning embedded devices.

Twitter: [@oppenheim1](https://www.twitter.com/oppenheim1)


Keys? Where we're going, we don't need keys
-------------------------------------------
by Damien Cauquil

Smartlocks are the new way of securing doors by replacing the old mechanical locks by new high-tech and connected locks, able to
communicate with other smart devices such as smartphones and computers.
Vendors argue that "key dematerialization" is the future of keys, where anybody would be able to give, control and revoke keys for one or
multiple locks by using his smartphone. No more physical keys needed for a better control, they say.

We'll go through the challenges of key dematerialization in the actual world, from technical challenges to real world implementations ... and failures.

Widespread smartlocks (and padlocks) are not so smart, and developers often fail at correctly implementing cryptographic algorithms (especially when the smartlock is advertised as using a strong AES-256 implementation), and of course security by obscurity is still used and broken when dealing with critical embedded systems.

During this talk, we're going to demonstrate some real world attacks on one of these smartlocks, from information leaks to "wireless lockpicking" through fuzzing.


Bio: Damien Cauquil
-------------------
Damien Cauquil is Head of Research at Sysdream, a French IT Security Company, and also an experienced reverse-engineer. He started reversing binaries at the age of 16, with some friends and a lot of coke and pizzas, using old tools such as Win32dasm or Procdump.  He is now playing with electronics, embedded systems and his soldering iron.

He is a regular speaker at the French Nuit du Hack conference, but also spoke at other security conferences such as Hack In Paris, 29C3 and CCCamp 2015.


Draw me a Local Kernel Debugger
-------------------------------
by Samuel Chevet and Clément Rouault

Local Kernel Debugging is the ability to perform kernel-mode debugging on a
single computer. In other words, the debugger runs on the same computer
that is being debugged. Windows offers this functionality through windbg and kd
binaries which allow to read/write the kernel memory, perform in/out and access MSRs.

This presentation will explain how dbgengine (core of windbg) works: which APIs are
exposed and what it requires to work properly. We will show how to abuse it to
be able to perform Local Kernel Debugging in Python. Finally, we demonstrate its
interest throught use cases.

Bio: Samuel Chevet
------------------

Samuel Chevet is a security researcher currently working at Sogeti ESEC R&D.
His interests mainly lies in reverse engineering, vulnerability research and windows internals.

[@w4kfu](https://twitter.com/w4kfu)

Bio: Clement Rouault
--------------------

Clement Rouault is a security researcher currently working at Sogeti ESEC R&D.
Fervent user of Python he is interested in use, abuse and implementation of this language.
His research interests include reverse engineering and exploitation.

[@hakril](https://twitter.com/hakril)

Security of Virtual Desktop Infrastructures: from great concepts to bad surprises
---------------------------------------------------------------------------------
by Maxime Clementz, Simon Petitjean

Virtual Desktop Infrastructure hosts users' desktop environments on remote servers which are accessed over a network using a remote display protocol from specific client software or hardware such as Thin-client or Zero-client.
We encountered such solutions during pentests in high-security networks. Moreover, we had the opportunity to study one specific commercial implementation: we identified and exploited several flaws that allow taking over the whole infrastructure.
We've had some fun hacking this technology so we would like to share our experience by explaining our findings and giving tips to mitigate the critical vulnerabilities we found.
**SPOILER**: responsible disclosure is simultaneously launched with this paper submission. Of course, the content of our final presentation will depend on the outcome of the discussion with the editor.


Bio: Maxime Clementz & Simon Petitjean
--------------------------------------

Maxime ([@maxime\_tz](https://twitter.com/maxime_tz)) and Simon ([@simonpetitjean](https://twitter.com/simonpetitjean)) joined the Cyber Security Advisory team at PwC Luxembourg in 2012 and 2013, respectively. Their favourite activities and assignments are penetration tests, information security advisory and computer forensics. When they have the occasion to perform vulnerability research or Security R&D, they are always delighted to present their results (Hack.lu 2012, 2013 and now 2015).

Binary Constraint Solving with LLVM
-----------------------------------
by Sophia D'Antoine


This talk will show how to perform a full chain control flow attack against a complex, stand-alone application.
Specifically, how to use mcsema, llvm, and satisfiability solvers to discover a targeted execution path using side channel analysis. From this we show how to traverse this path to collect path constraints and solve for user input which would give us the desired output.
This process can then be applied to any targeted behavior in a program, from finding known vulnerability characteristics to simply supplying the correct input to a 'crackme' binary.

A demonstration will conclude the talk by solving an obfuscated 'crackme' challenge using the above described process as well as a mini 'competition' by running a pintool solver and a pysymemu solver against the same binary and comparing to see which gets the flag first.

Bio: Sophia D'Antoine
---------------------

Sophia D’Antoine is a security researcher at Trail of Bits and a recent graduate student from Rensselaer Polytechnic Institute. At RPI, her graduate research focuses on malicious applications of hardware side channels in virtualized environments. She has presented at RECon Montreal, Blackhat and Sec-t on this topic, specifically on exploiting out-of-order execution, a processor optimization, to create a side channel.
Presently, she is working with LLVM to automatically analyze, obfuscate, and transform execution paths. Additionally, she is merging concepts of hardware side channel vulnerabilities at this software level of execution. Through her involvement in RPISEC, she has taught security courses, competed in CTFs, and performed security consulting assessments.

Website: [sophia.re](http://www.sophia.re/)

Advances in Secure Messaging Protocols
--------------------------------------
by Frederic Jacobs

Along with the Snowden revelations, there's been a surge of interest in end-to-end security for messaging. This idea is nothing new, OTR and PGP have been around for some time but failed to get widespread adoption.

We discuss the desirable cryptographic properties of secure messaging protocols and show how they are achieved in practice in different protocols. We also show how multiple newcomers to the secure messaging space are reducing metadata trails and discuss impact it has on fighting abuse such as spam.

Bio: Frederic Jacobs
--------------------

Frederic Jacobs is discovering lattices and elliptic curves at the Swiss Institute of Technology by day and works on multiple applied cryptography projects by night. He is leading the development of Signal at Open Whisper Systems.

How not to build an electronic voting system
--------------------------------------------
by Quentin Kaiser

Back in 1994, Belgium was one of the first European country to push for the deployment of electronic voting systems. Thought at the time as a sign of Belgium stepping foot in the 21st century, the system stayed in use up to the latest European elections that took place in May 2014. As years passed, bugs got discovered, issues were raised, and public concern grew up to the point where the government was obliged by law to publish the source code of those systems. We jumped on the opportunity to audit the code in June 2014, a few days after the #bug2505 debacle.
By auditing the source code provided by the Ministry of Home Affairs, we found multiple vulnerabilities in the system that could easily be exploited by an attacker to tamper with the election process.

This presentation will cover all the Belgian election system components, from the different implementations of ballot boxes to the infrastructure responsible of counting each and every vote. Our ultimate goal is to cast a light on bad security practices we found in election management systems so it hopefully get fixed by the next election year.


Bio: Quentin Kaiser
-------------------

Quentin Kaiser is currently working as a Security Engineer, dealing with various tasks such as web and mobile applications penetration testing, social engineering engagements, and audits of network infrastructures. His interests gravitates around social engineering, open source intelligence, and Android security. During his studies he founded the first hackerspace in the Luxembourg province, located in Bastogne, Belgium: BHackspace.


Totally Spies!
--------------
by Marion Marschalek, Paul Rascagnères, Joan Calvet


In March 2014 a set of slides were leaked from the Communications Security Establishment Canada (CSEC), outlining operation SNOWGLOBE which involves a mysterious malware dubbed Babar that has been spotted spying on Canadian institutions as well as attacking institutions in Iran and other targets in the middle east. CSEC attributed the attacks "with moderate certainty" to a French intelligence agency.
The group behind Babar is now commonly referred to as "AnimalFarm" in antimalware industry, suggesting Babar was only a small piece of a much bigger puzzle. Since CSEC slides' publication, a group of valorous adventurers, animated by the thrill of understanding complex malware operations, has been relentlessly following SNOWGLOBE's trail. Along its path, this group found several pieces of AnimalFarm's arsenal, for example stealthy Casper, exotic Bunny and even big ears Babar itself. The newest heavy-weight actor on the list of miscreants is Dino, the espionage dinosaur.

This presentation aims to provide a global picture on SNOWGLOBE's operations and also delve into technical quirks of their malware. An assessment of the connection between their various piece of software will be given from a reverse engineer's perspective, and what technical hints regarding attribution can be found.

Bio: Marion Marschalek
----------------------

Marion Marschalek does malware reverse engineering. Some say she also does marketing, but at the time of writing she could not be reached to further comment on that. At daytime she hunts malware for Cyphort Inc., at nighttime she hunts ghosts. Two years ago Marion won Halvar Flake's reverse engineering challenge for females, since then she set out to rock and roll the industry. She practices martial arts and has a vivid passion to take things apart. Preferably, other people's things.

Bio: Paul Rascagnères
---------------------

Paul Rascagnères is a malware analyst and researcher for the Sekoia's CERT. He is specialized in Advanced Persistant Threat (APT) and incident response. He worked on several complex cases such as government linked malware or rootkits analysis. He is a worldwide speaker at several security events.

Bio: Joan Calvet
----------------

Joan Calvet is a malware researcher working at ESET, where he is mainly involved into in-depth malware investigations. He defended his Ph.D. thesis in 2013, and has spoken at security conferences such as REcon, Virus Bulletin and DeepSec.

HackingTeam - how they infected your Android device by 0days
------------------------------------------------------------
by Attila Marosi

There is no need to make a long introduction when speaking about the famous Remote Control System (RCS), the product of the Italian company Hacking Team. The huge amount - 400 Gb - of leaked data gives rise to lengthy discussion and is extremely concerning for every part of the professionally, politically or even those superficially interested only.

This presentation has three parts: The first is a quick introduction, what the concept and the environment look like (Exploit Delivery Network - Android, Fake App Store...), how the malware was delivered to the targets; and how the infected devices were controlled through the proxy chain.

The second is a detailed analysis of the exploits which were used to infect Android devices. I will give a step-by-step description of the installation (infection) process. Hacking Team has many 0day exploits to install the application and to elevate privileges on those devices. These exploits will also be presented. The third part is a collection of the interesting techniques that were used to keep the application as silent and undetectable as possible (VM and Cuckoo evasion, Anti-Virus detection project… etc.).

Bio: Attila Marosi
------------------

Attila Marosi has always been working in information security field since he started in IT. As a lieutenant of active duty he worked for almost a decade on special information security tasks occurring within the Special Service for National Security. Later he was transferred to the newly established GovCERT-Hungary, which is an additional national level in the internationally known system of CERT offices. Now he works for the SophosLab as a Senior Threat Researcher in the Emerging Thread Team to provid novel solution for the newest threats.

Attila has several international certificates such as CEH, ECSA, OSCP, OSCE. During his free time he is reading lections and does some teaching on different levels; on the top of them for white hat hackers. He presented on many security conferences including hack.lu, DeepSEC, AusCERT, Hacktivity, Troopers, HackerHalted and NullCon.


How digital forensics met threat intelligence
---------------------------------------------
by Ronan Mouchoux, Thomas Chopitea


Blue-team infosec is all about defending against an opponent. And as we all know, knowing (or "gathering intelligence on" your opponent is becoming crucial: being able to know (and to predict) your opponent's moves greatly reduces the cost of defending against their attacks.

This talk will (re-)introduce the concept of Threat Intelligence as we understand it today, leaving misconceptions behind and exploring the concepts and models that have already been developed to describe it, and see how it relates to "classical" intelligence.

Using concrete examples we'll see exactly how threat intelligence fits in the incident response process, ranging from preparation to lessons learned, and how dismissing it as snake oil can have a negative effect on the defenders. We'll also expose the some tools and processes that help DFIRers collect, manage, and use threat intelligence today, including their aspirations and limitations.


Bio: Ronan Mouchoux
-------------------

Ronan is analyst at CERT Sekoia with a focus on Cyber-Threat Intelligence. He is a former SOC analyst and network forensic analyst. He presented his work on bot detection inside corporate networks by leveraging OSINT feeds and semantic DGA detection at SSTIC2012 and Botconf2013. In 2014 he co-authored a paper on a cybercriminal ring stealing intellectual property dubbed "Pitty Tiger". During Botconf2014 he co-presented the main background questions the Pitty Tiger investigation team had to face; including data and people management, hypothesis and doubts, closed and open information release.

Bio: Thomas Chopitea
--------------------

Thomas Chopitea is an incident handler at CERT Société Générale. His day-to-day tasks revolve around incident response (duh), digital forensic investigations, malware analysis (including some reverse engineering late at night), and creating tools that can actually be used by humans. Thomas is one of the core developers of FIR, CERT Société Générale's open-source incident management platform and Malcom, a malware communication analysis and threat intelligence tool he introduced during Botconf2013.

Security Design and High-Risk Users
-----------------------------------

Security is a property of human outcomes, not technical systems. The security community understands how to think about the security of code and is learning how to think about the security of large systems, but has barely begun to start to think about how to improve security outcomes for humans. Security for humans affects the entire software development and deployment lifecycle, but it's most strongly present in the design and requirements phase where it has been largely ignored by the security community. The need for outcome-oriented security design is particularly obvious in the design of systems intended for use by high-risk, specifically-targeted users. In this talk, we'll describe the security design problem, the challenges of supporting high-risk users, and some steps toward practical processes and solutions for the missing discipline in the security community.

Bio: Eleanor Saitta
-------------------

Eleanor Saitta is a freelance security consultant specializing in architectural security for large-scale systems, integrating security into the development lifecycle, and cross-domain security for news organizations and NGOs targeted by nation states. Her employers over the past 12 years include Bishop Fox, IOActive, Security Innovation, and iSEC Partners.
Eleanor is a co-founder and developer for [Trike](http://octotrike.org/), an open source threat modeling methodology and tool which partially automates the art of security analysis and also contributes to the [Briar](https://briarproject.org) and [Mailpile](https://mailpile.is) secure messaging projects.

Eleanor is a regular speaker at industry conferences; past venues include ToorCon, CCC, Hack in The Box, and HOPE.

Twitter: [@Dymaxion](https://twitter.com/Dymaxion)

Scrutinizing WPA2 Password Generating Algorithms in Wireless Routers
--------------------------------------------------------------------
by Eduardo Novella

A wireless router is a networking device that enables a user to set up a wireless connection to the Internet. A router can offer a secure channel by cryptographic means which provides authenticity and confidentiality. Nowadays, almost all routers use a secure channel by default that is based on Wi-Fi Protected Access II (WPA2). This is a security protocol which is believed not to be susceptible to practical key recovery attacks. However, the passwords should have sufficient entropy to avert brute force attacks.

In this research, we compose a strategy on how to reverse-engineer embedded routers. Furthermore, we describe a procedure that can instantly gather a complete wireless authentication trace which enables an offline password recovery attack. Finally, we present a number of use cases where we identify extremely weak password generating algorithms in various routers which are massively deployed in The Netherlands.

The algorithms are used to generate the default WPA2 password. Such a password is loaded during device initialization and hardware reset. Users that did not explicitly change their wireless password are most likely vulnerable to practical attacks which can recover their password within minutes. A stolen password allows an adversary to abuse someone else’s internet connection, for instance compromising the firewall, making a fraudulent transaction or performing other criminal activities. Together with the Dutch National Cyber Security Centre we have initiated a responsible disclosure procedure. However, since these routers are also used by many other companies in various countries, our findings seem to relate an international industry wide security issue.


Bio: Eduardo Novella
--------------------

Eduardo Novella has been finishing his studies abroad at the Radboud University Nijmegen. He is a security analyst at Riscure in The Netherlands where performs security evaluations on embedded devices. Before joining Riscure, he was messing around with wireless routers. Concretely, he was wondering how WPA2 keys were generated by some ISPs. He took several Dutch routers for research and got the answer. He will show how to extract and reverse engineer firmware images, and subsequently how to break the weak cryptography within a few minutes.


Stegosploit - Delivering Drive-By Exploits With Only Images
-----------------------------------------------------------
by Saumil Shah

Stegosploit creates a new way to encode "drive-by" browser exploits and deliver them through image files. These payloads are undetectable using current means. This paper discusses two broad underlying techniques used for image based exploit delivery - Steganography and Polyglots. Drive-by browser exploits are steganographically encoded into JPG and PNG images. The resultant image file is fused with HTML and Javascript decoder code, turning it into an HTML+Image polyglot. The polyglot looks and feels like an image, but is decoded and triggered in a victim's browser when loaded.

The Stegosploit Toolkit contains the tools necessary to test image based exploit delivery. A case study of a Use-After-Free memory corruption exploit (CVE-2014-0282) shall be presented demonstrating the Stegosploit technique.

Bio: Saumil Shah
----------------

Saumil Shah is the founder and CEO of Net-Square, providing cutting edge information security services to clients around the globe. Saumil is an internationally recognized speaker and instructor, having regularly presented at awesome conferences like Deepsec, Blackhat, RSA, CanSecWest, PacSec, EUSecWest, Hack.lu, Hack-in-the-box and others. He has authored two books titled "Web Hacking: Attacks and Defense" and "The Anti-Virus Book".

Saumil graduated with an M.S. in Computer Science from Purdue University, USA and a B.E. in Computer Engineering from Gujarat University. He spends his leisure time breaking software, flying kites, travelling around the world and taking pictures.


Why Johnny Can't Unpack: Toward One Click Unpacking
---------------------------------------------------

Johnny is frustrated, he can't unpack malware. Nor does his latest sandbox which his organization acquired from some Fortune-100 company, nor does his cloud service which his company pays a few k's every month for. Every day he's struggling to analyze malware in order grab intelligence from the latest malware his organization got infected in , but he's looking for something different, something which might assist him to analyze high amounts of packed and obfuscated malware.

In this research I show the journey of "Why Johnny can't Unpack", I start by showing the general problem of unpacking in comparison to the halting problem and then move onto the different complications unpacking obfuscated and protected code has with nowadays protectors. Next, I move onto explaining how it is possible to achieve how percentage of unpacking rate using a debugger-free environment using VMI and program analysis techniques.

Using the aforementioned techniques, we are able to achieve high unpacking rate and the ability to correlate binaries, basic blocks and even families to achieve better malware unpacking results, however we can also expand this research into the next 20% which involves deobfuscation and program transformation by transforming VM-bytecode into x86.

By combining the aforementioned techniques, we are able to achieve high unpacking rate and the ability to correleate between binaries, basic blocks and even different malware families. However, we can also expand this research into fully deobfuscating a program which was whiteboxed or transformed by VM-code or program whitening techniques.


Bio: Shift
----------

Shift is a freelance security researcher with a strong interest in lowlevel, vulnerability research and operating systems.
Wandering from two sides of the coin Shift enjoys breaking software and reverse engineering different types of software.


Improving Flash Exploits Analysis
---------------------------------
by Tillmann Werner

Eight different zero-day vulnerabilities in Adobe Flash Player in 2015 so far, and analysts are struggling to get a handle on the problem:
Malicous Flash poses some special challenges at them when trying to answer, for example, if a particular object is malicious, if it contains
an exploit for a known vulnerability, or if variants of it have been observed before. Naturally, the answer is in the code. In this talk we
will discuss ways of making the relevant information available and use it to write signatures that allow us to identify and classify variants
of known exploit as well as understand unknown ones faster. Together with this presentation we will release swffile.py, a Python class to be
used in custom analysis tools that provides an interface for SWF file parsing.


Bio: Tillmann Werner
--------------------

Tillmann Werner is the Director of Technical Analysis at CrowdStrike Intelligence where he is responsible for the analysis of various kinds
of threats. He loves combining scientific research with intelligence analysis and specializes in malware reverse engineering, honeypot
technologies and containment strategies for large-scale botnets. As a member of the Honeynet Project, Tillmann is actively involved with the
global computer security community and is a regular speaker on the international conference circuit.

Workshops
=========

Malcom Workshop (2 hours)
-------------------------
by Sebastien Larinier and Thomas Chopitea

Crowdsourced Malware Triage! (2 hours)
--------------------------------------
by Sergei Frankoff, Sean Wilson

Malware triage is an important function in any mature incident response program; the process of quickly analyzing potentially malicious files or URLs to determine if your organization has exposure. But what if you don't have an incident response program? What if you are just setting one up? What if you don't have the tools you need to perform your analysis? With the current offering of free online tools and the right mindset, a web browser and a notepad may be all you need.  

In this workshop you will work through the triage of a live Exploit Kit using only free online tools. We will provide an introduction and demo of each tool and support you as you perform your analysis.

This workshop is aimed at junior incident responders, hobby malware analysts, and general security or IT practitioners who are interested in learning more about the malware triage process. If you have no experience with malware analysis but you are a strong developer and understand web technologies such as Javascript and Flash you should have no problem completing the workshop.

In order to participate in this workshop you will need the following:
 - Laptop with a modern web browser and a text editor.  
 - For the text editor Notepad.exe will work but you will have more fun if it has syntax highlighting. Try Notepad++ or SublimeText. 
 - Good Internet connection! 

Bio: Sergei Frankoff
--------------------

Sergei Frankoff is a malware researcher and the Director of Threat Intelligence at Sentrant. His current focus is ad-fraud malware and the ecosystems that support modern ad-fraud. Prior to joining Sentrant Sergei worked as an incident responder and a security analyst. Sergei is a strong believer in taking an open, community approach to combating cyber crime. He actively contributes to open source tools and tries to publish as much as possible. You can find him on twitter as [@herrcore](https://www.twitter.com/herrcore).

Bio: Sean Wilson
----------------

Sean is an incident responder and malware researcher currently focused on tracking botnet and other crimeware based malware. He is also an active contributor to open source security tools focused on incident response. Previously Sean has worked in a number of application security roles with a focus on security testing and threat modelling. He also loves fly fishing.


Analyzing Malicious Office Documents (2 hours)
----------------------------------------------
by Didier Stevens

Dr. Honeypots or: How I Learned to Stop Worrying and Love My Enemies (4 hours)
------------------------------------------------------------------------------
by Guillaume Arcas, Lukas RIST


Hack, brute, root, crash... and start again ! 100% hands-on workshop
--------------------------------------------------------------------
by Guillaume Prigent, Adrien Barchapt

Come on and do it yourself immersed in a real infrastructure and with your own network (hns-platform based).
The objective of this workshop is to show, step by step, how an attacker is able to implement these exploits and how to try to limit the damage (or not) on real and virtual device (SIEMENS, SCHNEIDER, ALLEN-BRADLEY, ...).

Do it yourself ! - Technical labs

Led by Guillaume Prigent and Adrien Barchapt, just implement yourself IT and SCADA network operation with metasploit framework, nmap NSE and IDS/IPS with suricata following different use-cases:

 * Nmap NSE modbus discover;
 * PLC Scan;
 * Metasploit TCP / Modbus - Schneider Remote Start / Stop;
    #1 from attack to signature with suricata IDS;
    #2 from signature to attack with Metapsloit :
        Build your own auxliary module for TCP/Modbus force listen only command

Prerequisites:

* Laptop with Windows 32/64 bits or Linux 64 bits only (Debian wheezy, Debian jessie, Ubuntu 14.04, Ubuntu 14.10, Ubuntu 15.10, Kali Linux) with a RJ45 Gigabit NIC (required !).
* A virtualbox OVA is also available in case your OS is not supported by hns-platform. Please check that your CPU supports virtualization technology

Workshop BTA: an open-source Active Directory security audit framework (2 hours)
--------------------------------------------------------------------------------
by Joffrey Czarny

When it comes to the security of the information system, Active Directory domain controllers are, or should be, at the center of concerns, which are (normally) to ensure compliance with best practices, and during a compromise proved to explore the possibility of cleaning the information system without having to rebuild Active Directory. However, few tools implement this process and several ways exist to backdoor Active Directory. We propose to present some possible backdoors which could be set by an intruder in Active Directory to keep administration rights. For example, how to modify the AdminSDHolder container in order to reapply rights after administrator actions. Moreover, backdoors can be implemented in Active Directory to help an intruder to gain back his privileges.

We will present BTA, an audit tool for Active Directory databases, and our methodology for verifying the application of good practices and the absence of malicious changes in these databases.

The Workshop will be organised as follows:

- We begin by a presentation, describing the stakes around the Active Directory, centerpiece of any information system based on Microsoft technologies. Then some backdoors, in order to keep admins rights or to help an intruder to quickly recover admins rights, will be demonstrated. At last, we will present BTA and the methodology developed to analysis Active Directory.

- Thereafter, we will use (play with) BTA and try to discover backdoors within a Active Directory. We will try also to develop some miners in order to understand how BTA is architectured and show how it's easy to perform some new security checks.

More information on BTA can be found on the Bitbucket repository [https://bitbucket.org/iwseclabs/bta](https://bitbucket.org/iwseclabs/bta)

Bio: Joffrey Czarny
-------------------

Joffrey Czarny is working for Airbus Group Innovations (FR) as a security researcher. Since 2001, Joffrey is a pentester who has released advisories on VoIP Cisco products and spoken at various security-focused conferences (Hack.lu ITunderground, Hacktivity, HITB,  SSTIC, BlackHat Arsenal...). On his spare time, Joffrey is co-organizer of NoSuchCon (Paris) conference.

