
from chart_patterns import *

class Chart_AnotherWay():
    def __init__(self):
        self.song_name ='Another way'

    def build_chart(self,full_path):
        song_length = 39500
        song_bpm = 126 #83
        cycle = 4
        song_mpb = ((1000 * 60 / song_bpm) / cycle)  
        song_difficulty = 5
        number_of_nodes = 95 
        recommended_fps = 60

        song_offset = 3700
        s1 = 146 #146
        s2 = (s1//4)*3

        hold_len = s1*2
        hold_half = s1
        hold_full = s1*4

        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, number_of_nodes,recommended_fps))
            beat_pos = song_offset

            for i in range(14): 
                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += s1
                f.write(pattern)

                pattern = basic_strike(beat_pos+s2, 2, 1)
                beat_pos += 2*s1
                f.write(pattern)

                pattern = basic_strike(beat_pos, 3, 1)
                beat_pos += s1
                f.write(pattern)

                for i in range(1,4):
                    pattern = basic_strike(beat_pos, i, 1)
                    if i==3:
                        beat_pos += s1
                    else:
                        beat_pos += s2
                    f.write(pattern)

            pattern = basic_hold(beat_pos - s1, 4, 1, hold_len)
            beat_pos += hold_len
            f.write(pattern)

            beat_pos += hold_len*2

            pattern = basic_hold(beat_pos, 4, 1, hold_half)
            beat_pos += hold_len
            f.write(pattern)

            pattern = basic_hold(beat_pos, 4, 1, hold_half)
            beat_pos += hold_len
            f.write(pattern)

            beat_pos += 200 

            for j in range(4):
                pattern = basic_strike(beat_pos + s1*4, j + 1, 1)
                #pattern += basic_strike(beat_pos + s1 * 12, j+1, 1)
                pattern += basic_strike(beat_pos + s1 * 17, j+1, 1)
                beat_pos += (hold_full + s1)*4
                f.write(pattern)
