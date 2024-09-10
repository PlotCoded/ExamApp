import json

<<<<<<< HEAD
=======
with open("Storage.json","r") as file:
	content = file.read()

	content = json.loads(content)

>>>>>>> 13483fca6ec6bf8c173c66f5cb2efe5300135b50
def subject_list():
	with open("Storage.json","r") as file:
		content = file.read()

	content = json.loads(content)
	return list(content.keys())

def last_question(subject):
	with open("Storage.json","r") as file:
		content = file.read()

	content = json.loads(content)
	return list(content[subject][2]["questions"].keys())[-1].split(" ")[1]

def get_time(subject):
	with open("Storage.json","r") as file:
		content = file.read()

	content = json.loads(content)
	return content[subject][0]["details"]["time"]

def get_marks(subject):
	with open("Storage.json","r") as file:
		content = file.read()

	content = json.loads(content)
	return content[subject][0]["details"]["marks"]

def get_questions(subject, action):
	with open("Storage.json","r") as file:
		content = file.read()

	content = json.loads(content)
	if action == "questions":
		return list(content[subject][2]["questions"].values())
	elif action == "length":
		return len(list(content[subject][2]["questions"].values()))
	else:
		raise Exception("Actions can only be 'questions' or 'length'")

<<<<<<< HEAD
=======
def get_question_keys(subject):
	return list(content[subject][2]["questions"].keys())

>>>>>>> 13483fca6ec6bf8c173c66f5cb2efe5300135b50
def get_option_type(subject):
	with open("Storage.json","r") as file:
		content = file.read()

	content = json.loads(content)
	return list(content[subject][1]["option_type"].values())

def get_options(subject):
	with open("Storage.json","r") as file:
		content = file.read()

	content = json.loads(content)
	return list(content[subject][3]["options"].values())

def get_answers(subject):
	with open("Storage.json","r") as file:
		content = file.read()

	content = json.loads(content)
	return list(content[subject][4]["answers"].values())

def add_subject(subject, details={}, option_type={}, questions={}, options={}, answers={}):
	with open("Storage.json","r") as file:
		content = file.read()

	content = json.loads(content)
	content.update({subject: [{"details":details}, {"option_type":option_type},{"questions":questions},{"options":options},{"answers":answers}]})

	with open("Storage.json","w") as file:
		content = json.dumps(content, indent=4)
		file.write(content)

def add_details(subject, details={}):
	with open("Storage.json", "r") as file:
		content = file.read()

	content = json.loads(content)
	content[subject][0]["details"].update(details)

	with open("Storage.json","w") as file:
		content = json.dumps(content, indent=4)
		file.write(content)

def add_option_type(subject, option_type={}):
	with open("Storage.json", "r") as file:
		content = file.read()

	content = json.loads(content)
	content[subject][1]["option_type"].update(option_type)

	with open("Storage.json","w") as file:
		content = json.dumps(content, indent=4)
		file.write(content)

def add_questions(subject, questions):
	with open("Storage.json", "r") as file:
		content = file.read()

	content = json.loads(content)
	content[subject][2]["questions"].update(questions)

	with open("Storage.json","w") as file:
		content = json.dumps(content, indent=4)
		file.write(content)

def add_options(subject, options={}):
	with open("Storage.json", "r") as file:
		content = file.read()

	content = json.loads(content)
	content[subject][3]["options"].update(options)

	with open("Storage.json","w") as file:
		content = json.dumps(content, indent=4)
		file.write(content)

def add_answers(subject, answers={}):
	with open("Storage.json", "r") as file:
		content = file.read()

	content = json.loads(content)
	content[subject][4]["answers"].update(answers)

	with open("Storage.json","w") as file:
		content = json.dumps(content, indent=4)
		file.write(content)

def change_subject_name(subject, new_subject):
	with open("Storage.json", "r") as file:
		content = file.read()

	content = json.loads(content)
	val = content[subject]
	content.update({new_subject:val})
	content[new_subject][0]["details"]["name"] = new_subject

	del content[subject]

	with open("Storage.json","w") as file:
		content = json.dumps(content, indent=4)
		file.write(content)

def change_subject_details(subject, time, marks):
	with open("Storage.json", "r") as file:
		content = file.read()

	content = json.loads(content)
	content[subject][0]["details"].update({"time":time})
	content[subject][0]["details"].update({"marks":marks})

	with open("Storage.json","w") as file:
		content = json.dumps(content, indent=4)
		file.write(content)

def change_question(subject, question):
	with open("Storage.json", "r") as file:
		content = file.read()

	content = json.loads(content)
	content[subject][2]["questions"][list(question.keys())[0]] = list(question.values())[0];

	with open("Storage.json","w") as file:
		content = json.dumps(content, indent=4)
		file.write(content)

def change_option_type(subject, option_type):
	with open("Storage.json", "r") as file:
		content = file.read()

	content = json.loads(content)
	content[subject][1]["option_type"][list(option_type.keys())[0]] = list(option_type.values())[0];

	with open("Storage.json","w") as file:
		content = json.dumps(content, indent=4)
		file.write(content)

def change_option(subject, option):
	with open("Storage.json", "r") as file:
		content = file.read()

	content = json.loads(content)
	content[subject][3]["options"][list(option.keys())[0]] = list(option.values())[0];

	with open("Storage.json","w") as file:
		content = json.dumps(content, indent=4)
		file.write(content)

def change_answer(subject, answer):
	with open("Storage.json", "r") as file:
		content = file.read()

	content = json.loads(content)
	content[subject][4]["answers"][list(answer.keys())[0]] = list(answer.values())[0];

	with open("Storage.json","w") as file:
		content = json.dumps(content, indent=4)
		file.write(content)

def add_before(subject, question_number, option_type={"Question 1":"Options"}, question={}, option={}, answer={}):
	with open("Storage.json", "r") as file:
		content = file.read()

	content = json.loads(content)

	#Options type
	keys = list(content[subject][1]["option_type"].keys())
	options_type = list(content[subject][1]["option_type"].values())

	keys = keys[question_number-1::]
	options_type =  options_type[question_number-1::]

	for _ in keys:
		del content[subject][1]["option_type"][_]

	content[subject][1]["option_type"].update(option_type)

	i = 0
	for _ in range(question_number +1, question_number + len(options_type) + 1):
		content[subject][1]["option_type"].update({f"Question {_}":f"{options_type[i]}"})
		i+=1

	#Questions
	keys = list(content[subject][2]["questions"].keys())
	questions = list(content[subject][2]["questions"].values())

	keys = keys[question_number-1::]
	questions =  questions[question_number-1::]

	for _ in keys:
		del content[subject][2]["questions"][_]

	content[subject][2]["questions"].update(question)
	
	i = 0
	for _ in range(question_number +1, question_number + len(questions) + 1):
		content[subject][2]["questions"].update({f"Question {_}":f"{questions[i]}"})
		i+=1

	#options
	if option != {}:
		keys = list(content[subject][3]["options"].keys())
		options = list(content[subject][3]["options"].values())

		keys = keys[question_number-1::]
		options =  options[question_number-1::]

		for _ in keys:
			del content[subject][3]["options"][_]

		content[subject][3]["options"].update(option)
		
		i = 0
		for _ in range(question_number +1, question_number + len(options) + 1):
			content[subject][3]["options"].update({f"Question {_}":options[i]})
			i+=1

	#Answers
	keys = list(content[subject][4]["answers"].keys())
	answers = list(content[subject][4]["answers"].values())

	keys = keys[question_number-1::]
	answers =  answers[question_number-1::]

	for _ in keys:
		del content[subject][4]["answers"][_]

	content[subject][4]["answers"].update(answer)
	
	i = 0
	for _ in range(question_number +1, question_number + len(answers) + 1):
		content[subject][4]["answers"].update({f"Question {_}":answers[i]})
		i+=1

	with open("Storage.json","w") as file:
		content = json.dumps(content, indent=4)
		file.write(content)

def add_after(subject, question_number, option_type, question, option, answer):
	with open("Storage.json", "r") as file:
		content = file.read()

	content = json.loads(content)

	#Option type
	keys = list(content[subject][1]["option_type"].keys())
	options_type = list(content[subject][1]["option_type"].values())

	keys = keys[question_number::]
	options_type = options_type[question_number::]

	for _ in keys:
		del content[subject][1]["option_type"][_]

	content[subject][1]["option_type"].update(option_type)

	i = 0
	for _ in range(question_number + 2, question_number + len(options_type) + 2):
		content[subject][1]["option_type"].update({f"Question {_}":options_type[i]})
		i+=1

	#Questions
	keys = list(content[subject][2]["questions"].keys())
	questions = list(content[subject][2]["questions"].values())

	keys = keys[question_number::]
	questions = questions[question_number::]

	for _ in keys:
		del content[subject][2]["questions"][_]

	content[subject][2]["questions"].update(question)

	i = 0
	for _ in range(question_number + 2, question_number + len(questions) + 2):
		content[subject][2]["questions"].update({f"Question {_}":questions[i]})
		i+=1

	#Options
	if option != {}:
		keys = list(content[subject][3]["options"].keys())
		options = list(content[subject][3]["options"].values())

		keys = keys[question_number::]
		options = options[question_number::]

		for _ in keys:
			del content[subject][3]["options"][_]

		content[subject][3]["options"].update(option)

		i = 0
		for _ in range(question_number + 2, question_number + len(options) + 2):
			content[subject][3]["options"].update({f"Question {_}":options[i]})
			i+=1

	#Answers
	keys = list(content[subject][4]["answers"].keys())
	answers = list(content[subject][4]["answers"].values())

	keys = keys[question_number::]
	answers = answers[question_number::]

	for _ in keys:
		del content[subject][4]["answers"][_]

	content[subject][4]["answers"].update(answer)

	i = 0
	for _ in range(question_number + 2, question_number + len(answers) + 2):
		content[subject][4]["answers"].update({f"Question {_}":answers[i]})
		i+=1
	
	with open("Storage.json","w") as file:
		content = json.dumps(content, indent=4)
		file.write(content)

def delete_question(subject, question_number):
	with open("Storage.json", "r") as file:
		content = file.read()

	content = json.loads(content)

	#Option type
	keys = list(content[subject][1]["option_type"].keys())
	options_type = list(content[subject][1]["option_type"].values())

	if len(options_type) != question_number:
		keys = keys[question_number::]
		options_type = options_type[question_number::]

		for _ in keys:
			del content[subject][1]["option_type"][_]

	elif len(options_type) == question_number:
		keys = keys[question_number-1::]
		options_type = options_type[question_number-1::]

		for _ in keys:
			del content[subject][1]["option_type"][_]

			options_type = options_type[question_number::]
		
	if len(options_type) != question_number:
		i = 0	
		for _ in range(question_number, question_number + len(options_type)):
			content[subject][1]["option_type"].update({f"Question {_}":options_type[i]})
			i+=1

	#Question
	keys = list(content[subject][2]["questions"].keys())
	questions = list(content[subject][2]["questions"].values())

	if len(questions) != question_number:
		keys = keys[question_number::]
		questions = questions[question_number::]

		for _ in keys:
			del content[subject][2]["questions"][_]

	elif len(questions) == question_number:
		keys = keys[question_number-1::]
		questions = questions[question_number-1::]

		for _ in keys:
			del content[subject][2]["questions"][_]

			questions = questions[question_number::]
		
	if len(questions) != question_number:
		i = 0	
		for _ in range(question_number, question_number + len(questions)):
			content[subject][2]["questions"].update({f"Question {_}":questions[i]})
			i+=1

	#Options
	keys = list(content[subject][3]["options"].keys())
	options = list(content[subject][3]["options"].values())

	if len(options) != question_number:
		keys = keys[question_number::]
		options = options[question_number::]

		for _ in keys:
			del content[subject][3]["options"][_]

	elif len(options) == question_number:
		keys = keys[question_number-1::]
		options = options[question_number-1::]

		for _ in keys:
			del content[subject][3]["options"][_]

			options = options[question_number::]
		
	if len(options) != question_number:
		i = 0	
		for _ in range(question_number, question_number + len(options)):
			content[subject][3]["options"].update({f"Question {_}":options[i]})
			i+=1

	#Answers
	keys = list(content[subject][4]["answers"].keys())
	answers = list(content[subject][4]["answers"].values())

	if len(answers) != question_number:
		keys = keys[question_number::]
		answers = answers[question_number::]

		for _ in keys:
			del content[subject][4]["answers"][_]

	elif len(answers) == question_number:
		keys = keys[question_number-1::]
		answers = answers[question_number-1::]

		for _ in keys:
			del content[subject][4]["answers"][_]

			answers = answers[question_number::]
		
	if len(answers) != question_number:
		i = 0	
		for _ in range(question_number, question_number + len(answers)):
			content[subject][4]["answers"].update({f"Question {_}":answers[i]})
			i+=1

	with open("Storage.json","w") as file:
		content = json.dumps(content, indent=4)
		file.write(content)

# add_before("Maths", 1, option_type={"Question 1":"sdonosnd"}, question={"Question 1": "aohdoaos"}, option={}, answer={"Question 1":"scscdsd"})