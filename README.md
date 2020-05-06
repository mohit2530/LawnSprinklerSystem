# Lawn Sprinkler System

![Build Status](https://travis-ci.org/klugjo/hexo-autolinker.svg?branch=master)
[![License][license-image]][license]

<img src="https://github.com/mohit2530/LawnSprinklerSystem/blob/master/sprinkler.jpeg"
 alt="Sprinkler System" title="Sprinklers" align="right" width="400px" height="400px" />

 Lawn Sprinkler System is designed to aid in proper usage of the sprinkler system to effectively aid the users to care for their lawn. In the first release of the project, this lawn sprinkler system does the very basics and we will continue to provide upgrade as we develop such features.

 ## Limitations

 1. Weather is not being monitored. We assume that it is a sunny day.

 2. We have no way of letting the user provide the lawn dryness. Lawn Dryness is set at `Medium` as such.

 3. We do not take the previous days or the weather of the future days into account either.

 4. One of the major upgrades is to calculate the water flow, and be able to assume the amount of water contained in  one given area to give estimates on how long the flow has to occur. We are still working on its implementation.


## Release 1.00.02

 1. Monitoring Weather. If the hours is between 5 am and 10 am then only we monitor the weather. If the time is not at the allocated range, the sprinkler system should not even activate.

 2. Lawn dryness is still currently set at `Medium`.

 3. Previous day weather and future days weather are still not taken under consideration. Using `OpenWeatherApi.org` for the weather data. Working on the fix to fetch values for previous and future data.

 4. Water flow is also WIP. Will update in the coming releases.


## Release 1.00.03

1. Updating the water flow. Now the program will set the watering to a dedicated level. More WIP on future releases.

2. Includes minor bug fixes.


## Release 1.00.04

 1. Updating the water flow, currently the timer operates in conjunction to the level of water flow. Therfore, relaying stop to the relay when the timer has expired.

 2. Logging is enabled and all weather data is being stored in the information files.


### UPCOMMING RELEASE
======================

The upcomming release will include ability to research for previous weather and will record that activity. The next implementation would be where the script would allow the sprinkler system to execute only when there is no rainfall yesterday and today.


## Basic Installations

We are currently upgrading our systems to be able to use docker. Once that is put into place, we no longer would require dependencies to be installed. For now however, we have some dependencies to be installed.

 1. python 3.0
 2. requests library for python


 ## QuickStart

The application is simple, yet effective. The main goal behind this is to aid in the DIY Projects of a lawn sprinkler system. The quickstart guide should encompass a `HOW TO` video once everything is set up and done. This will allow the user to DIY the sprinkler system. The main overarching goal is to make lawn watering easy and as automatic as possible with the idea of being cost effective.


## Find out more

| **[Technical Docs][techdocs]**     | **[Setup Guide][setup]**     | **[Roadmap][roadmap]**           | **[Contributing][contributing]**           |
|-------------------------------------|-------------------------------|-----------------------------------|---------------------------------------------|
| [![i1][techdocs-image]][techdocs] | [![i2][setup-image]][setup] | [![i3][roadmap-image]][roadmap] | [![i4][contributing-image]][contributing] |

## Architecture

The architecture is based on Python as a service, with an integration of DB system ( Not yet decided ). A basic simple front end design is being thought to enable users to be able to send data that is required to the system.


## Questions or Help

We are committed to a loosely-coupled architecture and would love to assist you in the usage of the application itself. If you would like to request features or support please email the team.


## Copyright and License

Copyright @ 2020.

Licensed under the **[MIT LICENSE][license]**
you may not use this software except in compliance with the License.

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.



[license-image]: http://img.shields.io/badge/license-Apache--2-blue.svg?style=flat
[license]: https://www.mit.edu/~amini/LICENSE.md

[techdocs-image]: https://d3i6fms1cm1j0i.cloudfront.net/github/images/techdocs.png
[setup-image]: https://d3i6fms1cm1j0i.cloudfront.net/github/images/setup.png
[roadmap-image]: https://d3i6fms1cm1j0i.cloudfront.net/github/images/roadmap.png
[contributing-image]: https://d3i6fms1cm1j0i.cloudfront.net/github/images/contributing.png

[techdocs]: https://github.com/mohit2530/LawnSprinklerSystem
[setup]: https://github.com/mohit2530/LawnSprinklerSystem
[roadmap]: https://github.com/mohit2530/LawnSprinklerSystem
[contributing]: https://github.com/mohit2530/LawnSprinklerSystem