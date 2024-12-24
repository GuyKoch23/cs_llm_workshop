import c_type_question_util
import chatgpt_util
import df_builder
import chatgpt_util
import df_builder

def analyze_list(original_questions, prompts, original_answers_letters, original_answers_sentences):
    prompted_questions = c_type_question_util.convert_questions_to_prompted(original_questions, prompts)
    
    question_avg_dfs = []
    for i in range(len(original_questions)):
        question_dfs = []
        for k in range(5):
            gpt_answers = []
            for prompted_question in prompted_questions:
                question_gpt_answers = c_type_question_util.query_c_type_questions_list(prompted_question)
                gpt_answers.append(question_gpt_answers)
            gpt_prompt_letters, gpt_prompt_sentences = c_type_question_util.parse_letters_sentences_list(gpt_answers[i])
            letter_compares = c_type_question_util.compare_letters(original_answers_letters[i], gpt_prompt_letters)
            int_letter_compares = [int(element) for element in letter_compares]
            sentence_compares = c_type_question_util.compare_sentences(original_answers_sentences[i], gpt_prompt_sentences)
            float_sentence_compares = [float(element) for element in sentence_compares]
            result_df = df_builder.build_question_results_df([int_letter_compares, float_sentence_compares],json=False, type='C')
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