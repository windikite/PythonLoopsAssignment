import random

positive_moods = ["happy", "energetic", "joyful", "excited", "relaxed"]
negative_moods = ["sad", "angry", "melancholic", "envious", "wistful"]
encouraging_statements = ["Keep it up!", "Glad you felt that way!", "Nice positivity!"]
uplifting_statements = ["I hope your day got better!", "Everyone has bad days, you'll have good ones soon for sure!", "Take care of yourself!"]
days_of_week = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

moods = positive_moods + negative_moods

for day in days_of_week:
	mood = random.choice(moods)
	statement = ""
	if mood in positive_moods:
		statement = random.choice(encouraging_statements)
	elif mood in negative_moods:
		statement = random.choice(uplifting_statements)
	print("On", day, "you were", mood, ".", statement)
