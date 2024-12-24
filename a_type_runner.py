import a_type_question_util
import a_type_comparison_util
import chatgpt_util
import df_builder
import chatgpt_util
import df_builder

def analyze_list(original_questions, prompts, original_answers):
    prompted_questions = a_type_question_util.convert_questions_to_prompted(original_questions, prompts)
    question_avg_dfs = []
    for i in range(len(original_questions)):
        question_dfs = []
        for k in range(2):
            gpt_answers = []
            for prompted_question in prompted_questions:
                question_gpt_answers = chatgpt_util.query_list_chatgpt(prompted_question)
                gpt_answers.append(question_gpt_answers)

            formatted_original_answers = []
            for original_answer in original_answers:
                formatted_original_answer = a_type_question_util.rephrase_a_type_answer(original_answer)
                formatted_original_answers.append(formatted_original_answer)

            formatted_gpt_answers = []
            for question_gpt_answers in gpt_answers:
                question_formatted_gpt_answers = a_type_question_util.rephrase_a_type_answer_list(question_gpt_answers)
                formatted_gpt_answers.append(question_formatted_gpt_answers)
            compares = []
            for j in range(len(prompts)):
                compare_json = a_type_comparison_util.compare_answers_chatgpt(formatted_original_answers[i], formatted_gpt_answers[i][j])
                compares.append(compare_json)
            result_df = df_builder.build_question_results_df(compares)
            question_dfs.append(result_df)
        avg_df = sum(question_dfs) / len(question_dfs)
        question_avg_dfs.append(avg_df)
        print(f"************** Average of Q{i} **************")
        print(avg_df)
    total_avg_df = sum(question_avg_dfs) / len(question_avg_dfs)
    print("************** Total average of all questions **************")
    print(total_avg_df)