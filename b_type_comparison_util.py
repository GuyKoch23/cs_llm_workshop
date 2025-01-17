import chatgpt_util
import pandas as pd
import json

def compare_answers_chatgpt(promise_answer, hypothesis_answer):
    query = f"""
            ### Evaluation Prompt
            Please provide the promise (ground truth) and hypothesis (LLM-generated answer) for the data structure question. I will evaluate the hypothesis by comparing it to the promise using the following criteria:

            | Criteria             | Description                                                                 | Score Range | Evaluation Notes                        |
            |----------------------|-----------------------------------------------------------------------------|-------------|-----------------------------------------|
            | Data Structure Choice | Is the chosen data structure in the hypothesis consistent with the promise?   | 1–10       | Explanation of how well the data structure aligns with the requirements and promise. |
            | Implementation        | Is the hypothesis logically accurate and aligned with the promise?             | 1–10       | Explanation of correctness in implementation, logic, and problem-solving approach. |
            | Time Complexity       | Is the time complexity in the hypothesis consistent with the promise?          | 1–10       | Explanation of how well the time complexity aligns with the promise. |
            
            ### Scoring Guidance:
            - 1 (Very Poor): Severe inaccuracies, fundamentally incorrect, or completely irrelevant.
            - 2 (Poor): Major flaws or misunderstandings, barely aligns with the promise.
            - 3 (Below Average): Significant issues, though partially related or relevant.
            - 4 (Fair): Noticeable gaps or errors, but somewhat aligned with the promise.
            - 5 (Average): Basic alignment, with both correct and incorrect aspects; improvements needed.
            - 6 (Above Average): Mostly correct with minor flaws; demonstrates adequate understanding.
            - 7 (Good): Largely accurate and aligned with the promise, with minor refinements required.
            - 8 (Very Good): Accurate, well-reasoned, and closely aligned with the promise, with minor gaps.
            - 9 (Excellent): Near-perfect, optimal, and meets all aspects of the promise effectively.
            - 10 (Outstanding): Exceeds the promise with exemplary clarity, correctness, and optimization.

            ### How It Works
            1. **Promise**: {promise_answer}
            2. **Hypothesis**: {hypothesis_answer}
            3. The result will be provided in the following JSON format:


            "DataStructureChoice":
                "score": <1-10>,
                "notes": "Explanation of how well the data structure in the hypothesis matches the promise."
            ,
            "Implementation":
                "score": <1-10>,
                "notes": "Explanation of how logically accurate and aligned the hypothesis is with the promise."
            ,
            "TimeComplexity":
                "score": <1-10>,
                "notes": "Explanation of how the time complexity in the hypothesis compares to the promise."
        
            """
    result = chatgpt_util.query_single_chatgpt(query, json=True)
    return result # the result is a json format
