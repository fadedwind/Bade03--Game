from chart_patterns import *

class Chart_Waikiki():
    def __init__(self):
        self.song_name = 'Waikiki'

    def build_chart(self,full_path):
        song_length = 118600
        song_bpm = 123*2
        cycle = 4
        song_mpb = ((1000 * 60 / song_bpm) / cycle)  
        song_difficulty = 0
        delete_unnessesary_node = 34
        number_of_nodes = int((song_length / 1000) * (song_bpm / 60)) - 4 -delete_unnessesary_node
        recommended_fps = 60

        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, number_of_nodes,recommended_fps))
            beats = 0
            switch = True
            while number_of_nodes > 0:
                if beats % cycle == 1:
                    pattern = ''
                    if switch:
                        pattern = basic_strike(beats*song_mpb, 1, 1)
                        number_of_nodes -= 1
                    else:
                        pattern = basic_hold(beats*song_mpb, 2, 1, 500)
                        number_of_nodes -= 1
                    f.write(pattern)
                    switch = not switch
                beats += 1


