import pyecharts.options as opts
from pyecharts.charts import Pie
from fun import *

#  近五年二手宝马车辆占比饼图
c = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(year(), car())],
        radius=["40%", "75%"],
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="浙江省",subtitle="近五年二手宝马车辆占比"),
        legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
    )
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    .render("../out/car_year.html")
)
