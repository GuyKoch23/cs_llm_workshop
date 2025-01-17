import c_type_question_util
import chatgpt_util
import df_builder
import chatgpt_util
import df_builder
import pandas as pd
import nli_util
import bleu_util

difficulty_csv_path = "questions_difficulty_rank\\type_c_difficulty_rank.csv"
questions_responses_data_directory_path = "questions_responses_data_type_c"
before_round_directory_path = "questions_results_before_round_type_c"
questions_results_directory_path = "questions_results_type_c"
questions_final_avg_path = "final_avg.csv"

value_to_word = {
        -1: 'Contradiction',
        0 : 'Neutral',
        1 : 'Entailment'
    }

def analyze_list(original_questions, prompts, original_answers_letters, original_answers_sentences):
    model, tokenizer = nli_util.get_mode_tokenizer()
    prompted_questions = c_type_question_util.convert_questions_to_prompted(original_questions, prompts)
    
    question_avg_dfs = []
    difficulty_list = []
    all_questions_responses_df = pd.DataFrame()
    for i in range(len(original_questions)):
        question_dfs = []
        question_responses_df = pd.DataFrame()
        for k in range(5):
            # gpt_answers = []
            # for prompted_question in prompted_questions:
            try:
                question_gpt_answers = c_type_question_util.query_c_type_questions_list_conccurently(prompted_questions[i])
                    #gpt_answers.append(question_gpt_answers)
                gpt_prompt_letters, gpt_prompt_sentences = c_type_question_util.parse_letters_sentences_list(question_gpt_answers)
                
                question_responses_iteration_df = pd.DataFrame({
                    "Question Type": "C",
                    "Question ID": i,
                    "Iteration": k,
                    "Question": original_questions[i],
                    "Prompt" : prompts,
                    "Prompted Question": prompted_questions[i],
                    "LLM Multi-choice Answer": gpt_prompt_letters,
                    "LLM Sentence Answer": gpt_prompt_sentences,
                })
                question_responses_df = pd.concat([question_responses_df, question_responses_iteration_df])
                
                nli_compares = []
                nli_entailment_probs = []
                nli_neutral_probs = []
                nli_contradiction_probs = []
                bleu_compares = []
                for j in range(len(prompts)):

                    # nli metric
                    nli_result, probabilities = nli_util.nli_compare_promise_and_hypothesis(original_answers_sentences[i], gpt_prompt_sentences[j], model, tokenizer)
                    nli_compares.append(nli_result)
                    nli_entailment_probs.append(probabilities['entailment'])
                    nli_neutral_probs.append(probabilities['neutral'])
                    nli_contradiction_probs.append(probabilities['contradiction'])
                    
                    # bleu metric
                    bleu_result = bleu_util.compare_bleu(original_answers_sentences[i], gpt_prompt_sentences[j])
                    bleu_compares.append(bleu_result)

                letter_compares = c_type_question_util.compare_letters(original_answers_letters[i], gpt_prompt_letters)
                int_letter_compares = [int(element) for element in letter_compares]
                sentence_compares = c_type_question_util.compare_sentences(original_answers_sentences[i], gpt_prompt_sentences)
                float_sentence_compares = [float(element) for element in sentence_compares]
                try:
                    result_df = df_builder.build_question_results_df([int_letter_compares, float_sentence_compares], nli_compares, nli_entailment_probs, nli_neutral_probs, nli_contradiction_probs, bleu_compares,json=False, type='C')
                    question_dfs.append(result_df)
                    # print(f"finished df {i}")
                except:
                    continue
            except Exception as e:
                print(f"######### Exception in question {i} iter {k} #########")
                continue
        s = sum(question_dfs)
        l = len(question_dfs)
        if l > 0:
            avg_df = s / l 
            avg_df.to_csv(f"{before_round_directory_path}\Q{i}.csv", index=False)
            question_avg_dfs.append(avg_df)
            print(f"************** Average of Q{i} **************")
            print(avg_df)
            difficulty_list.append([i, original_questions[i], 10 - (10*avg_df.values.mean())])

        question_responses_df.to_csv(f"{questions_responses_data_directory_path}\\Q{i}_responses_data.csv", index=False)
        all_questions_responses_df = pd.concat([all_questions_responses_df, question_responses_df])

    all_questions_responses_df.to_csv(f"{questions_responses_data_directory_path}\\questions_responses_data_final.csv", index=False)

    total_avg_df = sum(question_avg_dfs) / len(question_avg_dfs)
    total_avg_df['NLI (Sentence)'] = total_avg_df['NLI (Sentence)'].round().map(value_to_word)
    total_avg_df.to_csv(f"{questions_results_directory_path}\\{questions_final_avg_path}", index=False)

    for i, quest_df in enumerate(question_avg_dfs):
        quest_df['NLI (Sentence)'] = quest_df['NLI (Sentence)'].round().map(value_to_word)
        quest_df.to_csv(f"{questions_results_directory_path}\Q{i}.csv", index=False)

    results_df = pd.DataFrame(difficulty_list, columns=["Question ID", "Question", "Difficulty"])
    results_df.to_csv(difficulty_csv_path, index=False)
    print("************** Total average of all questions **************")
    print(total_avg_df)