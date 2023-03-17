# 绘制:整个页面
from pyecharts.charts import Page
from make_charts import *

page = Page(
	page_title="浙江省宝马二手车数据可视化大屏",
	layout=Page.DraggablePageLayout,  # 拖拽方式
)
page.add(
	# 增加:大标题
	make_title(),
	# 绘制:昂贵top10”和“便宜top10”的柱状图
	make_bar_cash(),
	# 绘制:各里程区间的二手车数目柱状图
	make_bar_km(),
	# 绘制:浙江省各城市二手车数目地图
	make_map_zhejiang(),
	# 绘制:近五年二手车数目占比
	make_pie_year(),
	# 绘制:里程大于5万公里的二手车占比
	make_liquid(),
	# 绘制:散点图
	make_scatter()
)
page.render('../out/大屏_临时.html')  # 执行完毕后,打开临时html并排版,排版完点击Save Config，把json文件放到本目录下
print('生成完毕:大屏_临时.html')

