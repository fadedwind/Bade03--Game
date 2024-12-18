from chart_patterns import *

class Chart_Destructoid():
    def __init__(self):
        self.song_name = 'Destructoid'

    def build_chart(self,full_path):
        ##################################### fill in
        song_length = 94900
        song_bpm = 110*2
        song_mpb = ((1000 * 60 / song_bpm))
        song_difficulty = 0
        number_of_nodes = 3
        recommended_fps = 60

        gap = 100
        ####################################

        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, number_of_nodes,recommended_fps))
            ################################## fill in
            beats = 0

            pattern = basic_strike(beats, 1, 1)
            beats += gap
            f.write(pattern)
            pattern = basic_strike(beats, 1, 1)
            beats += gap
            f.write(pattern)
            pattern = basic_strike(beats, 1, 1)
            beats += gap
            f.write(pattern)
            ##################################

