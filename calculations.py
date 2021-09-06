from datetime import date, timedelta

lmp=date(2021,5,1)
duedate=lmp+timedelta(days=280)
duration = [(lmp + timedelta(days = day)).isoformat() for day in range(281)]

def weeks(duration, n):
    for x in range(0, len(duration), n):
        week=duration[x: n+x]
        if len(week) < n:
            week = week + [None for y in range(n-len(week))]
        yield week

weeks_list=[]
for i in (weeks(duration, 7)):
    weeks_list.append(i)

week_order=[]
for i in range(1,41):
    week_order.append("Week " + str(i))

week_dict=dict(zip(week_order, weeks_list))

def current_week():
    today = date.today().strftime("%Y-%m-%d")
    for key in week_dict:
        if today in week_dict[key]:
            return key

print(current_week())
