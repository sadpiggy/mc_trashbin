# 要求

大作业须要实现的内容：(LTL模型检验算法实现）

 

1. Parser：transition system 以及 LTL formula的读取（读取格式见同单元的说明，可以假设transition system没有terminal state，LTL公式输入中每一个子公式都有括号）
2. 教材上从 LTL formula 到 GNBA 的等价构造
3. 教材上从 GNBA 到 NBA 的等价转换
4. 教材上 transition system 与 NBA 之间的product construction (Definition 4.62, Page 200)
5. 教材上检查 persistence property的nested depth-first search algorithm (Algorithm 8, Page 211)

对于2和3，如果你愿意的话，你也可以考虑在保证正确性的前提下对原有方法进行修改，或完全采用自己的方法。但须要把改动的地方以及为什么这么改动是正确的写到实现文档里。

 

大作业须要提交（zip文件）：

1. 带有注释的源代码（注释须要标注出各个模块的功能以及上述四个关键步骤对应的代码）
2. 编译方式以及使用方式
3. 实现文档（包括代码结构、数据结构等各个主要实现细节）

# 实现

###  工具

+ 使用antrl和c++

+ 安装antrl

  + 

  + ```text
    wget https://www.antlr.org/download/antlr-4.7.2-complete.jar
    ```

    + 需要安装最新版，否则出现

      ```
      pthon运行报错: Could not deserialize ATN：
      raise Exception("Could not deserialize ATN with version " + str(version) + " (expected " + str(SERIALIZED_VERSION) + ").") Exception: Could not deserialize ATN with version (expected 4)
      ```

  + pip install antlr4-python3-runtime

  + 将antlr的位置写入环境变量

    ```
    # antlr4
    export CLASSPATH=".:/usr/local/lib/antlr.jar:$CLASSPATH"
    alias antlr4='java -jar /usr/local/lib/antlr.jar'
    alias grun='java org.antlr.v4.gui.TestRig'
    ```

+ 