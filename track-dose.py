days = [
   { "day_name": "mon",
        "taken_at": {
        '12:00': 0,
        '14:00': 0,
        '16:00': 0
        }
    },
    { "day_name": "thu",
        "taken_at": {
        '12:00': 0,
        '14:00': 0,
        '16:00': 0
        }
    },
    { "day_name": "wed",
        "taken_at": {
        '12:00': 0,
        '14:00': 0,
        '16:00': 0
        }
    },
    { "day_name": "thu",
        "taken_at": {
        '12:00': 0,
        '14:00': 0,
        '16:00': 0
        }
    },
    { "day_name": "fri",
        "taken_at": {
        '12:00': 0,
        '14:00': 0,
        '16:00': 0
        }
    },
    { "day_name": "sat",
        "taken_at": {
        '12:00': 0,
        '14:00': 0,
        '16:00': 0
        }
    },
    { "day_name": "sun",
        "taken_at": {
        '12:00': 0,
        '14:00': 0,
        '16:00': 0
        }
    }
]

dose_ray = []

unit = 'changeme'
substance = 'changeme'
for i in days:
    days = i["day_name"]
    dose = i["taken_at"].values()
    dose_per_day = sum(dose)
    print(f"{days}: {dose_per_day} {unit}")
    dose_ray.append(dose_per_day)
    
Total = sum(dose_ray)

nl='\n'
 
print(f"{nl}Total -> {substance}: {Total} {unit}")
