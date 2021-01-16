# AutoDataBasics
Simplifies Timesheet Entry for DataBasics Timesheets. This should make it much easier to submit your timesheets without having to deal with DataBasics' UI.

Tested in Windows only so far.

### Requirements:
* A Python **3.6+** environment
* Selenium (can be installed using ``pip install selenium``)

### Setup:
* Clone this repository into a dedicated directory (the ``adb.py`` file is really the only thing you need).
* Download the **[Selenium Chrome driver](https://chromedriver.chromium.org/downloads)** and place the executable file in the same directory alongside adb.py
* Create an ``auth.txt`` file with 3 lines: The **URL** for your DataBasics login page, your **username** and your **password**. Example:
```
https://xxx.data-basics.net/xxx/databasics.ext#
sergiome@gmail.com
p455w0rd
```
* On DataBasics, **[create as many Favorite/Memorized](https://databasics.atlassian.net/wiki/spaces/PG6/pages/526544/Favorites+Timesheet) rows as you will need** to cover your timesheet entries. For example, create one for your project, one for vacations, and so on.

### Filling your Timesheet
Anytime you want to fill your timesheet, prepare a ``timesheet.txt`` file following the format detailed below and place it in the same directory as the script, auth and driver. Each line in this file corresponds to a timesheet entry, with each value separated by commas. 

The first value of every row is the **position of the favorite/memorized entry to be used for this line, as displayed in your Favorites table, starting from 0** (in the above example, your favorite entry for project work would be 0, and the one for vacations would be 1). You may need to login to DataBasics and look at your Favorites to figure out what number each Favorite corresponds to.

Example mapping:

<img src="https://i.imgur.com/LdExgJH.png" width=550>

The rest of the values are self-explanatory: The second value is the entry note/description, and the following 5 values are the time values from Monday to Friday. 

Example: 
```
0, This is a note for an entry that uses the favorite in the first row (project work), 1,8,0,8,8
1, This is a note for an entry using the favorite in second row (vacations), 7,0,0,0,0
1, This is a note for another entry that uses the favorite in the second row (vacations), 0,0,8,0,0
```
(This is a CSV file and is ingested as one, so feel free to use your favorite CSV Editor to prepare it!)

### Execution:
Just execute the script!

```python adb.py```

If all goes well, you should see a Chrome window open, and the entire process will be automated. Once finished, **review your timesheet** and submit! **This script does not auto-submit your timesheet**. You have to press that button yourself :)

---

### For Developers:

If you want to build a UI for this, change the input file format or extend it in any other way, it should be fairly easy to do. You can just import the script and use the ``runDataBasics`` function, which receives the **login url**, **username**, **password** and **timesheet lines** which is a list of dict/json objects with ``fav``, ``note`` and ``times`` attributes.

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
