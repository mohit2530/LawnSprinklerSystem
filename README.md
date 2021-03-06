# Lawn Sprinkler System

![Build Status](https://travis-ci.org/klugjo/hexo-autolinker.svg?branch=master)
[![License][license-image]][license]

<img src="https://github.com/mohit2530/LawnSprinklerSystem/blob/master/sprinkler.jpeg"
 alt="Sprinkler System" title="Sprinklers" align="right" width="400px" height="400px" />

 Lawn Sprinkler System is designed to aid in proper usage of the sprinkler system to effectively aid the users to care for their lawn. In the first release of the project, this lawn sprinkler system does the very basics and we will continue to provide upgrade as we develop such features.


## Basic Installations

We are currently upgrading our systems to be able to use docker. Once that is put into place, we no longer would require dependencies to be installed. For now however, we have some dependencies to be installed.

 1. python 3.0
 2. requests library for python
 3. pip3 install pytz for local datetime
 4. sudo apt-get install python-rpi.gpio python3-rpi.gpio
 5. Crontab :: --> 0 * * * * python3 [location of file] <!-- run the scrint on the hour every hour -->
 6. Crontab :: --> 0 22 * * * cd /home/Desktop/code/LawnSprinklerSystem && git pull <!-- git pull everyday 10 pm from master -->
 6. `sudo su` -> `crontab -e` -> `0 7 * * 1 apt update && apt dist-upgrade -y` <!-- update the electronics every monday at 7 am -->
 7. Added the smtp library for email usage. Available without installation on python 3 +


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

[techdocs]: https://github.com/mohit2530/LawnSprinklerSystem/blob/master/documentation.md
[setup]: https://github.com/mohit2530/LawnSprinklerSystem/blob/master/setup/setup.md
[roadmap]: https://github.com/mohit2530/LawnSprinklerSystem
[contributing]: https://github.com/mohit2530/LawnSprinklerSystem
