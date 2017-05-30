#-*- coding:utf-8 -*-
import os
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator


def draw_music_cloud(music_dir='/Users/zhuqi/Music/网易云音乐', mask_path='mask/163Music6.png', font_path='Arial Unicode.ttf'):
    '''
    draw_music_cloud
    :param music_dir: music dir
    :param mask_path: mask picture dir (background)
    :param font_path: font path
    :return:
    '''
    singer = {}
    for root,dirs,files in os.walk(music_dir):
        songs = [x.split(' - ')[0].decode('UTF-8') for x in files if '.mp3' in x]
        for song in songs:
            if song in singer:
                singer[song] += 1
            else:
                singer[song] = 1

    # print sorted(singer.iteritems(),key=lambda d:d[1],reverse=True)

    mask = np.array(Image.open(mask_path))
    image_colors = ImageColorGenerator(mask)

    wc = WordCloud(background_color="white", font_path=font_path, mask=mask).generate_from_frequencies(singer)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    # bg picture
    plt.imshow(mask, cmap=plt.cm.gray, interpolation="bilinear")
    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    draw_music_cloud()