import a_type_question_util
import chatgpt_util
import a_type_comparison_util
import json_util
import df_builder
import d_type_runner
import a_type_runner
import c_type_runner

def run_A():
    questions = [
            """
            Describe an implementation of a data structure with the following operations (x is a key):}
            Insert(x) - in amortized time (O(log n)).
            Search(x) - in amortized time (O(log n)).
            Delete(x) - in amortized time (O(log n)).
            """
            # """
            # Describe an implementation of a data structure with the following operations (x is a key):
            # Insert(x) - in amortized time (O(log n)).
            # Search(x) - in amortized time (O(log n)).
            # Delete(x) - in amortized time (O(1)).
            # """, 
            # """
            # Describe an implementation of a data structure with the following operations (x is a key):
            # Insert(x) - in amortized time O(log n).
            # Search(x) - in amortized time O(log n).
            # Delete(x) - in amortized time O(1) and also in worst-case time O(1).
            # """
                ]

    prompts = [
            "",
            """
            You are very good in computer science
            """,
            """
            You are very good in computer science and know how to solve data structures questions, please solve the following question and explain your thinking process 
            """,
            """
            You are a very smart professor in computer science, think smartly and long time about the following question:
            """,
            """
            You are charlie chaplin and since you are an actor you do not know anything about computer science or data structures: 
            """,
            """
            Solve the following question carefully, analyze your answer few times before responding and improve if needed, when giving me the complexity, make sure you can prove it: 
            """
            ]
    

    original_answers =[
                        """
                        \textbf{Central Data Structure:} AVL Tree. \textbf{Brief Description:} We will use the standard operations of an AVL tree. \textbf{Complexity Explanation:} All operations are in worst-case in \(O(\log n)\), and therefore, in particular, amortized directly from the definition of amortized.                        
                        """
                        # """
                        # \textbf{Central Data Structure:} AVL Tree. \textbf{Brief Description:} We will use the standard operations of an AVL tree. \textbf{Explanation for Complexity:} In the banker's method - at the time of insertion \((x(\text{insert})\), we insert the element, and additionally leave \(\log n\) coins for its deletion.
                        # """,
                        # """
                        # \textbf{Central Data Structure:} AVL Tree. \textbf{Secondary Data Structure:} Linked List. The worst-case complexity of insert is \(O(n \log n)\). The worst-case complexity of search is \(O(n \log n)\). \textbf{Solution:}  
                        # During initialization, we will initialize an AVL tree and a linked list.  
                        # During deletion, we will insert \(x\) at the beginning of the linked list.  
                        # During search/insert, before performing the actual operation, we will traverse the entire linked list and delete element by element.  
                        # After emptying the list, we will perform the actual operation (search/insert).  
                        # Amortized analysis using the banker's method - at the time of insertion \((x\text{, insert})\), we will insert the element and also leave it with \(\log n\) coins for its deletion.
                        # """
                    ] 
    
    a_type_runner.analyze_list(questions, prompts, original_answers)

def run_C():
    questions = [
            """
            What is the asymptotic relationship between the following functions:
            If there are multiple correct answers, choose the tightest one.
            \( f(n) = \frac{n}{\log(n)}, \quad g(n) = \frac{n^2}{(\log(n))^{2004}} \)
            \begin{enumerate}
                \item \( f(n) = O(g(n)) \)
                \item \( f(n) = \Omega(g(n)) \)
                \item \( f(n) = \Theta(g(n)) \)
                \item \( f(n) = o(g(n)) \)
                \item \( f(n) = \omega(g(n)) \)
            \end{enumerate}
            """
                ]

    prompts = [
            "",
            """You are very good in computer science""",
            ]
    
    original_answers_letters =[
                        """a"""
                    ] 
    
    original_answers_sentences = [
        """For all \( \epsilon > 0 \), it holds that \(\log n = o(n)\)."""
    ]
    c_type_runner.analyze_list(questions, prompts, original_answers_letters, original_answers_sentences)



def run_D():
    questions = [
            """
            \textit{We define a family of functions (mapping $n$ keys to a table of size $m$) as almost universal: \newline
            For any two distinct values from the domain of $n$ keys, the probability of randomly selecting a function from the family such that it returns the same value (among $m$ values) for both is bounded by $m^{-1/3}$. \newline
            What is the minimum table size $m$ such that if we choose a function randomly from an almost universal family, the expected number of collisions is bounded by $\frac{1}{2}$? \newline
            A. $n^{1/3}$ \newline
            B. $n^{2/3}$ \newline
            C. $n^{4/3}$ \newline
            D. $n^2$ \newline
            E. $n^3$ \newline
            F. $n^6$}
            """
                ]

    prompts = [
            "",
            """
            You are very good in computer science
            """,
            ]
    
    original_answers =[
                        """
                        F
                        """
                    ] 
    d_type_runner.analyze_list(questions, prompts, original_answers)



def main():
    #run_A()
    run_C()
    #run_D()
    

if __name__ == '__main__':
    main()

