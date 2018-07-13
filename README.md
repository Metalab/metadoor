# metadoor

New Metalab™ feature: Look up whether the door is open!

There's now a Raspberry Pi at the door under ```10.20.30.77``` (locally) and ```2a02:61:a2::d8``` or http://entry.bällebad.info/ (IPv6) (globally) (there's is no mirror in the mean time) and publishes:
* ```index.html``` – Nice and shiny interface
* ```status.json``` – JSON containing the status

The JSON API will return one of the following values
* ```status: boot``` – No status detected yet
* ```status: open``` – Metalab is open
* ```status: closed``` – Metalab is closed

Tadaa!

Brought to you by Nico, Nini, Ripper, Phileas, and many other lovely Metalab people <3  
Resurrected™ by Hetti
