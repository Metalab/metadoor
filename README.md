# metadoor

New Metalab™ feature: Look up whether the door is open!

# Setup

Script works if systemuser is `metadoor`

Run the `setup_doorsystem.sh` script as root via sudo.

**Currently no warranty that it runs out of the box**

## Folder Structure

```dehydrated``` Config for dehydrated Let's Encrypt certificates and auto renew  
```metadoor```: metadoor scripts and service and timer files  
```nginx```: nginx config files  

# General Info

**Attention: This solution is temporary and will be replaced in the future by a better door status system**

There's now a Raspberry Pi at the door under ```http://10.20.30.77``` (locally) and https://eingang.metalab.at/ (IPv4 + IPv6 globally) that publishes:
* ```index.html``` – Nice and shiny interface
* ```status.json``` – JSON containing the onsite status
* ```doorstatus.json``` – JSON containing the door status

The JSON API for the onsite status returns one of the following values
* ```status: unknown``` – Metalab onsite status is unknown
* ```status: open``` – Metalab onsite status is powered up
* ```status: closed``` – Metalab onsite is shutdown

The JSON API for the door status returns one of the following values
* ```status: boot``` – No status detected yet
* ```status: open``` – Metalab door is open
* ```status: closed``` – Metalab door is closed

Tadaa!

Brought to you by Nico, Nini, Ripper, Phileas, and many other lovely Metalab people <3  
Resurrected by Hetti
