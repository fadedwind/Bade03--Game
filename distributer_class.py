import pygame
from variables import *
from text_writer import *
from tiles import *
import math
from frame_class import *

def func1(input):
    return -0.3835*(input**2)+53.213*input-315.61

def func2(input):
    return 183.37*math.log(input)+56.319

def offset_corresponding_to_speed(input):
    if 10<=input<=20:
        return func1(input)
    elif 20<input<=100:
        return func2(input)
    else:
        return 0 

class Distributer():
    def __init__(self,stage_speed,offset,screen,request_list,song_name,song_bpm, given_fps, beat_line_request = False):
        global song_offsets
        self.screen = screen
        self.speed = stage_speed 

        if song_name in song_offsets.keys():
            song_offset = song_offsets[song_name]
        else:
            song_offset = 0
        self.offset = offset + int(offset_corresponding_to_speed(self.speed)) + song_offset
        print("Offset: ",self.offset)
        self.delta_t = ((line_length - node_spawning_y_pos)/self.speed)*100 

        self.given_fps = given_fps
        self.fps_error = (1000//self.given_fps) 

        tile_requests = []

        for request in request_list:
            tile_pattern = request[0]
            beat_pos_of_current_request = int(request[1])
            nodes_to_to_append_at_current_request = []
            holdes_to_to_append_at_current_request = []

            if len(tile_pattern) != 4:
                raise ValueError("Tile pattern not given as length-4 string!")

            for i in range(4): 
                if tile_pattern[i] == '_':
                    continue
                tile_info = request[2 + i].split('/')  

                if tile_pattern[i] == 'N':
                    n = Node(i + 1, int(tile_info[0]), self.given_fps, tile_info[1].strip())

                    nodes_to_to_append_at_current_request.append(n)
                elif tile_pattern[i] == 'H':
                    length = int(tile_info[1]) * self.speed // 100
                    h = Hold(i + 1, int(tile_info[0]), length, self.given_fps, tile_info[2].strip())
                    holdes_to_to_append_at_current_request.append(h)

            tile_requests.append( [beat_pos_of_current_request, nodes_to_to_append_at_current_request, holdes_to_to_append_at_current_request] )

        self.tile_requests = tile_requests
        self.beat_line_request = beat_line_request
        self.song_mpb = ((1000 * 60 / song_bpm))

        self.distributer_creation_time = pygame.time.get_ticks()

        self.ready = False
        first_request = self.tile_requests[0]

        self.very_first_request_deploy_time = - self.delta_t
        self.first_request_time_respect_to_music_start = int(first_request[0])

        self.first_call = True

        self.music_did_start_right_away = False
        self.state_determined = False

        self.time_anomaly = 0

    def print_next_n_requests(self,num):
        print('='*50)
        ind = 0
        while ind<min(len(self.tile_requests),num):
            print(self.tile_requests[ind])
            ind+=1

    def get_time(self): 
        time = pygame.time.get_ticks() - self.distributer_creation_time
        return time

    def distribute(self,nodes_on_screen,holds_on_screen,beat_lines):
        cur_time = self.get_time()  

        if self.first_call: 
            if cur_time != 0:
                self.distributer_creation_time = pygame.time.get_ticks()
                cur_time = 0
                self.first_call = False

        if self.beat_line_request and self.deploy_time(int(cur_time%self.song_mpb),0):
            self.deploy_beat_line(cur_time, beat_lines)

        if not self.ready:
            if not self.state_determined and cur_time > -self.very_first_request_deploy_time:  
                self.music_did_start_right_away = True
                self.state_determined = True
            if cur_time >= -self.very_first_request_deploy_time:
                self.ready = True

        cur_time = cur_time - (self.offset + self.time_anomaly)


        if not self.tile_requests == []:  
            current_request = self.tile_requests[0]
            current_request_deploy_time = int(current_request[0])

            if not self.deploy_time(current_request_deploy_time,cur_time): 
                return

            while self.deploy_time(current_request_deploy_time,cur_time): 
                tile_pattern = current_request[0]
                nodes_to_add = current_request[1]
                holds_to_add = current_request[2]
                for node in nodes_to_add:
                    nodes_on_screen.append(node)
                for hold in holds_to_add:
                    holds_on_screen.append(hold)

                self.tile_requests.remove(current_request)

                # next step
                if self.tile_requests == []: 
                    break
                current_request = self.tile_requests[0]
                current_request_deploy_time = int(current_request[0]) - self.delta_t

    def multi_tile_translator(self,tile_pattern):
        return

    def deploy_time(self,first_deploy_time,cur_time):
        return abs(first_deploy_time-cur_time) <= self.fps_error 

    def near_passed_deploy_time(self,first_deploy_time,cur_time):
        return 0 <= cur_time - first_deploy_time <= 50

    def node_not_deployed(self,node):
        pass

    def deploy_beat_line(self,cur_time,beat_lines):
        beat_lines.append(BeatLine(cur_time//self.song_mpb,self.given_fps ,show_beat = False))


