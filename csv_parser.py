import pandas as pd

def get_questions_answers(type):
    # File path of the CSV file
    csv_file_path = 'path/to/your/file.csv'

    # Read the CSV file using pandas
    data = pd.read_csv(csv_file_path)

    # Filter rows based on conditions
    filtered_data = data[(data['question_type'] == type) &
                        (data['has_solution'] == 'TRUE') &
                        (data['question_translation_latex'] != 'na')]

    # Extract the lists
    question_latex_list = filtered_data['question_translation_latex'].tolist()
    answer_latex_list = filtered_data['answer_translation_latex'].tolist()

    return question_latex_list, answer_latex_list