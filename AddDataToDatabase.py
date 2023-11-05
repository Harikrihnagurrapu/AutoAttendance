import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('/Users/adityabhogil/PycharmProjects/AutoAttendance/ serviceAccountKey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://auto-attendance11-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "202211":
        {
            "name": "Jyotiraditya bhogil",
            "major": "ETCS",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "202224":
        {
            "name": "Eshaan Kachru",
            "major": "ETCS",
            "starting_year": 2022,
            "total_attendance": 12,
            "standing": "B",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "202208":
        {
            "name": "Shubham Bhandary",
            "major": "ETCS",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "202228":
        {
            "name": "Shreyash Katole",
            "major": "ETCS",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "202230":
        {
            "name": "Rohan Khamitkar",
            "major": "ETCS",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "202219":
        {
            "name": "Harikrishna Gurrapu",
            "major": "ETCS",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },

}

for key, value in data.items():
    ref.child(key).set(value)
