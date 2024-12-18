from chart_patterns import *

class Chart_DropsOfH2O():
    def __init__(self):
        self.song_name = 'Drops of H2O'

    def build_chart(self,full_path):
        song_length = 98900
        song_bpm = 108*2
        cycle = 4
        song_mpb = ((1000 * 60 / song_bpm)/cycle)  
        song_difficulty = 0
        number_of_nodes = int((song_length / 1000) * (song_bpm / 60)) - 4
        recommended_fps = 60

        song_offset = -230
        s1 = 108
        s2 = 54

        hold_len = 80

        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, number_of_nodes,recommended_fps))
            beat_pos = song_offset

            pattern = basic_hold(beat_pos, 4, 1, hold_len)
            beat_pos += s1

