import b_type_question_util
import b_type_comparison_util
import chatgpt_util
import df_builder
import chatgpt_util
import df_builder
from concurrent.futures import ThreadPoolExecutor
import pandas as pd
import nli_util
import bleu_util

difficulty_csv_path = "questions_difficulty_rank\\type_b_difficulty_rank.csv"
questions_responses_data_directory_path = "questions_responses_data_type_b"
before_round_directory_path = "questions_results_before_round_type_b"
questions_results_directory_path = "questions_results_type_b"
questions_final_avg_path = "final_avg.csv"

value_to_word = {
        -1: 'Contradiction',
        0 : 'Neutral',
        1 : 'Entailment'
    }

def query_chatgpt_concurrently(prompted_questions):
    with ThreadPoolExecutor() as executor:
        gpt_answers = list(executor.map(chatgpt_util.query_single_chatgpt, prompted_questions))
    return gpt_answers

def rephrase_answers_concurrently(gpt_answers):
    with ThreadPoolExecutor() as executor:
        formatted_gpt_answers = list(executor.map(b_type_question_util.rephrase_b_type_answer, gpt_answers))
    return formatted_gpt_answers

def rephrase_original_answers_concurrently(original_answers):
    with ThreadPoolExecutor() as executor:
        formatted_original_answers = list(executor.map(b_type_question_util.rephrase_b_type_answer, original_answers))
    return formatted_original_answers





def analyze_list(original_questions, prompts, original_answers):
    prompted_questions = b_type_question_util.convert_questions_to_prompted(original_questions, prompts)
    question_avg_dfs = []
    
    print(f"starting formatting original answers")

    # formatted_original_answers = []
    # for original_answer in original_answers:
    #     formatted_original_answer = b_type_question_util.rephrase_b_type_answer(original_answer)
    #     formatted_original_answers.append(formatted_original_answer)
    
    formatted_original_answers = rephrase_original_answers_concurrently(original_answers)

    difficulty_list = []
    all_questions_responses_df = pd.DataFrame()
    model, tokenizer = nli_util.get_mode_tokenizer()
    for i in range(len(original_questions)):
        print(f"starting question {i}")
        question_dfs = []
        question_responses_df = pd.DataFrame()
        for k in range(5):
            # print(f"starting gpt_answers {i}")
            ######gpt_answers = []
            ###### for prompted_question in prompted_questions:
            #question_gpt_answers = chatgpt_util.query_list_chatgpt(prompted_questions[i]) # GOOD
            ######    gpt_answers.append(question_gpt_answers)

            question_gpt_answers = query_chatgpt_concurrently(prompted_questions[i])
            question_responses_iteration_df = pd.DataFrame({
                "Question Type": "B",
                "Question ID": i,
                "Iteration": k,
                "Question": original_questions[i],
                "Prompt" : prompts,
                "Prompted Question": prompted_questions[i],
                "LLM Answer": question_gpt_answers,
            })
            question_responses_df = pd.concat([question_responses_df, question_responses_iteration_df])


            # print(f"starting gpt format {i}")
            ######formatted_gpt_answers = []
            ######for question_gpt_answers in gpt_answers:
            # question_formatted_gpt_answers = b_type_question_util.rephrase_b_type_answer_list(question_gpt_answers) # GOOD
            ######    formatted_gpt_answers.append(question_formatted_gpt_answers)

            question_formatted_gpt_answers = rephrase_answers_concurrently(question_gpt_answers)


            compares = []
            nli_compares = []
            nli_entailment_probs = []
            nli_neutral_probs = []
            nli_contradiction_probs = []
            bleu_compares = []
            # print(f"starting compare format {i}")
            for j in range(len(prompts)):
                # DICE metric
                compare_json = b_type_comparison_util.compare_answers_chatgpt(formatted_original_answers[i], question_formatted_gpt_answers[j])
                compares.append(compare_json)

                # nli metric
                nli_result, probabilities = nli_util.nli_compare_promise_and_hypothesis(original_answers[i], question_gpt_answers[j], model, tokenizer)
                nli_compares.append(nli_result)
                nli_entailment_probs.append(probabilities['entailment'])
                nli_neutral_probs.append(probabilities['neutral'])
                nli_contradiction_probs.append(probabilities['contradiction'])
                
                # bleu metric
                bleu_result = bleu_util.compare_bleu(original_answers[i], question_gpt_answers[j])
                bleu_compares.append(bleu_result)
            try:
                result_df = df_builder.build_question_results_df(compares, nli_compares, nli_entailment_probs, nli_neutral_probs, nli_contradiction_probs , bleu_compares)
                question_dfs.append(result_df)
                # print(f"finished df {i}")
            except:
                continue

        if len(question_dfs) > 0:
            avg_df = sum(question_dfs) / len(question_dfs)
            avg_df.to_csv(f"{before_round_directory_path}\Q{i}.csv", index=False)
            question_avg_dfs.append(avg_df)
            print(f"************** Average of Q{i} **************")
            print(avg_df)
            difficulty_list.append([i, original_questions[i], 10 - avg_df.values.mean()])
        
        question_responses_df.to_csv(f"{questions_responses_data_directory_path}\\Q{i}_responses_data.csv", index=False)
        all_questions_responses_df = pd.concat([all_questions_responses_df, question_responses_df])

    all_questions_responses_df.to_csv(f"{questions_responses_data_directory_path}\\questions_responses_data_final.csv", index=False)

    total_avg_df = sum(question_avg_dfs) / len(question_avg_dfs)
    total_avg_df['NLI Result'] = total_avg_df['NLI Result'].round().map(value_to_word)
    total_avg_df.to_csv(f"{questions_results_directory_path}\\{questions_final_avg_path}", index=False)

    results_df = pd.DataFrame(difficulty_list, columns=["Question ID", "Question", "Difficulty"])
    results_df.to_csv(difficulty_csv_path, index=False)

    for i, quest_df in enumerate(question_avg_dfs):
        quest_df['NLI Result'] = quest_df['NLI Result'].round().map(value_to_word)
        quest_df.to_csv(f"{questions_results_directory_path}\Q{i}.csv", index=False)


    print("************** Total average of all questions **************")
    print(total_avg_df)


    

