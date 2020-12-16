"""
In this assigment, you will be writing a function that finds the target words in a given text.
The inputs will be a text and a list of tuples including the target words along with its rank.
The function should return at most five target words in the given text, which have the highest ranking. For example;

Inputs:

text:
"I like to play board games with my friends at the weekends."
targets_words:
[(work, 5), (play, 1), (like, 2), (flower, 9)]

Output:
[(play, 1), (like, 2)]


[Optional 1] for whom is interested in language processing. you can go deep into with processing pipelines.
https://spacy.io/usage/processing-pipelines

Instead of using the targets.txt, use targets_tagged.txt to load the targets. The targets will be in the format of
((lemma, tag), rank) i.e. (('work', 'verb'), 5).
Tokenize, tag and parse the sentences in the text with the help of spaCy library. Use tagged tokens to match with
target words.

[Optional 2]
Propose a solution (do not code) when the size of target words is 2000. You can feel free think of constructing
 your own data structure or getting help from a DBMS.
"""
import sys
from typing import List, Tuple


target = Tuple[str, int]

# TODO: if you want to take a challenge in NLP, uncomment next 4 lines and comment out the line 32nd.
# import spacy
# nlp = spacy.load("en_core_web_sm")
# Word = Tuple[str, str]
# target = Tuple[Word, str]


def find_targets_in_text(target_words: List[target], text: str) -> List[target]:
    found_tuple_list = []

    for target_word in target_words:
        if target_word[0] in text:
            found_tuple_list.append(target_word)

    found_tuple_list.sort(key=lambda x: x[1], reverse=True)

    print(found_tuple_list[:5])
    return found_tuple_list[:5]


text = """Baseball is a bat-and-ball game played between two opposing teams who take turns batting and fielding. The game proceeds when a player on the fielding team, called the pitcher, throws a ball which a player on the batting team tries to hit with a bat. The objective of the offensive team (batting team) is to hit the ball into the field of play, allowing its players to run the bases, having them advance counter-clockwise around four bases to score what are called "runs". The objective of the defensive team (fielding team) is to prevent batters from becoming runners, and to prevent runners' advance around the bases. A run is scored when a runner legally advances around the bases in order and touches home plate (the place where the player started as a batter). The team that scores the most runs by the end of the game is the winner.
The first objective of the batting team is to have a player reach first base safely. A player on the batting team who reaches first base without being called "out" can attempt to advance to subsequent bases as a runner, either immediately or during teammates' turns batting. The fielding team tries to prevent runs by getting batters or runners "out", which forces them out of the field of play. Both the pitcher and fielders have methods of getting the batting team's players out. The opposing teams switch back and forth between batting and fielding; the batting team's turn to bat is over once the fielding team records three outs. One turn batting for each team constitutes an inning. A game is usually composed of nine innings, and the team with the greater number of runs at the end of the game wins. If scores are tied at the end of nine innings, extra innings are usually played. Baseball has no game clock, although most games end in the ninth inning.
Baseball evolved from older bat-and-ball games already being played in England by the mid-18th century. This game was brought by immigrants to North America, where the modern version developed. By the late 19th century, baseball was widely recognized as the national sport of the United States. Baseball is popular in North America and parts of Central and South America, the Caribbean, and East Asia, particularly in Japan, South Korea and Taiwan.
In the United States and Canada, professional Major League Baseball (MLB) teams are divided into the National League (NL) and American League (AL), each with three divisions: East, West, and Central. The MLB champion is determined by playoffs that culminate in the World Series. The top level of play is similarly split in Japan between the Central and Pacific Leagues and in Cuba between the West League and East League. The World Baseball Classic, organized by the World Baseball Softball Confederation, is the major international competition of the sport and attracts the top national teams from around the world."""


def convert_to_tuples(target_file: str) -> List[target]:
    with open(target_file) as f:
        lines = f.readlines()
        verify_target_uniqueness(lines)
        data = {}
        for line in lines:
            line = line.split(",")
            data[line[0]] = int(line[1])

        tuples = []
        for k, v in data.items():
            tuples.append((k, v))
        return tuples


def verify_target_uniqueness(lines) -> None:
    unique = []
    for line in lines:
        line = line.split(",")
        if line[0] not in unique:
            unique.append(line[0])
        else:
            print(f"Target word '{line[0]}' is duplicated, verify your input file!")


if __name__ == "__main__":
    target_words = convert_to_tuples(target_file=sys.argv[1])
    find_targets_in_text(target_words=target_words, text=text)
