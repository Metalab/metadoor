# metadoor

New Metalab™ feature: Look up whether the door is open!

There's now a Raspberry Pi at the door under ```10.20.30.77``` (locally) and ```2001:858:5:3a42::d8``` (globally) (there's [a mirror too!](http://static.exaple.org/openClose)) and publishes:
* ```index.html``` – Nice and shiny interface
* ```status.json``` – JSON containing the status

The JSON API will return one of the following values
* ```status: boot``` – No status detected yet
* ```status: open``` – Metalab is open
* ```status: closed``` – Metalab is closed

Tadaa!

Brought to you by Nico, Nini, Ripper, Phileas, and many other lovely Metalab people <3
