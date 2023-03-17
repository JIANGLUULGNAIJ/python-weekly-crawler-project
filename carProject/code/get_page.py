from pyecharts.charts import Page

# 执行之前,请确保:1、已经把json文件放到本目录下 2、把json中的title和table的id替换掉
Page.save_resize_html(
    source="../out/大屏_临时.html",
    cfg_file="../chart_config.json",
    dest="../可视化最终效果.html"
)
