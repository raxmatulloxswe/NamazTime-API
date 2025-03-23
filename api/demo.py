from waqt import NamazTime

prayer_times = NamazTime("london", school=1, method=3)
namaz_periods = prayer_times.today()
# namaz_periods_weekly = prayer_times.weekly()

if namaz_periods:
    for key, value in namaz_periods.items():
        print(f"🟢 {key}: {value}")
