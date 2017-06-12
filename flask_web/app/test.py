import json

def load_question():
	with open('../data/{0}'.format('NB_question_predict.json')) as data_file:
		data = json.load(data_file);
		
	with open('../data/{0}'.format('questions_nondup_dup.csv')) as data_file:
		question_id = [row['question_id'] for row in csv.DictReader(data_file)]

	missing = []
	

if __name__ == '__main__':
    load_question()