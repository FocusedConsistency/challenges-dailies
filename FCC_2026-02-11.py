def compute_score(judge_scores, *penalties):
    total = sum(judge_scores) - max(judge_scores) - min(judge_scores)
    total -= sum(penalties)
    return total

compute_score([10, 8, 9, 6, 9, 8, 8, 9, 7, 7], 1) # 64
