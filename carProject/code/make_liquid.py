from pyecharts import options as opts
from pyecharts.charts import Liquid
from pyecharts.globals import SymbolType
from fun import *

# 里程水球图
c = (
    Liquid()
    .add(
        "里程数大于5",
        [percentage(), percentage()],
        is_outline_show=False,
        shape=SymbolType.DIAMOND,
        # 背景颜色
        background_color="#87CEEB",
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="浙江省",subtitle="宝马二手车"),
        )
    .render("../out/car_water.html")
)
