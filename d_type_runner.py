import d_type_question_util
import chatgpt_util
import df_builder
import chatgpt_util
import df_builder

def analyze_list(original_questions, prompts, original_answers):
    prompted_questions = d_type_question_util.convert_questions_to_prompted(original_questions, prompts)


    question_avg_dfs = []
    for i in range(len(original_questions)):
        question_dfs = []
        for k in range(2):
            gpt_answers = []
            for prompted_question in prompted_questions:
                question_gpt_answers = d_type_question_util.rephrase_d_type_answer_list(prompted_question)
                gpt_answers.append(question_gpt_answers)
            compares = []
            for j in range(len(prompts)):
                compare_result = d_type_question_util.comapre_d_type(original_answers[i], gpt_answers[i][j])
                compares.append(compare_result)
            result_df = df_builder.build_question_results_df(compares, json=False, type='D')
            question_dfs.append(result_df)
        s = sum(question_dfs)
        l = len(question_dfs)
        avg_df = s / l 
        question_avg_dfs.append(avg_df)
        print(f"************** Average of Q{i} **************")
        print(avg_df)
    total_avg_df = sum(question_avg_dfs) / len(question_avg_dfs)
    print("************** Total average of all questions **************")
    print(total_avg_df)