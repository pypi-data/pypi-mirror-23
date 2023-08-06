#TbaApi3
TbaApi3 is a Python library for TheBlueAlliance.com's API version 3. It's currently in development, but right now supports all Team and requests. 

#Installation
To install TbaApi3 with pip:  
```pip install TbaApi3```
In addition to having the library installed, you'll need an API Key from TBA. You can find one [here](https://www.thebluealliance.com/account).

#Usage
To create an ApiObject with new key `'key'`:
```
import TbaApi3

api_object = TbaApi3.ApiObject('key')
```
Now you can check documentation to find corresponding TBA API calls and their functions, as well as a few extra "convenience" functions. For example, to find all FRC teams active in a season:
```
teams = api_object.get_all_teams(year)
```
Now to get the name of the first team:
```
print(teams[0].nickname)
```
