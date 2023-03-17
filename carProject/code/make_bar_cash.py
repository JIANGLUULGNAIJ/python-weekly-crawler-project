from pyecharts import options as opts
from pyecharts.charts import Bar
import pandas as pd

databar=pd.read_csv("../data/finaldata.csv")
df=databar.sort_values(by="现价",ascending=False)
df = df.reset_index(drop=True)
df=df.drop(labels=["id"], axis=1)
maxlist=[]
maxnamelist=[]
minlist=[]
minnamelist=[]
allname=[]
maxallname=df.get("品牌")
maxallcash=df.get("现价")
for i in range(10):
    maxlist.append(maxallcash[i])
    maxnamelist.append(maxallname[i])
df=df.sort_values(by="现价",ascending=True)
df = df.reset_index(drop=True)
minallcash=df.get("现价")
minallname=df.get("品牌")
for i in range(10):
    minlist.append(minallcash[i])
    minnamelist.append(minallname[i])
for i in range(10):
   newdata= maxnamelist[i]+"/"+minnamelist[i]
   allname.append(newdata)
bar = (
    Bar()
    .add_xaxis(allname)
    .add_yaxis("最贵前十", maxlist)
    .add_yaxis("最便宜前十",minlist)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="最便宜与最贵"),
        yaxis_opts=opts.AxisOpts(name="价钱/万"),
        xaxis_opts=opts.AxisOpts(name="车名"),)
    .set_global_opts(xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-45)))
)
bar.render("../out/最便宜与最贵对比.html")

