## Information

 1. One of the major upgrades is to calculate the water flow, and be able to assume the amount of water contained in  one given area to give estimates on how long the flow has to occur. We are still working on its implementation.

## Release 1.00.02

 1. Monitoring Weather. If the hours is between 5 am and 10 am then only we monitor the weather. If the time is not at the allocated range, the sprinkler system should not even activate.

 2. Lawn dryness is still currently set at `Medium`.

 3. Previous day weather and future days weather are still not taken under consideration. Using `OpenWeatherApi.org` for the weather data. Working on the fix to fetch values for previous and future data.

 4. Water flow is also WIP. Will update in the coming releases.


## Release 1.00.03

1. Updating the water flow. Now the program will set the watering to a dedicated level. More WIP on future releases.

2. Includes minor bug fixes.


## Release 1.00.04

 1. Updating the water flow, currently the timer operates in conjunction to the level of water flow. Therefore, relaying stop to the relay when the timer has expired.

 2. Logging is enabled and all weather data is being stored in the information files.


## Release 1.00.05

1. Installation of `pip3 install pytz` for local date time.

2. Surfacing the ability to look into previous day weather data and set the sprinkler to run henceforth.

3. Control the size of the file, If the file is too large, then the script will remove the first lines. This check only occurs on December 31 every year.

## Release 1.00.06

1. Set up to work in cron timer from RASPBERRY PI.

2. Odd hourly checks are run, cron tab is also set for odd hours.

3. Installation of `sudo apt-get install python-rpi.gpio python3-rpi.gpio`

## Release 2.00.00

1. Fully functional sprinkler system is recorded at this point.

2. Sprinkler is adjusted to run at 6 am in the morning. If rain is not detected within the following day, the sprinkler should start for a time span of 9.12 minutes. This occurs everyday provided the conditions are met.

3. Will update features as / if they are requested.


## Release 2.00.01

1. Minor bug fixes and updates.

2. Ability to send email services to users that are set up.

3. Clear redundant information texts every month on the 15th.