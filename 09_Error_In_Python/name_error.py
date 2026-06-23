#not defined high_score,never introduced high_score --> name error
#scope error

def calculate_score() -> None:
    high_score: int = 0 #local scope
calculate_score()
#name error
#print(high_score)