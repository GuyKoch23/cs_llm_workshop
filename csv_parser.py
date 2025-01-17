import pandas as pd
import random

def get_questions_answers(type, path):
    csv_file_path = path
    data = pd.read_csv(csv_file_path, encoding='latin1')

    if type == "D":
        filtered_data = data[
            (
            ((data['question_type'] == 'D')
            | (data['question_type'] == 'd'))
            & (data['has_solution'] == True)
            & (data['multiple_choice_answer'] != "FALSE")
            & (data['multiple_choice_answer'] != "1")
            & (data['multiple_choice_answer'] != "2")
            & (data['multiple_choice_answer'] != "3")
            & (data['multiple_choice_answer'] != "4")
            & (data['multiple_choice_answer'] != "5")
            & (data['multiple_choice_answer'] != "6")
            & (data['dataset'] == "tested")
            & (data['question_translation_latex'] != 'na')
            & (data['multiple_choice_answer'] != 'na')
            )
        ]
        relevant_data_indexes = filtered_data.index.tolist()

        random.seed(1337)
        d_type_2_3 = random.sample(relevant_data_indexes, int(len(relevant_data_indexes)*2/3))
        d_type_1_3 = list(set(relevant_data_indexes) - set(d_type_2_3))

        relevant_2_3_rows = filtered_data.loc[d_type_2_3]
        relevant_1_3_rows = filtered_data.loc[d_type_1_3]

        question_latex_list_2_3 = relevant_2_3_rows['question_translation_latex'].tolist()
        multiple_choice_list_2_3 = relevant_2_3_rows['multiple_choice_answer'].tolist()

        question_latex_list_1_3 = relevant_1_3_rows['question_translation_latex'].tolist()
        multiple_choice_list_1_3 = relevant_1_3_rows['multiple_choice_answer'].tolist()

        return question_latex_list_2_3, multiple_choice_list_2_3, question_latex_list_1_3, multiple_choice_list_1_3
    

    if type == "C":
        filtered_data = data[
            (
            ((data['question_type'] == 'C')
            | (data['question_type'] == 'c')) 
            & (data['has_solution'] == True)
            & (data['multiple_choice_answer'] != "FALSE")
            & (data['multiple_choice_answer'] != "1")
            & (data['multiple_choice_answer'] != "2")
            & (data['multiple_choice_answer'] != "3")
            & (data['multiple_choice_answer'] != "4")
            & (data['multiple_choice_answer'] != "5")
            & (data['multiple_choice_answer'] != "6")
            & (data['dataset'] == "tested")
            & (data['question_translation_latex'] != 'na')
            & (data['multiple_choice_answer'] != 'na')
            & (data['answer_translation_latex'] != 'na')
            )
        ]
        relevant_data_indexes = filtered_data.index.tolist()

        random.seed(1337)
        c_type_2_3 = random.sample(relevant_data_indexes, int(len(relevant_data_indexes)*2/3))
        c_type_1_3 = list(set(relevant_data_indexes) - set(c_type_2_3))

        relevant_2_3_rows = filtered_data.loc[c_type_2_3]
        relevant_1_3_rows = filtered_data.loc[c_type_1_3]

        question_latex_list_2_3 = relevant_2_3_rows['question_translation_latex'].tolist()
        multiple_choice_list_2_3 = relevant_2_3_rows['multiple_choice_answer'].tolist()
        answer_latex_list_2_3 = relevant_2_3_rows['answer_translation_latex'].tolist()

        question_latex_list_1_3 = relevant_1_3_rows['question_translation_latex'].tolist()
        multiple_choice_list_1_3 = relevant_1_3_rows['multiple_choice_answer'].tolist()
        answer_latex_list_1_3 = relevant_1_3_rows['answer_translation_latex'].tolist()

        return question_latex_list_2_3, multiple_choice_list_2_3, answer_latex_list_2_3, question_latex_list_1_3, multiple_choice_list_1_3, answer_latex_list_1_3
    
    if type == "B":
            relevant_data = data[
                (
                (data['question_type'] == type)
                & (data['is_relevant'] == True)  
                & (data['has_solution'] == True)
                & (data['dataset'] == "tested")
                & (data['question_translation_latex'] != 'na')
                & (data['answer_translation_latex'] != 'na')
                )
            ]

            relevant_data_indexes = relevant_data.index.tolist()
    
            random.seed(1337)
            b_type_2_3 = random.sample(relevant_data_indexes, int(len(relevant_data_indexes)*2/3))
            b_type_1_3 = list(set(relevant_data_indexes) - set(b_type_2_3))

            relevant_2_3_rows = relevant_data.loc[b_type_2_3]
            relevant_1_3_rows = relevant_data.loc[b_type_1_3]

            question_latex_list_2_3 = relevant_2_3_rows['question_translation_latex'].tolist()
            question_latex_list_1_3 = relevant_1_3_rows['question_translation_latex'].tolist()
            answer_latex_list_2_3 = relevant_2_3_rows['answer_translation_latex'].tolist()
            answer_latex_list_1_3 = relevant_1_3_rows['answer_translation_latex'].tolist()

            return question_latex_list_2_3, question_latex_list_1_3, answer_latex_list_2_3, answer_latex_list_1_3
    
    if type == "A":
        relevant_data = data[
            (
            ((data['question_type'] == 'A')
            | (data['question_type'] == 'a'))  
            & (data['is_relevant'] == True)  
            & (data['has_solution'] == True)
            & (data['question_translation_latex'] != 'na')
            & (data['answer_translation_latex'] != 'na')
            )
        ]

        relevant_data_indexes = relevant_data.index.tolist()
        other_team_2_3, other_team_1_3 = get_2_3_questions()
        other_team = list(set(other_team_2_3).union(set(other_team_1_3)))

        relevant_no_other_team = list(set(relevant_data_indexes) - set(other_team))
        
        random.seed(1337)
        relevant_no_other_team_2_3 = random.sample(relevant_no_other_team, int(len(relevant_no_other_team)*2/3))
        relevant_no_other_team_1_3 = list(set(relevant_no_other_team) - set(relevant_no_other_team_2_3))
        
        relevant_other_team_2_3 = list(set(other_team_2_3).intersection(set(relevant_data_indexes)))
        relevant_other_team_1_3 = list(set(other_team_1_3).intersection(set(relevant_data_indexes)))

        relevant_2_3 = list(set(relevant_no_other_team_2_3).union((relevant_other_team_2_3)))
        relevant_1_3 = list(set(relevant_no_other_team_1_3).union(set(relevant_other_team_1_3)))

        relevant_2_3_rows = relevant_data.loc[relevant_2_3]
        relevant_1_3_rows = relevant_data.loc[relevant_1_3]


        question_latex_list_2_3 = relevant_2_3_rows['question_translation_latex'].tolist()
        question_latex_list_1_3 = relevant_1_3_rows['question_translation_latex'].tolist()
        answer_latex_list_2_3 = relevant_2_3_rows['answer_translation_latex'].tolist()
        answer_latex_list_1_3 = relevant_1_3_rows['answer_translation_latex'].tolist()

        return question_latex_list_2_3, question_latex_list_1_3, answer_latex_list_2_3, answer_latex_list_1_3

def get_2_3_questions():
    lst = [882, 881, 870, 865, 859, 858, 857, 852, 850, 849, 841, 838, 786, 785, 784, 783, 782, 781, 780, 779, 778, 777, 688, 687, 686, 658, 656, 655, 654, 653, 652, 651 ]
    lst += [51, 62, 63, 99, 121, 155, 164, 504, 520, 521, 522, 523, 524, 526, 527, 532 ,533, 534]
    lst += [86,87,88,89,90,91,92,93,94,95,96,98,106,107,108,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,140,141,142,143,144,148]

    random.seed(1337)
    subset = random.sample(lst, int(len(lst)*2/3))
    not_sampled = list(set(lst) - set(subset))

    return subset, not_sampled



