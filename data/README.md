# Plugin List

（未来会改成JOSN或者其他便于程序识别的格式）

## Official

> 注意：后续插件列表可能按字母顺序排序

### `driver_topojson`

基于 `topojson` 库，并未完全自行实现读取

* 仓库地址：https://github.com/mattijn/topojson
* 包地址：https://pypi.org/project/topojson/
* 文档地址：https://mattijn.github.io/topojson/

### `driver_shp`

基于 `pyshp` 库，并未完全自行实现读取

* 仓库地址：https://github.com/GeospatialPython/pyshp
* 包地址：https://pypi.org/project/pyshp/

### `driver_poly`

自行实现，提供多种输出方式

可以直接粗转换为Overpass或者其他常见的序列，也可转换为Yuheng的Carto对象或者从Carto对象生成多种序列

## Registry

See: https://github.com/geo-yuheng/yuheng-plugin-registry



## yuheng-indoor3d

渲染出三维模型或者室内三维可视化的相关支持，暂无细节设定

## yuheng-geoslice

类似osmium对数据按照bbox空间切片，只不过这里可以按照polygon，类似geopandas

## yuheng-nodeshrink

从1开始重新为所有node和way、relation编号，压缩到最大编号与len(node_dict)一样
  


