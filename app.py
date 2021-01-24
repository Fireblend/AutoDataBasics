from flask import Flask, request, render_template
from os import path
import csv
import adb

app = Flask(__name__)

@app.route("/")
def form():
    global alias_dict, db_url, username, password, faves, timesheet_lines

    db_url = ""
    username = ""
    password = ""
    timesheet_lines = []

    faves = ["Favorite "+str(x) for x in list(range(1,21))]
    alias_dict = dict()

    if(path.exists("auth.txt")):
        with open("auth.txt") as auth:
            auth_txt = auth.read().split("\n")
            db_url = auth_txt[0]
            username = auth_txt[1]
            password = auth_txt[2]

    if(path.exists("alias.txt")):
        faves = []
        with open("alias.txt") as alias:
            for line in alias.read().split("\n"):
                try:
                    alias_dict[line.split(":")[0]] = int(line.split(":")[1])
                    faves.append(line.split(":")[0])
                except:
                    pass

    if(path.exists("timesheet.txt")):
        with open("timesheet.txt") as ts:
            csv_reader = csv.reader(ts)
            timesheet_lines = []
            for row in csv_reader:
                timesheet_lines.append({"fav":row[0].strip(),
                "note":row[1].strip(),
                "times":[x.strip() for x in row[2:]]})

    return render_template("index.html", username=username, password=password, db_url=db_url, faves=faves, timesheet_lines=timesheet_lines)

@app.route("/submit", methods=['POST'])
def form_post():
    ts = buildTimesheet(request)
    if request.form['action'] == "Save Draft":
        saveToFile(ts)
    elif request.form['action'] == "Delete Draft":
        deleteDraft()
        return form()
    elif request.form['action'] == 'Submit to DataBasics':
        url = request.form["url"]
        username = request.form["username"]
        password = request.form["password"]
        adb.runDataBasics(url, username, password, ts, alias=alias_dict)
    print(ts)
    return('', 204)

def buildTimesheet(request):
    i = 0
    ts = []
    while request.form.get(f"fave{i}", None):
        fav = request.form[f"fave{i}"]
        des = request.form[f"description{i}"]
        times = [request.form[f"{x}{i}"] for x in ["mon","tue","wed","thu","fri"]]
        i += 1
        if(des.strip() == "" and sum([float(x) for x in times]) == 0): continue
        ts.append({"fav":fav, "note":des, "times":times})
    return ts

def deleteDraft():
    with open("timesheet.txt", "w") as ts_file:
        ts_file.write('')

def saveToFile(ts):
    with open("timesheet.txt", "w") as ts_file:
        for entry in ts:
            times=",".join(entry["times"])
            fav = entry["fav"]
            note = entry["note"]
            ts_file.write(f"{fav},\"{note}\",{times}\n")
