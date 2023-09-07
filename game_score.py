from dataclasses import dataclass
import random
from faker import Faker
import datetime
#ssssssssssss

@dataclass
class Game_Score:
    player_name : str
    score:int 



def get_lowest_score(game_scores :list[Game_Score]):
        smallest_score = None
        for game_score in game_scores:
              if smallest_score is None: # här kan vi använda lambda
                   smallest_score = game_score.score
                   continue
              if game_score.score < smallest_score:
                    smallest_score = game_score.score
        return smallest_score

              
      

def get_highest_score(game_scores :list[Game_Score]):
      highest_score = None
      for game_score in game_scores:
              if highest_score is None: # här kan vi använda lambda
                  highest_score = game_score.score
                  continue
              if game_score.score > highest_score:
                    highest_score = game_score.score
      return highest_score
      
      

def get_lowest_highest_scores(list_of_game_scores: list[Game_Score]): # tuple: int
    highest_score = get_highest_score(list_of_game_scores)
    lowest_score = get_highest_score(list_of_game_scores)
    return lowest_score , highest_score    # return (lowest_score,highest_score) så står på egentligen

    




if __name__ == "__main__":

    game_scores = []
    faker = Faker()
    for i in range(10**5):
        random_score = random.randint(10,10_000)
        game_score = Game_Score(player_name = faker.name(),
                                score = random_score)
        game_scores.append(game_score)
    
    lowest_score = get_lowest_score(game_scores)
    highest_score = get_highest_score(game_scores)
    scores = get_lowest_highest_scores(game_scores) # lowest måste vara innan highest
    print(scores)