import os, sys
from variables import *

def update_score(song_name,score):
    global creater_mode
    if creater_mode:
        return 

    APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
    full_path = os.path.join(APP_FOLDER, 'scores.txt')

    if os.path.isfile(full_path):
        pass
    else:
        f = open(full_path, "x")


    tokens = []
    with open(full_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        tokens = [line.split(',') for line in lines]

    tokens = [[token[0],float(token[1])] for token in tokens]

    song_score_exists = False
    update_flag = False
 
    for token in tokens:
        if token[0] == song_name:
            song_score_exists = True
            if token[1] < score:
                update_flag = True 
                tokens.remove(token)

    if not song_score_exists or update_flag:
        tokens.append([song_name,score])
        print("New high score!")
        print("Score updated for %s to %.2f" % (song_name, score))

    with open(full_path, "w") as f:
        for token in tokens:
            f.write("%s,%.2f\n"%(token[0],round(token[1],2)))

def fetch_highest_score(song_name):
    APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))
    full_path = os.path.join(APP_FOLDER, 'scores.txt')

    if os.path.isfile(full_path):
        pass
    else:
        return 0 
    tokens = []
    with open(full_path, "r") as f:
        lines = [line.strip() for line in f.readlines()]
        tokens = [line.split(',') for line in lines]

    for token in tokens:
        if token[0] == song_name:
            return float(token[1])

    return 0
