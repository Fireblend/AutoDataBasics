# AutoDataBasics
Simplifies Timesheet Entry for DataBasics Timesheets. Tested in Windows only so far.

### Requirements:
* A Python **3.6+** environment
* Selenium (can be installed using ``pip``)
* On DataBasics, **[create as many Favorite/Memorized](https://databasics.atlassian.net/wiki/spaces/PG6/pages/526544/Favorites+Timesheet) rows as you will need** to cover your timesheet entries. For example, create one for your project, one for vacations, and so on.

### Setup:
* Clone this repository into a dedicated directory.
* Download the **[Selenium Chrome driver](https://chromedriver.chromium.org/downloads)** and place the executable file in the same directory alongside adb.py
* Create an ``auth.txt`` file with 3 lines: The **URL** for your DataBasics login page, your **username** and your **password**. Example:
```
https://xxx.data-basics.net/xxx/databasics.ext#
sergiome@gmail.com
p455w0rd
```
* Create a ``timesheet.txt`` file and place it alongside the driver, script and auth file. Your timesheet will be filled using the information contained in this file: Each line will correspond to a timesheet entry, with each value separated by commas. 

The first value is the **row number for the favorite this entry will correspond to, starting from 0** (in the above example, your favorite entry for project work would be 0, and the one for vacations would be 1). You may need to login to DataBasics and look at your Favorites to figure out what number each Favorite corresponds to.

The rest of the values are self-explanatory: The second value is the entry note/description, and the following 5 values are the time values from Monday to Friday. 

Example: 
```
0, This is a note for an entry that uses the favorite in the first row, 1,2,3,4,5
1, This is a note for an entry using the favorite in second row, 5,4,3,2,1
1, This is a note for another entry that uses the favorite in the second row, 0,0,1,0,0
```
### Execution:
Just execute the script!
```python adb.py```

If all goes well, you should see a Chrome window open, and the entire process will be automated. Once finished, **review your timesheet** and submit! **This script does not auto-submit your timesheet**. You have to press that button yourself :)

---

### For Developers:

If you want to build a UI for this, change the input file format or extend it in any other way, it should be fairly easy to do. You can just import the script and use the ``runDataBasics`` function, which receives the **login url**, **username**, **password** and **timesheet lines** which is a list of json objects with "fav", "note" and "times" attributes.

Example:
``` py
import adb

db_url = ...
username = ...
password = ...

ts = [{"fav":0, "note":"this is a note", "times":[1,1,2,4,5]},
      {"fav":1, "note":"this is another note", "times":[2,2,3,1,1]},
      {"fav":1, "note":"this is a third note", "times":[1,1,0,0,0]}]
 
 adb.runDataBasics(db_url, username, password, ts)
 ```
