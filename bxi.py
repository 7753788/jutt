a
    �aa  �                   @   s  z$d dl Z d dlZd dlZd dlZW n ey@   e �d� Y n0 d dlZdZejddd��� Z	e �d� e
d� e�d	�j�� Ze j�d
�r�eekr�e �d� n`e �d� de	v r�de	v r�e �d� e �d� n&de	v r�e �d� e �d� ne
d� ne
d� dS )�    Nzpip install requestsz1.0z	uname -omT)�shell�clearz Checking Update . . .zAhttps://raw.githubusercontent.com/Binyamin-binni/bxi/main/versionZbxizchmod 777 bxi && ./bxiz
rm -rf bxiZAndroidZarmzXcurl -L -o bxi https://raw.githubusercontent.com/Binyamin-binni/dynamic/main/bxi/arm/bxiZaarchz\curl -L -o bxi https://raw.githubusercontent.com/Binyamin-binni/dynamic/main/bxi/aarch64/bxiz* Unknown architecture, contact with owner.z% Unknown machine, contact with owner.)�os�sys�
subprocessZrequests�ImportError�system�vZcheck_output�decodeZarch�print�get�text�rstripZvf�path�isfile� r   r   �/storage/emulated/0/bxistart.py�<module>   s0   




