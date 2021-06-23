subjects = {
	"математика": [],
	"информатика": [10, 10, 10],
	"русск. яз.": [],
	"русск. лит.": [10, 9, 9, 10, 10],
	"бел. яз.": [],
	"бел. лит.": [10, 9, 9, 10, 10],
	"физика": [10, 8, 10, 10, 10],
	"химия": [9, 8, 8, 10, 9],
	"биология": [],
	"всем. история": [10, 10, 9],
	"история Бел.": [9, 9, 10],
	"обществов.": [10, 10],
	"география": [],
	"англ. яз.": [9, 9, 8, 10, 10, 9],
}


def add_marks(subject: str, marks: list):
	try:
		subjects[subject] += marks
	except KeyError:
		print("Нет такого предмета!")

def get_subject_average_score(subject: str):
	try:
		marks = subjects[subject]
	except KeyError:
		return "Нет такого предмета"

	total_score = sum(marks)
	try:
		average_score = total_score / len(marks)
	except ZeroDivisionError:
		return 0

	return average_score

def get_total_average_score():
	total_score = 0

	for subject in subjects:
		total_score += round(get_subject_average_score(subject))

	return round(total_score / len(subjects), 2)



