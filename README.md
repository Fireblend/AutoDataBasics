# AutoDataBasics (Now with a friendly Web UI!)
Simplifies Timesheet Entry for DataBasics Timesheets. This should make it much easier to submit your timesheets without having to deal with DataBasics' UI.

Tested in Windows only so far.

### Requirements:
* A Python **3.6+** environment
* Chrome Web Browser
* Selenium (can be installed using ``pip install selenium``)
* Flask (can be installed using ``pip install flask``)

### One-Time Setup:
1. Clone or download the contents of this repository into a dedicated directory.
2. Download the **[Selenium Chrome driver](https://chromedriver.chromium.org/downloads)** and place the executable file in the same directory alongside ``adb.py``
3. On DataBasics, **[create as many Favorite/Memorized](https://databasics.atlassian.net/wiki/spaces/PG6/pages/526544/Favorites+Timesheet) entries as you will need** to cover your timesheet entries. For example, create one for your project, one for vacations, one for meetings, and so on.
4. Next, set up an **alias file**:  Create a file called ``alias.txt`` with each line being a descriptive name for each **Favorite** created in the previous step, in the same order as they appear on the DataBasics Favorites. Example:
```
project
vacations
meetings
```
5. **Optional**: Create an ``auth.txt`` file with 3 lines: The **URL** for your DataBasics login page, your **username** and your **password**. Example:
```
https://xxx.data-basics.net/xxx/databasics.ext#
sergiome@gmail.com
p455w0rd
```
---
### Filling your Timesheet:
Anytime you want to report your time, just open your terminal, navigate to the directory where the files are located and run:

```flask run```

If all goes well, the AutoDataBasics UI should be available at the displayed address (i.e. http://127.0.0.1:5000/):

<img src="https://cdn.discordapp.com/attachments/694966618471792680/802965567253512212/unknown.png">

This UI is pretty straightforward, but here's some features:

- **Save Draft**: Saves your current draft on a ``timesheet.txt`` file. This file will be used to automatically fill your timesheet next time you open AutoDataBasics.
- **Delete Draft**: Deletes all entries on any existing draft and clears the displayed timesheet.
- **Submit to DataBasics**: This will start the automated timesheet-filling process. Sit back and watch your timesheet be filled :)

---
### For Developers:

If you want to build an alternate UI for this, change the input file format or extend it in any other way, it should be fairly easy to do. You can just import the script and use the ``runDataBasics`` function, which receives the **login url**, **username**, **password** and **timesheet lines** which is a list of dict/json objects with ``fav``, ``note`` and ``times`` attributes. **Aliases** are submitted through the optional ``alias`` parameter as a dictionary of ``str`` keys and ``int`` values.

Example:
``` py
import adb

db_url = ...
username = ...
password = ...

alias_dict = {"project":0, "meetings":1}

ts = [{"fav":"project", "note":"this is a note", "times":[1,1,2,4,5]},
      {"fav":"meetings", "note":"this is another note", "times":[2,2,3,1,1]},
      {"fav":"project", "note":"this is a third note", "times":[1,1,0,0,0]}]
 
 adb.runDataBasics(db_url, username, password, ts, alias=alias_dict)
 ```
---
Want to say thanks? Donate to <a href="https://immigrantfamiliestogether.com/"><b>Immigrant Families Together</b></a>, <a href="https://www.raicestexas.org/"><b>RAICES</b></a> or a similar charity :)
