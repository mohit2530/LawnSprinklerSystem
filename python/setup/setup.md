
# Everything you need to know

Most likely, the setup differs from your custom environment to your dedicated requirements. It is important to note that zones should be set, if the area of sprinkler coverage is more / less. Also note, your flow output and your water pressure because those are more likely to directly alter your sprinkler cycle.

## Advanced Notes

If your setup location is in an colder climate, it is important to use a drain valve to drain all the water out of the pipes so that the water does not freeze and break the pipe. Doing such will require to add a small valve control in the end of the pipe and using some mechanism to pull out the excess water. Will update on this later.

Also be mindful, that the idea behind this sprinkler is to have a dedicated output of water. This means that it will try to water every day, although for lawn application that is not the idea method. This also widely depends on the location you live in. Will also try to encorporate this in future releases. 

In addition to above, we are also trying to setup email and an UI interface to use on the local IP network. This allows for the user to control the water flow through their own convinience. This is designed with the idea that `weather` cannot always be predictable. So if customers have to edit the facility to provide water, they will be able to. However, this is upcoming in the future release.

## Setting Up


### Device Used

Raspberry PI. Model 4 **[Raspberry Pi Model][raspy]**

Relay 5V **[Relay][relay]**

Lights ( LED ) for visual purposes. **[Light][lights]**

Female Jumper Wires. **[Female Wires][wires]**

Rectifier Diode for flyback. **[Rectifier Diode][rectifier]**

220 Ohm Resistors for lights. **[Resistor][resistors]**

DC Solenoid Valve. **[DC Valve][valve]**

DC power adapter. **[DC Power Adapter][adapter]**

`Note`: The solenoid valve must match the power adapter type. And 3/4 inch solenoid valve is more than enough for small home projects.


**### Breadboard Image**

Image of the breadboard : **[ImageBreadboard][image]**

Image of the circuit : **[Circuit][circuitImg]**

[raspy]: https://www.raspberrypi.org/products/raspberry-pi-4-model-b/
[relay]:https://www.amazon.com/SunFounder-Channel-Optocoupler-Expansion-Raspberry/dp/B00E0NTPP4?ref_=fsclp_pl_dp_4
[lights]: https://www.sparkfun.com/products/12062
[wires]: https://www.sparkfun.com/products/9140
[rectifier]: https://www.sparkfun.com/products/8589
[resistors]: https://www.jameco.com/webapp/wcs/stores/servlet/Product_10001_10001_690700_-1
[valve]: https://www.lowes.com/pd/Orbit-1-in-Plastic-Electric-Inline-Irrigation-Valve/1000152387
[adapter]: https://www.amazon.com/12v-power-supply/s?k=12v+power+supply
[circuitImg]: https://github.com/mohit2530/LawnSprinklerSystem
[image]: https://github.com/mohit2530/LawnSprinklerSystem