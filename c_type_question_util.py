import chatgpt_util
import pandas as pd
import json
from concurrent.futures import ThreadPoolExecutor


def comapre_c_type(answer_1 = "", answer_2 = ""):
    query = f"""
                Compare the following strings: {answer_1}, {answer_2}
                answer me 1 if and only if the are identical
                otherwise, return 0
                if from some reason you can not compare them,
                or if one of them or both does not exist or empty, return 0.
                no additional output
            """
    try:
        result = int(chatgpt_util.query_single_chatgpt(query))
    except:
        result = 0
    return result # the result is a json format

def compare_letters(original_letter, gpt_letters):
    results = []
    for i in range(len(gpt_letters)):
        if (gpt_letters[i].lower()).startswith(original_letter.lower()):
            results.append(1)
        else:
            results.append(0)
    return results
        
def compare_sentences(original_sentence, gpt_sentence):
    results = []
    prefix = f"""
            Compare the following sentences in both semantic and syntax,
            Your answer need to be just a real number between 0 and 1 which evaluate the semantic simmilarity
            Ff for some reason you can not compare them,
            or if one of them or both does not exist or empty, return 0.
            """
    for i in range(len(gpt_sentence)):
        query = prefix + f""" Sentence1: {original_sentence}; Sentence2: {gpt_sentence[i]}"""
        try:
            result = float(chatgpt_util.query_single_chatgpt(query))
        except:
            result = 0
        results.append(result)
    
    return results

# def parse_letters_sentences_list(gpt_answers):
#     explanations = []
#     selected_options = []

#     # Process each string in the input list
#     for item in gpt_answers:
#         # Split the input into lines
#         lines = item.split("\n")

#         # Extract the selected option
#         for line in lines:
#             if line.startswith("Option selected: "):
#                 selected_options.append(line.replace("Option selected: ", "").strip())

#             # Extract the explanation
#             elif line.startswith("Explanation: "):
#                 explanations.append(line.replace("Explanation: ", "").strip())

#             else:
#                 if len(selected_options) > len(explanations):
#                     explanations.append("")
#                 else:
#                     selected_options.append("")

#     return selected_options, explanations

def parse_letters_sentences_list(gpt_answers):
    explanations = []
    selected_options = []

    # Process each string in the input list
    for item in gpt_answers:
        # Initialize flags to track if an option and explanation are found in the current item
        found_option = False
        found_explanation = False

        # Check if the item contains newlines; if not, treat it as a single line
        lines = item.split("\n") if "\n" in item else [item]

        # Extract the selected option and explanation
        for line in lines:
            if line.startswith("Option selected: "):
                option = line.replace("Option selected: ", "").strip()
                # Validate that the option is a single letter
                if len(option) == 1 and option.isalpha():
                    selected_options.append(option)
                else:
                    selected_options.append(" ")
                found_option = True

            elif line.startswith("Explanation: "):
                explanations.append(line.replace("Explanation: ", "").strip())
                found_explanation = True

        # If no option was found, append an empty string to maintain array length
        if not found_option:
            selected_options.append(" ")

        # If no explanation was found, append an empty string to maintain array length
        if not found_explanation:
            explanations.append(" ")

    return selected_options, explanations

    


def query_c_type_question(original_question):
    query = f"""
                Answer the question provided. From now on, refer to your answer as "hypothesis." Next, make the hypothesis more concise (maximum 30 words). Refer to this concise version as "LLM Answer."

                Based on the "LLM Answer," choose the option that logically follows or is entailed by it. Provide your answer in the following format, including a brief explanation:

                Option selected: [letter of correct option]
                Explanation: [1 sentence explaining why this option follows from "LLM Answer"]

                Always respond in this exact format.
            """
    query = query + original_question
    result = chatgpt_util.query_single_chatgpt(query)
    return result # the result is a json format

# def query_c_type_questions_list(prompted_question):
#     results = []
#     for prompt_question in prompted_question:
#         result = query_c_type_question(prompt_question)
#         results.append(result)
#     return results 


def query_c_type_questions_list_conccurently(prompted_question):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(query_c_type_question, prompted_question))
    return results



def convert_questions_to_prompted(questions, prompts):
    # prompted_questions = []
    # for question in questions:
    #     lst = []
    #     for prompt in prompts:
    #         lst.append(prompt + question)
    #     prompted_questions.append(lst)
    prompted_questions = convert_questions_to_prompted_concurrently(questions, prompts)
    return prompted_questions

def convert_questions_to_prompted_concurrently(questions, prompts):
    def combine_with_prompts(question):
        return [prompt + question for prompt in prompts]
    
    with ThreadPoolExecutor() as executor:
        prompted_questions = list(executor.map(combine_with_prompts, questions))
    return prompted_questions
