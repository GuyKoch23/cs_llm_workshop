import nltk
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
nltk.download("punkt_tab")

def compare_bleu(reference: str, candidate: str, ngram: int = 4) -> float:
    # Tokenize the reference and candidate sentences
    reference_tokens = [nltk.word_tokenize(reference.lower())]
    candidate_tokens = nltk.word_tokenize(candidate.lower())

    # Calculate the BLEU score for the given n-gram (default is unigram)
    smoothing_function = SmoothingFunction().method1  # Smoothing to handle zero counts
    bleu_score = sentence_bleu(
        reference_tokens,
        candidate_tokens,
        weights=[1.0 / ngram] * ngram,
        smoothing_function=smoothing_function,
    )

    return bleu_score*10


# # Example usage
# reference = "The sky is blue."
# candidate = "The sky is clear."

# # Compare using BLEU score for 1-gram (unigram)
# bleu_score_unigram = compare_bleu(reference, candidate, ngram=1)
# print(f"BLEU score (unigram): {bleu_score_unigram}")

# # Compare using BLEU score for 2-gram (bigram)
# bleu_score_bigram = compare_bleu(reference, candidate)
# print(f"BLEU score (bigram): {bleu_score_bigram}")