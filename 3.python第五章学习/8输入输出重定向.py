import os
cmd = input("cmd:")
os.system(cmd)

#把上面的代码编写完成后,需要到微软终端下运行:
"""
运行的步骤:
    1.切换到程序的目录如:
        1.1: cd e:\yincheng\3.python第五章学习
        1.2: e:
        1.3: python 8输入输出重定向.py>1.txt
        1.4: 再输入:ipconfig,此时程序就会把ipconfig下面的信息"重定向"输出到1.txt文件中
        
        注意点:
            > 代表:输出(覆盖模式)
            < 代表:输入
            >> 代表:增量输出
            < > 代表:输入和输出 示例:8输入输出重定向.py<1.txt>2.txt 解释:把1.txt文件里
                    面的内容如:tasklist输入进去,然后在把打印的内容输出到2.txt
            
"""





