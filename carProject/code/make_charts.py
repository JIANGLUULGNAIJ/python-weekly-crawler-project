from pyecharts import options as opts
from pyecharts.charts import Bar, Liquid, Map, Scatter, Pie
from pyecharts.components import Table
from pyecharts.globals import SymbolType, ThemeType

from fun import *


def make_bar_cash():
    databar = pd.read_csv("../data/finaldata.csv")
    df = databar.sort_values(by="现价", ascending=False)
    df = df.reset_index(drop=True)
    df = df.drop(labels=["id"], axis=1)
    maxlist = []
    maxnamelist = []
    minlist = []
    minnamelist = []
    allname = []
    maxallname = df.get("品牌")
    maxallcash = df.get("现价")
    for i in range(10):
        maxlist.append(maxallcash[i])
        maxnamelist.append(maxallname[i])
    df = df.sort_values(by="现价", ascending=True)
    df = df.reset_index(drop=True)
    minallcash = df.get("现价")
    minallname = df.get("品牌")
    for i in range(10):
        minlist.append(minallcash[i])
        minnamelist.append(minallname[i])
    for i in range(10):
        newdata = maxnamelist[i] + "/" + minnamelist[i]
        allname.append(newdata)
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC,width="500px",height="310px"))
            .add_xaxis(allname)
            .add_yaxis("最贵Top10", maxlist)
            .add_yaxis("最便宜Top10", minlist)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="最便宜与最贵"),
            yaxis_opts=opts.AxisOpts(name="价格（万）"),
            xaxis_opts=opts.AxisOpts(type_="value",name="车名"))
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45)))
    )
    return bar


def make_bar_km():
    databar = pd.read_csv("../data/finaldata.csv")
    databar2 = databar.sort_values(by="里程", ascending=False)
    databar2 = databar2.reset_index(drop=True)
    KMdata = databar2.get("里程")
    KMlist0_10 = []
    KMlist10_20 = []
    KMlist20_30 = []
    KMlistall = []
    KMname = ["0~10万公里", "10~20万公里", "20~30万公里"]
    for i in KMdata:
        if i >= 20:
            KMlist20_30.append(i)
        if 20 > i >= 10:
            KMlist10_20.append(i)
        if 10 > i:
            KMlist0_10.append(i)
    KMlistall.append(len(KMlist0_10))
    KMlistall.append(len(KMlist10_20))
    KMlistall.append(len(KMlist20_30))
    bar = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC,width="500px",height="310px"))
            .add_xaxis(KMname)
            .add_yaxis("二手车数目", KMlistall)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="公里区间"),
            yaxis_opts=opts.AxisOpts(name="二手车数目"),
            xaxis_opts=opts.AxisOpts(name="万公里"), )
            .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45)))
    )
    return bar


def make_liquid():
    c = (
        Liquid(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC,width="500px",height="310px"))
            .add(
            "里程数大于5",
            [percentage(), percentage()],
            is_outline_show=False,
            shape=SymbolType.DIAMOND,
            # 背景颜色
            background_color="#87CEEB",
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(subtitle="二手车中里程数 > 5万公里的比例"),
        )
    )
    return c


def make_map_zhejiang():
    databar = pd.read_csv("../data/finaldata.csv")
    sumall = databar['地区'].value_counts()
    allnumdata = []
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
        ['温州市', allnumdata[2]]
    ]
    map = (
        Map(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC,width="500px",height="310px"))
            .add(
            series_name="二手车数量",
            data_pair=pair_data,
            maptype="浙江"
        )

            .set_global_opts(
            title_opts=opts.TitleOpts(subtitle="各市二手车数量"),
            visualmap_opts=opts.VisualMapOpts(max_=500, is_piecewise=False)
        )
            .set_series_opts(
            label_opts=opts.LabelOpts(is_show=True, color="blue")
        )
    )
    return map


def make_pie_year():
    c = (
        Pie(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC,width="500px",height="310px"))
            .add(
            "",
            [list(z) for z in zip(year(), car())],
            radius=["40%", "75%"],
        )
            .set_global_opts(
            title_opts=opts.TitleOpts(subtitle="近五年二手宝马车辆占比"),
            legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
        )
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
    )
    return c


def make_scatter():
    data = pd.read_csv("../data/finaldata.csv")
    scatter = (
        Scatter(init_opts=opts.InitOpts(theme=ThemeType.ROMANTIC,width="500px",height="310px"))
            # 原价x轴
            .add_xaxis(data["原价"])
            # 现价y轴
            .add_yaxis(series_name="原价--现价", y_axis=data["现价"])
            .set_series_opts(
            # 去掉数值显示
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
            # 区域的一个缩放配置
            datazoom_opts=opts.DataZoomOpts(
                is_show=True
            ),

            # 视觉映射
            visualmap_opts=opts.VisualMapOpts(
                is_show=ThemeType,
                min_=0,
                max_=200
            )

        )
    )
    return scatter

def make_title():
    table = Table()
    table.add(headers=["基于Python的浙江省宝马二手车数据分析大屏"], rows=[], attributes={
        "align": "center",
        "border": False,
        "padding": "0px",
        "style": "background:{}; width:1500px;font-size:25px;".format('#F0E8CD')
    })
    return table