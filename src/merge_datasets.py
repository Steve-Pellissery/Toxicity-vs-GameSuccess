import pandas as pd

def merge_game_review_data(games, reviews, key="app_id"):
    return games.merge(reviews, on=key, how="left")
