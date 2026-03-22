import pandas as pd

def winning_candidate(candidate: pd.DataFrame, vote: pd.DataFrame) -> pd.DataFrame:
    # count votes per candidates
    count = vote['candidateId'].value_counts()

    # get candidateId with max votes
    top_id = count.idxmax()

    # return corresponding name
    return candidate[candidate['id'] == top_id][['name']]