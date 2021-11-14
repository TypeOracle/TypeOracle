parse_covfile

drcov的输出结果中把所有module都放在一个文件里
这里会解析这种格式，按照模块名分离成不同的文件
同时将历史结果整合，定期进行保存

1. 将pdf模板的代码覆盖文件命名为base.log
2. 设置frame.py中的INPUT_DIR和OUTPUT_DIR
3. 运行frame.py

== 在虚拟机中运行较慢，建议直接在宿主机中运行
== 调用7z解压文件到tmp文件夹中，最后再删除临时文件，所以不要使用tmp文件夹
