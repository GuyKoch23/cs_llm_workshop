from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F


def get_mode_tokenizer():
    model_name = "microsoft/deberta-large-mnli"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    return (model, tokenizer)

# returns 0 -1 or 1 according to result
def nli_compare_promise_and_hypothesis(promise, hypothesis, model, tokenizer):

    label_to_value = {
        "contradiction": -1,
        "neutral": 0,
        "entailment": 1
    }

    inputs = tokenizer(promise, hypothesis, return_tensors='pt', truncation=True, padding=True)
    
    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits
    
    probabilities = F.softmax(logits, dim=-1)
    
    labels = ["contradiction", "neutral", "entailment"]
    
    # Get the predicted label
    predicted_label = labels[torch.argmax(probabilities)]
    predicted_value = label_to_value[predicted_label]
    results = {label: probabilities[0][i].item() for i, label in enumerate(labels)}

    return predicted_value, results

# def main():
#     promise = "Yes"
#     hypothesis = "No"

#     result = nli_compare_promise_and_hypothesis(promise, hypothesis)

#     print(result)

# if __name__ == '__main__':
#     main()