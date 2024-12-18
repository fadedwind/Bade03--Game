import os, sys

from variables import update_chart_flag
from chart_test import Chart_Test
from chart_AnotherWay import *
from chart_Crystal import *
from chart_H2O import *
from chart_Waikiki import *
from chart_Destructoid import *
from chart_BadApple import *
from chart_HHM import *

chart_builder_list = []

chart_builder_list.extend([Chart_Test(), Chart_DropsOfH2O(), Chart_Waikiki(), Chart_AnotherWay(),Chart_Crystal()])

chart_builder_list.append(Chart_Destructoid())
chart_builder_list.append(Chart_BadApple())
chart_builder_list.append(Chart_HHM())


def write_chart(song_name,instance):
    APP_FOLDER = os.path.dirname(os.path.realpath(sys.argv[0]))+'/charts/'
    full_path = os.path.join(APP_FOLDER, '%s.txt'%song_name)

    build_method = getattr(instance, instance.__class__.build_chart.__name__)
    if build_method:
        build_method(full_path)

    print("Chart updated: %s"%song_name)

if update_chart_flag:
    for cb in chart_builder_list:
        write_chart(cb.song_name,cb)

def update_chart():
    for cb in chart_builder_list:
        write_chart(cb.song_name,cb)

