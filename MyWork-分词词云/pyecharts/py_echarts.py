""" 
@file: py_echarts.py
@Time: 2018/08/19
@Author:heningqiu
"""
# from pyecharts import Geo
# data =[("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)]
# geo =Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600, background_color='#404a59')
# attr, value =geo.cast(data)
# geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)
# geo.show_config()
# geo.render()
#
# from pyecharts import Bar
# bar =Bar("我的第一个图表", "这里是副标题")
# bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# bar.show_config()
# bar.render()

# from pyecharts import Bar
# attr=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1=[5, 20, 36, 10, 75, 90]
# v2=[56, 24, 32, 50, 35, 60]
# bar =Bar("x 轴和 y 轴交换")
# bar.add("商家A", attr, v1)
# bar.add("商家B", attr, v2, is_convert=True)
# bar.render()


# from pyecharts import Pie
# attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 =[11, 12, 13, 10, 10, 10]
# pie =Pie("饼图示例")
# pie.add("", attr, v1, is_label_show=True)
# pie.show_config()
# pie.render()

# from pyecharts import WordCloud
# name =['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications', 'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp', 'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham', 'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
# value =[10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
# wordcloud =WordCloud(width=1300, height=620)
# wordcloud.add("", name, value, word_size_range=[20, 100])
# wordcloud.show_config()
# wordcloud.render()


# from pyecharts import WordCloud
# name =['Sam S Club', 'Macys', 'Amy Schumer', 'Jurassic World', 'Charter Communications', 'Chick Fil A', 'Planet Fitness', 'Pitch Perfect', 'Express', 'Home', 'Johnny Depp', 'Lena Dunham', 'Lewis Hamilton', 'KXAN', 'Mary Ellen Mark', 'Farrah Abraham', 'Rita Ora', 'Serena Williams', 'NCAA baseball tournament', 'Point Break']
# value =[10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555, 550, 462, 366, 360, 282, 273, 265]
# wordcloud =WordCloud(width=1300, height=620)
# wordcloud.add("", name, value, word_size_range=[30, 100], shape='diamond')
# wordcloud.show_config()
# wordcloud.render()

# from pyecharts import Line
# attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 =[5, 20, 36, 10, 10, 100]
# v2 =[55, 60, 16, 20, 15, 80]
# line =Line("折线图示例")
# line.add("商家A", attr, v1, mark_point=["average"])
# line.add("商家B", attr, v2, is_smooth=True, mark_line=["max", "average"])
# line.show_config()
# line.render()

from pyecharts import Line
attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 =[5, 20, 36, 10, 10, 100]
v2 =[55, 60, 16, 20, 15, 80]
line =Line("折线图-面积图示例")
line.add("商家A", attr, v1, is_fill=True, line_opacity=0.2, area_opacity=0.4, symbol=None)
line.add("商家B", attr, v2, is_fill=True, area_color='#000', area_opacity=0.3, is_smooth=True)
line.show_config()
line.render()
