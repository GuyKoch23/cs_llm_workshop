import a_type_question_util
import chatgpt_util
import a_type_comparison_util
import json_util
import df_builder
import b_type_runner
import d_type_runner
import a_type_runner
import c_type_runner
import csv_parser

def run_A(questions, answers, prompts):
    a_type_runner.analyze_list(questions, prompts, answers)

def run_B(questions, answers, prompts):
    b_type_runner.analyze_list(questions, prompts, answers)

def run_C(questions, answers_letters, answers_sentences, prompts):
    c_type_runner.analyze_list(questions, prompts, answers_letters, answers_sentences)

def run_D(questions, answers_letters, prompts):
    d_type_runner.analyze_list(questions, prompts, answers_letters)



def main():
    path = "C:\\Guy\\Education\\TAU\\Year3\\Workshop\\output.csv"
    
    prompts = [
            "",
            """In the following question justify the data structure you have chosen for this problem. Explain why it is the most appropriate solution compared to other alternatives, considering the specific operations required. Limit your answer to 100-150 words""",
            """In the following question consider the required methods for the data structure. Focus on those methods,  and find the best suitable implementation. The latter takes priority over any other requirements. Limit your answer to 100-150 words""",
            """In the following question provide the time complexities for the main operations (e.g., insertion, deletion, search, access) on the chosen data structure. Be sure to explain how the complexities are derived. Limit your answer to 100-150 words""",
            """You are a hard-working, average-level third-year undergraduate student in computer science. Your role is to eagerly learn, share your understanding of topics from your coursework, and contribute a fresh perspective to the discussion. Limit your answer to 100-150 words""",
            """You are a highly intelligent professor specializing in data structures. Your role is to explain advanced concepts with clarity, provide deep insights, and challenge others with thought-provoking questions, while also making technical ideas approachable for less experienced participants. Limit your answer to 100-150 words""",
            """You are a curious and imaginative 3-year-old child. Your role is to ask simple and wonder-filled questions, offer playful or creative observations, and spark fresh perspectives in the discussion through your natural sense of curiosity. Limit your answer to 100-150 words""",
            """You are Robert Tarjan, a legendary computer scientist renowned for your groundbreaking contributions to algorithms and data structures. Your role is to bring theoretical depth, share innovative ideas, and engage with others constructively, tailoring your insights to match the group’s diverse expertise levels. Limit your answer to 100-150 words""",
            """You are Geoffrey Hinton, a pioneering researcher in artificial intelligence and neural networks. Your role is to share cutting-edge knowledge, highlight the relevance of AI to the discussion, and inspire curiosity and innovation in others through your visionary ideas. Limit your answer to 100-150 words""",
            """You are Hans Peter Luhn, a historical computer scientist known for your foundational work in information retrieval and text analysis. Your role is to offer historical context, connect your past innovations to modern advancements, and provide a foundational perspective to the discussion. Limit your answer to 100-150 words""",
            """Answer the following question, let's think step by step. Limit your answer to 100-150 words""",
            """Answer the following question and then go over your solution and improve it according to the requirements. Limit your answer to 100-150 words""",
            """Break the following question into smaller, simpler problems, then solve them one after another and then answer the original question. Limit your answer to 100-150 words""",
            """In the following questions, find the most important topics and ignore other parts which distract you. Answer to the point according to the relevant parts. Limit your answer to 100-150 words""",
        ]   
    
    a_question_latex_list_2_3, a_question_latex_list_1_3, a_answer_latex_list_2_3, a_answer_latex_list_1_3 = csv_parser.get_questions_answers("A", path)
    #b_question_latex_list_2_3, b_question_latex_list_1_3, b_answer_latex_list_2_3, b_answer_latex_list_1_3 = csv_parser.get_questions_answers("B", path)
    #c_question_latex_list_2_3, c_multiple_choice_list_2_3, c_answer_latex_list_2_3, c_question_latex_list_1_3, c_multiple_choice_list_1_3, c_answer_latex_list_1_3 = csv_parser.get_questions_answers("C", path)
    #d_question_latex_list_2_3, d_multiple_choice_list_2_3, d_question_latex_list_1_3, d_multiple_choice_list_1_3 = csv_parser.get_questions_answers("D", path)

    run_A(a_question_latex_list_2_3, a_answer_latex_list_2_3, prompts)
    #run_B(b_question_latex_list_2_3, b_answer_latex_list_2_3, prompts)
    #run_C(c_question_latex_list_2_3, c_multiple_choice_list_2_3, c_answer_latex_list_2_3, prompts)
    #run_D(d_question_latex_list_2_3, d_multiple_choice_list_2_3, prompts)
    

if __name__ == '__main__':
    main()
