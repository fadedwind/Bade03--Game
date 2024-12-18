import pygame

def invalid(statement):
    print(statement)
    raise ValueError

def basic_strike(pos,line,point,special = ''):
    multi_line_pattern = ''
    info = []
    for i in range(1,5): 
        if i==line:
            multi_line_pattern += 'N'
            info.append('%d/%s'%(point,special))
        else:
            multi_line_pattern += '_'
            info.append('')

    return write_multi_tiles(multi_line_pattern, pos, info)

def basic_hold(pos,line,point,length,special = ''):  
    multi_line_pattern = ''
    info = []
    for i in range(1,5): 
        if i==line:
            multi_line_pattern += 'H'
            info.append('%d/%d/%s'%(point,length,special))
        else:
            multi_line_pattern += '_'
            info.append('')

    return write_multi_tiles(multi_line_pattern, pos, info)

def write_multi_tiles(pattern, beat_pos,info):
    multi_tile_info = "%s,%d"%(pattern,beat_pos)

    for i in range(4): 
        tile_data = ',' 
        tile_info = info[i].split('/')

        if pattern[i]=='_': 
            pass
        elif pattern[i]=='N':
            if len(tile_info) == 1: 
                info[i] += '/'
            tile_data += info[i]
        elif pattern[i]=='H':
            if len(tile_info) == 2:
                info[i] += '/'
            tile_data += info[i]
        else:
            raise ValueError("Invalid pattern given!")

        multi_tile_info += tile_data

    return multi_tile_info+'\n'
