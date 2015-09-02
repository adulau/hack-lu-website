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

