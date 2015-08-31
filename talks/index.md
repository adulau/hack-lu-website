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

Webiste: [sophia.re](http://www.sophia.re/)


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

