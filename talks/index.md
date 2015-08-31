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

