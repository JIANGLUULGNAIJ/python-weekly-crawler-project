from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd


databar=pd.read_csv("../data/finaldata.csv")
databar2=databar.sort_values(by="里程",ascending=False)
databar2 = databar2.reset_index(drop=True)
KMdata=databar2.get("里程")
KMlist0_10=[]
KMlist10_20=[]
KMlist20_30=[]
KMlistall=[]
KMname=["0-10/KM","10-20/KM","20-30/KM"]
for i in KMdata:
    if i>=20:
        KMlist20_30.append(i)
    if 20>i>=10:
        KMlist10_20.append(i)
    if 10>i:
        KMlist0_10.append(i)
KMlistall.append(len(KMlist0_10))
KMlistall.append(len(KMlist10_20))
KMlistall.append(len(KMlist20_30))
bar = (
    Bar()
    .add_xaxis(KMname)
    .add_yaxis("车辆数",KMlistall)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="公里区间"),
        yaxis_opts=opts.AxisOpts(name="车辆数"),
        xaxis_opts=opts.AxisOpts(name="区间"),)
    .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45)))
)
bar.render("../out/公里区间.html")




