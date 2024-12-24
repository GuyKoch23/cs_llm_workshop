import pandas as pd
import json

# Extract scores from the JSON list
def extract_scores(json_list):
    scores_data = []
    for json_obj in json_list:
        js = json.loads(json_obj)
        scores = {key: value["score"] for key, value in js.items()}
        scores_data.append(scores)
    return scores_data
    
# builds pandas dataframe
def build_question_results_df(list, json=True, type='A'):
    # Create a DataFrame
    if type=='A':
        scores_data = extract_scores(list)
        df = pd.DataFrame(scores_data)
            # Assign titles to rows
        df.index = [
            "original",
            "Smart",
            "smart long",
            "Professor",
            "Charlie",
            "Carefully"
            ]
    elif type == 'C':
        indexes = ['Original', 'Modified']
        letters_compare = list[0]
        sentences_compare = list[1]
        df = pd.DataFrame({
            "Letters": letters_compare,
            "Sentences": sentences_compare
        }, index=indexes)
        print(df)
    else:
        indexes = ['Original', 'Modified']
        df = pd.DataFrame(list, index=indexes, columns=['Equal'])

    return df