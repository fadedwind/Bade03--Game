import pygame
import random
from variables import *
from music_ import *
from text_writer import *
from image_processor import *
from utility_functions import *
from score_saver import *

def view_score_menu(screen,clock,song_name,score_pointer,song_difficulty,total_points):
    score = score_pointer[0]
    music_Q(scoreboardMusic,True)
    viewer_run = True

    score_percentage = 0
    if total_points!=0:
        score_percentage = round((score / total_points) * 100, 3)
    score_percentage_loc = height//3 + title_text*2

    grade = score_grader(score_percentage)
    grade_sticker_loc = height//3 + title_text*4 + sticker_text//2

    alpha = 0
    alpha_max = 100
    score_color = score_colors[grade]
    bar_pos = (width // 2, height//3 + title_text*3)

    prev_score = fetch_highest_score(song_name)
    prev_score_loc = height//4 + big_text*2 + small_text

    update_score(song_name, score_percentage)

    credits = get_music_info(song_name)
    credits_loc = grade_sticker_loc + sticker_text*4

    drop_first_deploy_time = pygame.time.get_ticks()
    droplet_drawn = False  
    waterdrop_margin_x = 0
    waterdrop_margin_y = 0
    number_of_droplets = 3
    droplet_list = [(random.randint(0, 50),
                     (random.randint(bar_pos[0] - waterdrop_margin_x, bar_pos[0] + waterdrop_margin_x),
                      random.randint(bar_pos[1]-waterdrop_margin_y, bar_pos[1]+waterdrop_margin_y))) for i in
                    range(number_of_droplets)]


    while viewer_run:
        screen.fill(background_color[0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  
                viewer_run = False
                break

            if event.type == pygame.MOUSEMOTION:  
                pass

            if event.type == pygame.MOUSEBUTTONUP:
                (xp, yp) = pygame.mouse.get_pos()
                pass

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:  
                    viewer_run = False
                    break

        if not viewer_run:
            break

        write_text(screen, width // 2, height//20 , 'Press Enter to continue', small_text, background_color[0],
                   highlight_text_color)

        write_text(screen, width // 2, height//4 - big_text, '%s' % (song_name), big_text, background_color[0],
                   highlight_text_color)
        write_text(screen, width // 2, height//4 + big_text*2 - detail_text, 'Song difficulty: %s' % (song_difficulty), small_text, background_color[0],
                   highlight_text_color)

        write_text(screen, width // 2, score_percentage_loc, 'Score: %.1f %%' % (score_percentage), big_text,
                   background_color[0],
                   highlight_text_color)


        draw_score_bar(screen, score_percentage,score_color,alpha/alpha_max,bar_pos[0],bar_pos[1])
        if alpha < alpha_max:
            alpha += 1


        write_text(screen, width // 2, grade_sticker_loc , '%s' % (grade), sticker_text,
                   background_color[0],
                   score_color )


        write_text(screen, width//2, prev_score_loc, "Previous score: %.2f %%"%prev_score, tiny_text, background_color[0], highlight_text_color)

        write_text(screen, width//2, credits_loc+big_text, "'%s' song credits (link in README.md also):"%song_name, tiny_text, background_color[0],
                   highlight_text_color)

        for i in range(len(credits)):
            write_text(screen, width//2, credits_loc +big_text*2+ small_text*(i+1),
                       '%s'%credits[i], tiny_text, background_color[0],
                       highlight_text_color)


        if droplet_list:  
            current_run_time = pygame.time.get_ticks()
            for droplet in droplet_list:
                deploy_time = drop_first_deploy_time - droplet[0]
                position = droplet[1]
                delta = (current_run_time - (deploy_time))/1000
                if delta >= water_draw_time:
                    droplet_list.remove(droplet)
                factor = delta / water_draw_time
                radi = calc_drop_radius(factor, droplet_radius)
                pygame.draw.circle(screen,score_color, position, radi, particle_width)


        pygame.display.flip()
        clock.tick(main_loop_render_fps)

def draw_score_bar(screen, score_percentage, color, alpha,x,y):
    bar_width = (width//3)*2
    bar_height = big_text

    draw_bar_frame(screen, x, y, bar_width, bar_height, color)
    draw_bar(screen,x,y,bar_width,bar_height, score_percentage*alpha, color)


def score_grader(score_percentage):
    score_percentage = round(score_percentage)
    if score_percentage>= 100:
        return score_grades[0] # 'Pure Perfect!!! (PP)'
    if score_percentage>= 96:
        return score_grades[1] #'Perfect (P)'
    elif score_percentage>= 94:
        return score_grades[2] #'AA'
    elif score_percentage>= 90:
        return score_grades[3] #'A'
    elif score_percentage>= 80:
        return score_grades[4] #'B'
    elif score_percentage>= 70:
        return score_grades[5] #'C'
    elif score_percentage>= 60:
        return score_grades[6] #'D'
    elif score_percentage>= 40:
        return score_grades[7] #'E'
    else:
        return score_grades[8] #
