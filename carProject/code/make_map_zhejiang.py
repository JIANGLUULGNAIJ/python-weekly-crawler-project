from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd

databar=pd.read_csv("../data/finaldata.csv")
sumall=databar['地区'].value_counts()
allnumdata=[]
for i in sumall:
    allnumdata.append(i)
pair_data = [
    ['湖州市', allnumdata[8]],
    ['杭州市', allnumdata[1]],
    ['嘉兴市', allnumdata[4]],
    ['绍兴市', allnumdata[6]],
    ['金华市', allnumdata[3]],
    ['宁波市', allnumdata[0]],
    ['舟山市', 0],
    ['台州市', allnumdata[5]],
    ['丽水市', allnumdata[7]],
    ['衢州市', allnumdata[9]],
    ['温州市',allnumdata[2]]
]


def create_map():
    (
        Map()
            .add(
            series_name="二手宝马车辆数",
            data_pair=pair_data,
            maptype="浙江"
        )

            .set_global_opts(
            title_opts=opts.TitleOpts(title="浙江地图"),
            visualmap_opts=opts.VisualMapOpts(max_=500, is_piecewise=False)
        )
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=True, color="blue")
        )
            .render("../out/浙江二手车车辆数.html")
    )


create_map()

