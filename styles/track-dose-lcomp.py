days = [
   { "day_name": "mon",
        "taken_at": {
        '12:00': 0,
        '14:00': 0,
        '16:00': 0
        }
    },
    { "day_name": "tue",
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

unit = 'changeme'
substance = 'changeme'

day = (i["day_name"] for i in days)
nums = [sum(i["taken_at"].values()) for i in days]

[print(f"{i}: {x}") for i, x in zip(day, nums)]

nl = '\n'
print(f"{nl}Total -> {substance}: {sum(nums)}{unit}")
