bbk 2 ins
之前通过DynamoRIO获取了覆盖的基本块的首条指令，以及基本块的尝试
现在将其在ida中转化为指令的数量

for adobe reader:
1. 将要处理的dll通过ida处理后得到idb格式的文件
- 这个当时是我手动做的，应该有自动化的解析方法
2. 根据上一步得到的结果 adobe_sample_input 修改inscount.py中INPUT_DIR
- 并设置结果需要输出的OUTPUT_DIR
3. 运行batch.py 进行自动化的处理
4. 修改combine.py中OUTPUT_DIR以及OUTPUT_FNAME,运行combine.py
- step3输出结果是以文件为单位的，所以要将这些合并

for Foxit reader:
步骤基本一致，只是第三步运行batch.py改为运行foxitcmd.txt中的指令，最后也没必要使用combine.py

