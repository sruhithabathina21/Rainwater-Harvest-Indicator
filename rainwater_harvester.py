# rainwater_harvester.py
print("-------- Rainwater Harvest Indicator --------")
rainfall = float(input("Enter current day's rainfall (in mm): "))

threshold = 10.0  # Minimum rainfall for harvesting to be effective

if rainfall >= threshold:
    print("✅ It's worth collecting rainwater today.")
else:
    print("❌ Rainfall is too low; not worth collecting.")
