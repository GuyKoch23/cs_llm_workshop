import chatgpt_util
import pandas as pd
import json
from concurrent.futures import ThreadPoolExecutor


def comapre_d_type(original_letter, gpt_letter):
    # query = f"""
    #             Compare the following strings: {answer_1}, {answer_2}
    #             answer me 1 if and only if the are identical
    #             otherwise, return 0
    #             no additional output
    #         """
    # result = int(chatgpt_util.query_single_chatgpt(query))
    if (gpt_letter.lower()).startswith(original_letter.lower()):
        result = 1
    else:
        result = 0
    return result # the result is a json format


def rephrase_d_type_answer(original_question):
    prefix = """Read the following question and choose from the correct letter from the options in the question. give me just the letter of the correct answer and no more charecters."""
    query = prefix + original_question
    result = chatgpt_util.query_single_chatgpt(query)
    return result


def rephrase_d_type_answer_list_concurrently(original_questions):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(rephrase_d_type_answer, original_questions))
    return results

def rephrase_d_type_answer_list(original_questions):
    # results = []
    # for original_question in original_questions:
    #     result = rephrase_d_type_answer(original_question)
    #     results.append(result)
    results = rephrase_d_type_answer_list_concurrently(original_questions)
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
