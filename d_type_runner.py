import d_type_question_util
import chatgpt_util
import df_builder
import chatgpt_util
import df_builder
import pandas as pd

difficulty_csv_path = "questions_difficulty_rank\\type_d_difficulty_rank.csv"
questions_responses_data_directory_path = "questions_responses_data_type_d"
questions_results_directory_path = "questions_results_type_d"
questions_final_avg_path = "final_avg.csv"


def analyze_list(original_questions, prompts, original_answers):
    prompted_questions = d_type_question_util.convert_questions_to_prompted(original_questions, prompts)

    question_avg_dfs = []
    difficulty_list = []
    all_questions_responses_df = pd.DataFrame()
    for i in range(len(original_questions)):
        question_dfs = []
        question_responses_df = pd.DataFrame()
        for k in range(5):
            #gpt_answers = []
            #for prompted_question in prompted_questions:
            question_gpt_answers = d_type_question_util.rephrase_d_type_answer_list(prompted_questions[i])
            #    gpt_answers.append(question_gpt_answers)
            
            question_responses_iteration_df = pd.DataFrame({
                "Question Type": "D",
                "Question ID": i,
                "Iteration": k,
                "Question": original_questions[i],
                "Prompt" : prompts,
                "Prompted Question": prompted_questions[i],
                "LLM Multi-choice Answer": question_gpt_answers,
            })
            question_responses_df = pd.concat([question_responses_df, question_responses_iteration_df])
            
            
            compares = []
            for j in range(len(prompts)):
                compare_result = d_type_question_util.comapre_d_type(original_answers[i], question_gpt_answers[j])
                compares.append(compare_result)
            try:
                result_df = df_builder.build_question_results_df(compares,[],[],[],[],[], json=False, type='D')
                question_dfs.append(result_df)
            except:
                continue
        s = sum(question_dfs)
        l = len(question_dfs)
        if l > 0:
            avg_df = s / l 
            avg_df.to_csv(f"{questions_results_directory_path}\Q{i}.csv", index=False)
            question_avg_dfs.append(avg_df)
            print(f"************** Average of Q{i} **************")
            print(avg_df)
            difficulty_list.append([i, original_questions[i], 10 - (10*avg_df.values.mean())])
    
            question_responses_df.to_csv(f"{questions_responses_data_directory_path}\\Q{i}_responses_data.csv", index=False)
        all_questions_responses_df = pd.concat([all_questions_responses_df, question_responses_df])

    all_questions_responses_df.to_csv(f"{questions_responses_data_directory_path}\\questions_responses_data_final.csv", index=False)

    
    total_avg_df = sum(question_avg_dfs) / len(question_avg_dfs)
    total_avg_df.to_csv(f"{questions_results_directory_path}\\{questions_final_avg_path}", index=False)

    results_df = pd.DataFrame(difficulty_list, columns=["Question ID", "Question", "Difficulty"])
    results_df.to_csv(difficulty_csv_path, index=False)

    print("************** Total average of all questions **************")
    print(total_avg_df)