import chatgpt_util
import pandas as pd
import json

def comapre_d_type(answer_1, answer_2):
    query = f"""
                Compare the following strings: {answer_1}, {answer_2}
                answer me 1 if and only if the are identical
                otherwise, return 0
                no additional output
            """
    result = int(chatgpt_util.query_single_chatgpt(query))
    return result # the result is a json format

def rephrase_d_type_answer(original_question):
    prefix = """
                Which answer is correct? give me just the letter of the correct answer.
            """
    query = prefix + original_question
    result = chatgpt_util.query_single_chatgpt(query)
    return result

def rephrase_d_type_answer_list(original_questions):
    results = []
    for original_question in original_questions:
        result = rephrase_d_type_answer(original_question)
        results.append(result)
    return results

def convert_questions_to_prompted(questions, prompts):
    prompted_questions = []
    for question in questions:
        lst = []
        for prompt in prompts:
            lst.append(prompt + question)
        prompted_questions.append(lst)
    return prompted_questions


