# auto-action-service

Not sure yet!

Intervals:
[

    {
        "name": "display-off-night",
        "action": "display-off",
        "trigger": "interval",
        "seconds": 7
    },
    {
        "name": "refresh-display",
        "action": "display-on",
        "trigger": "interval",
        "seconds": 5
    }

]

[
{
"name": "display-on-evening",
"action": "display-on",
"trigger": "cron",
"hour": 18,
"minute": 0
},
{
"name": "display-off-night",
"action": "display-off",
"trigger": "cron",
"hour": 23,
"minute": 01
},
{
"name": "weekly-restart",
"action": "display-off",
"trigger": "cron",
"day_of_week": "sun",
"hour": 2,
"minute": 0
},
{
"name": "display-on-evening",
"action": "display-on",
"trigger": "cron",
"hour": 17,
"minute": 0
},
{
"name": "display-off-night",
"action": "display-off",
"trigger": "cron",
"hour": 23,
"minute": 30
},
{
"name": "refresh-display",
"action": "display-on",
"trigger": "interval",
"minutes": 10
}
]
