import chatgpt_util

def rephrase_a_type_answer(original_question):
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

def rephrase_a_type_answer_list(original_questions):
    results = []
    for original_question in original_questions:
        result = rephrase_a_type_answer(original_question)
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

