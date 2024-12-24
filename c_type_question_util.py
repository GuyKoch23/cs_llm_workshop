import chatgpt_util
import pandas as pd
import json

def comapre_c_type(answer_1, answer_2):
    query = f"""
                Compare the following strings: {answer_1}, {answer_2}
                answer me 1 if and only if the are identical
                otherwise, return 0
                no additional output
            """
    result = int(chatgpt_util.query_single_chatgpt(query))
    return result # the result is a json format

def compare_letters(original_letter, gpt_letters):
    results = []
    for i in range(len(gpt_letters)):
        if gpt_letters[i].startswith(original_letter):
            results.append(1)
        else:
            results.append(0)
    return results
        
def compare_sentences(original_sentence, gpt_sentence):
    results = []
    prefix = f"""
            Compare the following sentences in both semantic and syntax,
            Your answer need to be just a real number between 0 and 1 which evaluate the semantic simmilarity
            """
    for i in range(len(gpt_sentence)):
        query = prefix + f""" Sentence1: {original_sentence}; Sentence2: {gpt_sentence[i]}"""
        result = chatgpt_util.query_single_chatgpt(query)
        results.append(result)
    
    return results

def parse_letters_sentences_list(gpt_answers):
    explanations = []
    selected_options = []

    # Process each string in the input list
    for item in gpt_answers:
        # Split the input into lines
        lines = item.split("\n")

        # Extract the selected option
        for line in lines:
            if line.startswith("Option selected: "):
                selected_options.append(line.replace("Option selected: ", "").strip())

            # Extract the explanation
            elif line.startswith("Explanation: "):
                explanations.append(line.replace("Explanation: ", "").strip())

    return selected_options, explanations
    


def query_c_type_question(original_question):
    query = f"""
                Answer the following question. 
                From now on we will refer to your answer to the question using the word "hypothesis"
                Make the hypothesis from instruction 1 more concise, at most 30 words. From now on we will refer to your answer to the question using the word "LLM Answer" 
                
                Based on "LLM Answer" Select the option that entails from "LLM Answer".
                The option you chose should be one letter for the correct answer include 1 line of explanation of why you chose this option based on "LLM Answer", here is an example of your output:

                Option selected: b
                Explanation: The question requires a balanced tree data structure, option b consists of such data structure
                
                This should be the only text in your response and no more
            """
    query = query + original_question
    result = chatgpt_util.query_single_chatgpt(query)
    return result # the result is a json format

def query_c_type_questions_list(original_questions):
    results = []
    for original_question in original_questions:
        result = query_c_type_question(original_question)
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


