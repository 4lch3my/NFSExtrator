# NFSExtrator
Extract files via Python from a NFS stream embedded in a pcap file.
========
STEPS:

1, Open pcap in Wireshark > select nfs stream


2, Follow NFS TCP stream 


3, Show RAW > shave file as extracted.raw


4, RUN command: python3 nfs_extract.py extracted.raw



Example of execution: https://tryhackme.com/room/hfb1stolenmount
