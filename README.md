# AutoDataBasics
Simplifies Timesheet Entry for DataBasics Timesheets. Tested in Windows only so far.

### Requirements:
* A Python 3.6+ environment
* Selenium (can be installed using ``pip``)
* On DataBasics, [create as many Favorite/Memorized](https://databasics.atlassian.net/wiki/spaces/PG6/pages/526544/Favorites+Timesheet) rows as you will need to cover your timesheet entries.

### Setup:
* Clone this repository into a dedicated directory.
* Download the [Selenium Chrome driver](https://chromedriver.chromium.org/downloads) and place it in the same directory alongside adb.py
* Create an ``auth.txt`` file with 3 lines: The **URL** for your DataBasics login page, your **username** and your **password**. Example:
```
https://xxx.data-basics.net/xxx/databasics.ext#
sergiome@gmail.com
p455w0rd
```
* Create a ``timesheet.txt`` file and place it alongside the driver, script and auth file. The timesheet will be filled using the information contained in this file: Each line will correspond to a timesheet entry, with each value separated by commas. The first value is the favorite row this entry will correspond to, starting from 0. The second value is the entry note, and the rest of the values are the time values from monday to friday. Example: 
```
0, This is a note for an entry that uses the favorite in the first row, 1,2,3,4,5
1, This is a note for an entry using the favorite in second row, 5,4,3,2,1
1, This is a note for a second entry that uses the favorite in the second row, 0,0,1,0,0
```
### Execution:
Just execute the script!
```python adb.py```

If all goes well, you should see a Chrome window open, and the entire process will be automated. Once finished, review your timesheet and submit!

