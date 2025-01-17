import pandas as pd
import json

# Extract scores from the JSON list
def extract_scores(json_list, nli_compares,nli_entailment_probs, nli_neutral_probs, nli_contradiction_probs, bleu_compares):
    scores_data = []
    for i, json_obj in enumerate(json_list):
        js = json.loads(json_obj)
        scores = {key: value["score"] for key, value in js.items()}
        scores["BLEU"] = bleu_compares[i]
        scores["NLI Result"] = nli_compares[i]
        scores["NLI Entailment"] = nli_entailment_probs[i]
        scores["NLI Neutral"] = nli_neutral_probs[i]
        scores["NLI Contradiction"] = nli_contradiction_probs[i]
        scores_data.append(scores)
    return scores_data
    
# builds pandas dataframe
def build_question_results_df(DICE_compares, nli_compares, nli_entailment_probs, nli_neutral_probs, nli_contradiction_probs , bleu_compares, json=True, type='A'):
    # Create a DataFrame
    if type=='A' or type=='B':
        scores_data = extract_scores(DICE_compares, nli_compares, nli_entailment_probs, nli_neutral_probs, nli_contradiction_probs, bleu_compares)
        df = pd.DataFrame(scores_data)
            # Assign titles to rows
        df.index = [
            "Original",
            "Data Structure",
            "Implementation",
            "Complexity",
            "Student",
            "Professor",
            "Child",
            "Tarjan",
            "Geoffrey Hinton",
            "Hans Peter Luhn",
            "Step by Step",
            "Go Over And Improve Solution",
            "Break Into Smaller Problems",
            "Ignore parts"
            ]
    elif type == 'C':
        indexes = [
            "Original",
            "Data Structure",
            "Implementation",
            "Complexity",
            "Student",
            "Professor",
            "Child",
            "Tarjan",
            "Geoffrey Hinton",
            "Hans Peter Luhn",
            "Step by Step",
            "Go Over And Improve Solution",
            "Break Into Smaller Problems",
            "Ignore parts"
        ]
        letters_compare = DICE_compares[0]
        sentences_compare = DICE_compares[1]
        df = pd.DataFrame({
            "Is Choice Equal": letters_compare,
            "Sentence Simmiarity": sentences_compare,
            "BLEU (Sentence)": bleu_compares,
            "NLI (Sentence)": nli_compares,
            "NLI Entailment": nli_entailment_probs,
            "NLI Neutral" : nli_neutral_probs,
            "NLI Contradiction": nli_contradiction_probs
        }, index=indexes)
    else:
        indexes = [
            "Original",
            "Data Structure",
            "Implementation",
            "Complexity",
            "Student",
            "Professor",
            "Child",
            "Tarjan",
            "Geoffrey Hinton",
            "Hans Peter Luhn",
            "Step by Step",
            "Go Over And Improve Solution",
            "Break Into Smaller Problems",
            "Ignore parts"
        ]
        df = pd.DataFrame(DICE_compares, index=indexes, columns=['Is Choice Equal'])

    return df