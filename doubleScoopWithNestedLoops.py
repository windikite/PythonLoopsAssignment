import random

positive_moods = ["happy", "energetic", "joyful", "excited", "relaxed"]
negative_moods = ["sad", "angry", "melancholic", "envious", "wistful"]
encouraging_statements = ["Keep it up!", "Glad you felt that way!", "Nice positivity!"]
uplifting_statements = ["I hope your day got better!", "Everyone has bad days, you'll have good ones soon for sure!", "Take care of yourself!"]
days_of_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
times = ["8am", "1pm", "6pm"]

moods = positive_moods + negative_moods

for day in days_of_week:
	moods_felt = []
	mood_weight = 0
	mood_of_the_day = ""
	
	print("Moods for", day, ": ")
	for time in times:
		mood = random.choice(moods)
		moods_felt.append(mood)
		if mood in positive_moods:
			mood_weight += 1
		elif mood in negative_moods:
			mood_weight -= 1
		print(time, mood)
	statement = ""
	if mood_weight > 0:
		statement = random.choice(encouraging_statements)
		mood_of_the_day = "mostly positive!"
	elif mood_weight == 0:
		statement = random.choice(uplifting_statements)
		mood_of_the_day = "doing alright."
	elif mood_weight < 0:
		statement = random.choice(uplifting_statements)
		mood_of_the_day = "mostly negative."
	print("You were", mood_of_the_day, statement)