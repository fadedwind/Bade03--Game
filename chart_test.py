from chart_patterns import *

class Chart_Test():
    def __init__(self):
        self.song_name = 'test'

    def build_chart(self,full_path):

        song_length = 8 * 1000
        song_bpm = 100
        song_mpb = ((1000 * 60 / song_bpm))
        song_difficulty = -1
        number_of_nodes = 0
        total_points = 0
        recommended_fps = 60

        song_offset = 500

        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, number_of_nodes,recommended_fps))

            beat_pos = song_offset

            pattern = write_multi_tiles('NN__', beat_pos, ['1/','1/','',''])
            beat_pos += 1000
            f.write(pattern)

            pattern = write_multi_tiles('H_NN', beat_pos, ['1/300','','1/','1/'])
            beat_pos += 1000
            f.write(pattern)

            pattern = write_multi_tiles('HHHH', beat_pos, ['1/300','1/300','1/300','1/300'])
            beat_pos += 1000
            f.write(pattern)

            pattern = write_multi_tiles('HNHN', beat_pos, ['1/300','1/','1/300','1/'])
            beat_pos += 1000
            f.write(pattern)

            pattern = write_multi_tiles('NNNN', beat_pos, ['1/','1/','1/','1/'])
            beat_pos += 1000
            f.write(pattern)

            pattern = write_multi_tiles('___N', beat_pos, ['','','','1/'])
            beat_pos += 1000
            f.write(pattern)

            pattern = write_multi_tiles('H___', beat_pos, ['1/1000','','',''])
            beat_pos += 1000
            f.write(pattern)
