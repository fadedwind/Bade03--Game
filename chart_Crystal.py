from chart_patterns import *

class Chart_Crystal():
    def __init__(self):
        self.song_name = 'Crystal'  

    def build_chart(self,full_path):
        song_length = 101000
        song_bpm = 140 #210 #140*2 #70
        song_mpb = ((1000 * 60 / song_bpm))  # 85.7
        song_difficulty = 3
        number_of_nodes = 211
        recommended_fps = 60
        
        song_offset = -400

        hold_len1 = 2700
        hold_len2 = 1500
        hold_len3 = 800
        hold_gap = 100

        s1 = 425
        s2 = s1//2 + 1
        s3 = s1//4

        lsize0 = s3 - 50
        lsize1 = s2 - 50
        lsize2 = s1 - 50 
        lsize3 = s2*3 -50
        lsize4 = s1*2 -50

        with open("%s" % full_path, "w") as f:
            f.write('%d,%d,%d,%d,%d\n' % (song_length, song_bpm, song_difficulty, number_of_nodes,recommended_fps))
            beat_pos = song_offset

            pattern = basic_hold(beat_pos, 1, 1, hold_len1)
            beat_pos += hold_len1
            f.write(pattern)

            pattern = basic_hold(beat_pos - 2*hold_gap, 2, 1, hold_len3+hold_gap)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_hold(beat_pos - 2*hold_gap, 3, 1, hold_len2+hold_gap)
            beat_pos += hold_len2
            f.write(pattern)

            pattern = basic_hold(beat_pos - 2*hold_gap, 2, 1, hold_len3+hold_gap)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_hold(beat_pos - 2*hold_gap, 1, 1, hold_len3+hold_gap)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_hold(beat_pos- hold_gap, 4, 1, hold_len1 + hold_gap)
            beat_pos += hold_len1
            f.write(pattern)

            pattern = basic_hold(beat_pos - hold_gap, 3, 1, hold_len3 + hold_gap)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_hold(beat_pos , 2, 1, hold_len1 + hold_gap)
            beat_pos += hold_len1
            f.write(pattern)

            pattern = basic_hold(beat_pos - hold_gap*2, 1, 1, hold_len3)
            beat_pos += hold_len3
            f.write(pattern)

            beat_pos -= 180 

            pattern = basic_strike(beat_pos -30, 4, 1)
            beat_pos += hold_len2 + hold_gap + 150
            f.write(pattern)

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += hold_len1
            f.write(pattern)

            beat_pos -= 80 

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += 80
            f.write(pattern)
            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_len3//2 +10
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += hold_len3//2
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += hold_len2
            f.write(pattern)

            beat_pos += 110 

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += hold_len3 + hold_gap
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_len3 + hold_gap
            f.write(pattern)


            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += hold_len2
            f.write(pattern)

            beat_pos += 140  

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += hold_len3 + hold_gap + 40
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_len3 + hold_gap + 40
            f.write(pattern)

            beat_pos -= 100  # error correction

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += hold_len2 + hold_gap + 150
            f.write(pattern)

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_len3
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += hold_len1
            f.write(pattern)

            beat_pos -= 80  

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += 80
            f.write(pattern)
            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_len3//2 +10
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += hold_len3//2
            f.write(pattern)

            pattern = basic_strike(beat_pos, 4, 1)
            beat_pos += hold_len2
            f.write(pattern)

            beat_pos += 110 

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += hold_len3 + hold_gap
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_len3 + hold_gap
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += hold_len2
            f.write(pattern)

            beat_pos += 140  

            pattern = basic_strike(beat_pos, 1, 1)
            beat_pos += hold_len3 + hold_gap + 40
            f.write(pattern)

            pattern = basic_strike(beat_pos, 2, 1)
            beat_pos += hold_gap*4
            f.write(pattern)

            pattern = basic_strike(beat_pos, 3, 1)
            beat_pos += 0
            f.write(pattern)

            beat_pos += s1 

            for i in range(4):
                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += s1
                f.write(pattern)

                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += s1
                f.write(pattern)

                pattern = basic_strike(beat_pos, 2, 1)
                beat_pos += s1
                f.write(pattern)

                pattern = basic_strike(beat_pos, 2, 1)
                beat_pos += s1
                f.write(pattern)

            beat_pos += 5

            for i in range(4):
                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += s2
                f.write(pattern)

                pattern = basic_strike(beat_pos, 2, 1)
                beat_pos += s2
                f.write(pattern)

                pattern = basic_strike(beat_pos, 1, 1)
                beat_pos += s2
                f.write(pattern)

                pattern = basic_strike(beat_pos, 2, 1)
                beat_pos += s2
                f.write(pattern)

            beat_pos += 5

            for i in range(4):
                pattern = basic_hold(beat_pos, 1, 1, s2)
                beat_pos += s1
                f.write(pattern)

                pattern = basic_hold(beat_pos, 2, 1, s2)
                beat_pos += s1
                f.write(pattern)

            for j in range(2):
                for i in range(2):
                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1
                    f.write(pattern)

                    beat_pos += 10 

                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s2
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 2, 1)
                    beat_pos += s2
                    f.write(pattern)

                    pattern = basic_strike(beat_pos, 1, 1)
                    beat_pos += s1
                    f.write(pattern)

                    beat_pos -= 10 

                    for j in range(5):
                        pattern = basic_strike(beat_pos, 1, 1)
                        beat_pos += s2
                        f.write(pattern)

                        pattern = basic_strike(beat_pos, 2, 1)
                        beat_pos += s2
                        f.write(pattern)

                beat_pos += 10

            beat_pos += 10  

            for j in range(2):
                for i in range (4):
                    pattern = basic_hold(beat_pos + s2, 2, 1, lsize2 - s2) # start late
                    beat_pos += s1
                    f.write(pattern)

                    pattern = basic_hold(beat_pos, 3, 1, lsize1)
                    beat_pos += s2
                    f.write(pattern)
                    pattern = basic_hold(beat_pos, 2, 1, lsize3)
                    beat_pos += s2*3
                    f.write(pattern)

                    if j==0:
                        pattern = basic_hold(beat_pos, 3, 1, lsize0)
                        beat_pos += s3
                        f.write(pattern)
                        pattern = basic_hold(beat_pos, 2, 1, lsize0)
                        beat_pos += s3
                        f.write(pattern)
                    else:
                        pattern = basic_hold(beat_pos, 2, 1, lsize0)
                        beat_pos += s3
                        f.write(pattern)

                    pattern = basic_hold(beat_pos, 3, 1, lsize1)
                    beat_pos += s2
                    f.write(pattern)

                    if i==0:
                        if j==1:
                            pattern = basic_hold(beat_pos, 4, 1, lsize2)
                            beat_pos += s1
                            f.write(pattern)
                            pattern = basic_hold(beat_pos, 3, 1, lsize1)
                            beat_pos += s2
                            f.write(pattern)
                            pattern = basic_hold(beat_pos, 2, 1, lsize0)
                            beat_pos += s3
                            f.write(pattern)

                            pattern = basic_hold(beat_pos, 1, 1, lsize2)
                            beat_pos += s1
                            f.write(pattern)

                            pattern = basic_strike(beat_pos + 200, 2, 1)
                            beat_pos += s1
                            f.write(pattern)

                            beat_pos -= 50  
                        else: 
                            pattern = basic_hold(beat_pos+s2, 2, 1, lsize3-s2) # start late
                            beat_pos += s2*3
                            f.write(pattern)

                            pattern = basic_hold(beat_pos, 3, 1, lsize1)
                            beat_pos += s2
                            f.write(pattern)
                            pattern = basic_hold(beat_pos, 2, 1, lsize2)
                            beat_pos += s1
                            f.write(pattern)

                            pattern = basic_hold(beat_pos, 1, 1, lsize1)
                            beat_pos += s2
                            f.write(pattern)

                            pattern = basic_hold(beat_pos, 2, 1, lsize1)
                            beat_pos += s2
                            f.write(pattern)



                    elif i==1:
                        if j==1: 
                            beat_pos += s3
                        pattern = basic_hold(beat_pos, 2, 1, lsize4)
                        beat_pos += s1*2
                        f.write(pattern)

                        pattern = basic_hold(beat_pos, 3, 1, lsize3)
                        beat_pos += s2*3
                        f.write(pattern)
                        pattern = basic_hold(beat_pos, 4, 1, lsize1)
                        beat_pos += s2
                        f.write(pattern)


                    elif i==2:
                        beat_pos += s3 
                        if j==1:
                            beat_pos += s3  

                        pattern = basic_hold(beat_pos, 4, 1, lsize2)
                        beat_pos += s1
                        f.write(pattern)
                        pattern = basic_hold(beat_pos, 3, 1, lsize1)
                        beat_pos += s2
                        f.write(pattern)
                        pattern = basic_hold(beat_pos, 2, 1, lsize0)
                        beat_pos += s3
                        f.write(pattern)

                        pattern = basic_hold(beat_pos, 1, 1, lsize2)
                        beat_pos += s1
                        f.write(pattern)

                        pattern = basic_strike(beat_pos + 250, 2, 1)
                        beat_pos += s1
                        f.write(pattern)


                        beat_pos -= s3  

                    else:
                        beat_pos += 40  # start early

                        if j==1:
                            beat_pos += 200
                            ############ type B-6
                            pattern = basic_hold(beat_pos, 3, 1, lsize3 -s2)
                            beat_pos += s1
                            f.write(pattern)

                            pattern = basic_hold(beat_pos, 2, 1, lsize3)
                            beat_pos += s1
                            f.write(pattern)

                            pattern = basic_hold(beat_pos-s2, 1, 1, lsize4)
                            beat_pos += s2*3
                            f.write(pattern)

                            pattern = basic_hold(beat_pos + s3, 2, 1, lsize4)
                            beat_pos += 1000
                            f.write(pattern)

                        else:
                            pattern = basic_hold(beat_pos, 1, 1, lsize3)
                            beat_pos += s2*3
                            f.write(pattern)
                            pattern = basic_hold(beat_pos, 2, 1, lsize1)
                            beat_pos += s2
                            f.write(pattern)
                            pattern = basic_hold(beat_pos, 3, 1, lsize0)
                            beat_pos += s3
                            f.write(pattern)

                            pattern = basic_hold(beat_pos, 4, 1, lsize2)
                            beat_pos += s1
                            f.write(pattern)
                            pattern = basic_hold(beat_pos, 3, 1, lsize1)
                            beat_pos += s1
                            f.write(pattern)

                        beat_pos -= 40  # back to normal


                    beat_pos += 40  # resting tempo


        ##################################





