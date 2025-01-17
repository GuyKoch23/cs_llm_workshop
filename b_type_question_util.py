import chatgpt_util
from concurrent.futures import ThreadPoolExecutor

def rephrase_b_type_answer(original_question):
    prefix = """
                Read the following answer delimited by triple backticks: ```{answer}```
                Parse the answer to the following format without adding any data that is not in the answer:
                - Data structure used: 
                - Analysis:
                - Complexity:
            """
    query = prefix + original_question
    result = chatgpt_util.query_single_chatgpt(query)
    return result

def rephrase_b_type_answer_list(original_questions):
    # results = []
    # for original_question in original_questions:
    #     result = rephrase_b_type_answer(original_question)
    #     results.append(result)
    results = rephrase_b_type_answer_list_concurrently(original_questions)
    return results


def rephrase_b_type_answer_list_concurrently(original_questions):
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(rephrase_b_type_answer, original_questions))
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