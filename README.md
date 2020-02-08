# metadoor

New Metalab™ feature: Look up whether the door is open!

**Attention: This solution is temporary and will be replaced in the future by a door status on our homepage https://metalab.at**

There's now a Raspberry Pi at the door under ```10.20.30.77``` (locally), https://hodors.cyber.coffee (IPv4 Mirror globally) and ```2a02:61:a2::d8``` globally and publishes:
* ```index.html``` – Nice and shiny interface
* ```status.json``` – JSON containing the status

The JSON API will return one of the following values
* ```status: boot``` – No status detected yet
* ```status: open``` – Metalab is open
* ```status: closed``` – Metalab is closed

Tadaa!

Brought to you by Nico, Nini, Ripper, Phileas, and many other lovely Metalab people <3  
Resurrected™ by Hetti
