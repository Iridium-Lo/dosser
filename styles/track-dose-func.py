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

day = list(map(lambda x: x["day_name"], days))
nums = list(map(lambda x: sum(x["taken_at"].values()), days))

list(map(lambda x, y: print(f"{x}: {y}"), day, nums))

nl = '\n'
print(f"{nl}Total -> {substance}: {sum(nums)}{unit}")
