#学生：孙宏杰
#学校：成都工业学院
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.globals import ThemeType
#原价与现价散点图
def getScatter():
    data = pd.read_csv("../data/finaldata.csv")
    scatter=(
        Scatter(init_opts=opts.InitOpts(theme=ThemeType.DARK))
        #原价x轴
        .add_xaxis(data["原价"])
        #现价y轴
        .add_yaxis(series_name="原价与现价散点图",y_axis=data["现价"])
        .set_series_opts(
            #去掉数值显示
            label_opts=opts.LabelOpts(
                is_show=False
            ),
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(
                        type_="max",
                        name="现价最贵"
                    ),
                    opts.MarkPointItem(
                        type_="min",
                        name="现价最便宜"
                    )
                ]
            )
        ).set_global_opts(
            xaxis_opts=opts.AxisOpts(
                type_="value",
                name="原价/万"
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                name="现价/万"
            ),
            #区域的一个缩放配置
            datazoom_opts=opts.DataZoomOpts(
                is_show=True
            ),


            #视觉映射
            visualmap_opts=opts.VisualMapOpts(
                is_show=ThemeType,
                min_=0,
                max_=200
            )

        ).render("../out/原价与现价散点图.html")
    )
    return scatter
getScatter()