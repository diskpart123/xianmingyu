# -*- coding: utf-8 -*-
# @Time    : 2020/02/16 15:47
# @Author  : xianming yu
# @File    : 20面向对象_项目实战.py

"""
pygame入门
"""
"""
目标
    1.项目准备
    2.使用pygame创建图形窗口
    3.理解图像并实现图像绘制
    4.理解游戏循环,游戏时钟
    5.理解精灵和精灵组
    
项目准备
    1.新建飞机大战项目
    2.导入游戏素材图片
    游戏的第一印象
        1.把一些静止的图像绘制到游戏窗口当中
        2.根据用户的交互或其他情况,移动这些图像,产生动画效果
        3.根据图像之间是否发生重叠,判断敌机是否被摧毁等其他情况
i1 使用pygame创建图形窗口
    小节目标
        1.游戏的初始化和退出
        2.理解游戏中的坐标
        3.创建游戏主窗口
        4.简单的游戏循环
        注意:可以将图片素材绘制到游戏的窗口上,开发游戏之前需要先知道,如果建立游戏窗口
    i1.1 游戏的初始化和退出
        1.要使用pygame提供的所有功能之前,需要调用init方法
        2.在游戏结束前需要调用quit方法
        方法                         说明
        pygame.init()              导入并初始化pygame模块,使用其他模块之前,必须先调用init方法
        pygame.quit()              卸载所有pygame模块,在游戏结束之前调用
    
    i1.2 理解游戏中的坐标系
        坐标系
            1.原点在左上角(0,0)
            2.X轴水平方向向右,逐渐增加
            3.Y轴垂直方向向下,逐渐增加
        在游戏中,所有可见的元素都是以矩形区域来描述位置
            要描述一个矩形区域有四个要素:(x,y)(width,height)
        pygame专门提供了一个类pygame.Rect用于描述矩形区域
            Rect(x,y,width,height)->Rect
        pygame.Rect类内部构造
            x,y,
            left,top,bottom,right,
            center,centerx,centery,
            size,width,height  #size 尺寸大小  width 矩形宽度,height 矩形高度
        提示
            pygame.Rect是一个比较特殊的类,内部只是封装了一些数字计算
            不执行pygame.init()方法同样能够使用
        案例演练
            需求
                1.定义hero_rect矩形描述,英雄的位置和大小
                2.输出英雄的坐标原点(x和y)
                3.输出英雄的尺寸(宽度,高度)
            代码示例
                import pygame
                pygame.init()
                hero_rect = pygame.Rect(100, 500, 120, 125)
                pygame.quit()
                print("英雄的原点%d %d" % (hero_rect.x, hero_rect.y))
                print("英雄的尺寸%d %d" % (hero_rect.width, hero_rect.height))
                print("%d %d"%hero_rect.size) #size是元组属性,也是显示矩形尺寸
            输出结果:
                英雄的原点100 500
                英雄的尺寸120 125
                120 125
    i1.3 创建游戏主窗口
        1.pygame专门提供一个模块pygame.display用于创建,管理游戏窗口
            方法                          说明
            pygame.display.set_mode()     初始化游戏显示窗口
            pygame.display.update()       刷新屏幕内容显示,稍后使用
            set_mode的方法
            set_mode(resolution=(0,0)flags=0,depth=0)->Surface
        2.作用
            创建游戏显示窗口
        3.参数
            1.resolution 指定屏幕的宽和高,默认创建的窗口大小和屏幕大小一致
            2.flags 参数指定屏幕的附加选项,例如是否全屏等等,默认不需要传递
            3.depth 参数表示颜色的位数,默认自动匹配
        4.返回值
            1.暂时可以理解为游戏的屏幕,游戏的元素都需要被绘制到游戏的屏幕上
        5.注意
            必须使用变量记录 set_mode方法的返回结果!因为后续所有的图像绘制都基于这个返回结果
        6.创建游戏主窗口
            import pygame
            pygame.init()
            # 创建游戏的窗口 480*700
            screen = pygame.display.set_mode((480,700))            
            pygame.quit()
    i1.4 简单的游戏循环
        1.为了做到游戏程序启动后,不会立即退出,通常会在游戏程序中增加一个游戏循环
        2.所谓游戏循环就是一个"无限循环"
        3.在创建游戏窗口代码下方,增加一个无限循环
            注意:游戏窗口不需要重复创建  
            import pygame
            pygame.init()
            # 创建游戏的窗口 480*700
            screen = pygame.display.set_mode((480,700))
            #游戏死循环,保持游戏窗口一直显示
            while True:
                pass
            pygame.quit()
i2 理解图像并实现图像绘制
    i2.1 在游戏中,能够看到的"游戏元素"大多都是图像
        "图像文件"初始时保存在磁盘上的,如果需要使用,第一步需要加载到"内存"
    i2.2 要在屏幕上看到某一个图像的内容需要按照三个步骤
        1.使用pygame.image.load() 加载图像的数据
        2.使用游戏屏幕对象,调用blit方法将图像绘制到指定位置
        3.调用pygame.display.update() 方法更新整个屏幕的显示
            提示:要想在屏幕上看到绘制的结果,就一定调用pygame.display.update()方法
    i2.3 代码演练1-绘制背景图像
        1.加载background.png 创建背景
        2.将背景绘制在屏幕的(0,0)位置
        3.调用屏幕更新显示背景图像
        代码实现
            import pygame
            pygame.init()
            # 创建游戏的窗口 480*700
            screen = pygame.display.set_mode((480, 700))
            # 绘制图像的三个步骤
            # 1.加载图像数据
            bg = pygame.image.load("E:\\xianmingyu\\12飞机大战项目\\images\\background.png")
            # 2.blit绘制图像
            screen.blit(bg,(0,0))
            # 3.update更新屏幕显示
            pygame.display.update()
            while True:
                pass
            pygame.quit()
    i2.4 代码演练2-绘制英雄图像
        需求
            1.加载me1.png创建英雄飞机
            2.将英雄飞机绘制在屏幕的(200,500)的位置
            3.调整屏幕更新显示飞机图像      
        代码实现
            import pygame

            pygame.init()
            # 创建游戏的窗口 480*700
            screen = pygame.display.set_mode((480, 700))
            # 绘制图像的三个步骤
            # 1.加载背景图像数据
            bg = pygame.image.load("E:\\xianmingyu\\12飞机大战项目\\images\\background.png")
            # 2.blit绘制图像
            screen.blit(bg, (0, 0))
            # 3.加载英雄图像
            hero=pygame.image.load("E:\\xianmingyu\\12飞机大战项目\\images\\me1.png")
            # 4.blit绘制图像
            <在PyGame中的坐标原点在左上角(定义的窗口),向右X变大，向左X变小(可为负数),
            向下Y变大，向上Y变小(可为负数),下面的(200,300)理解为:x=200,y=500>
            screen.blit(hero,(200,500))
            # 5.update更新屏幕显示
            pygame.display.update()
            while True:
                pass
            pygame.quit()
        透明图像
            1.png格式的图像是支持透明的
            2.在绘制图像时,透明区域不会显示任何内容
            3.但是如果下方已经有内容,会透过"透明区域"显示出来
        理解update()方法的作用
            可以在screen对象完成所有blit方法之后,统一调用一次display.update()方法,
            同样可以在屏幕上看到最终的绘制效果
            1.使用display.set_mode()创建的screen对象是一个内存中的屏幕数据对象
                可以理解成是油画的画布
            2.screen.blit()方法可以在画布上绘制很多图像
                例如:英雄,敌机,子弹...
                这些图像有可能会彼此重叠或者覆盖
            3.display.update()方法会将画布的最终结果绘制在屏幕上,这样可以提高屏幕绘制效率,增加游戏的流畅度    
i3 理解游戏循环和游戏时钟
    现在英雄飞机已经被绘制到屏幕上,怎么能够让飞机移动呢?
    i3.1 游戏中动画实现原理
        1.跟电影原理相似,游戏中的动画效果,本质上是快速的在屏幕上绘制图像
            电影是将多张静止的电影胶片连续快速的播放,产生连贯的视觉效果
        2.一般在电脑上每秒绘制60次,能够达到非常连续高品质的动画效果
            每次绘制的结果被称为"帧"(Frame)
i4 游戏循环
    i4.1 游戏的两个组成部分(游戏初始化,游戏循环)
        游戏循环的开始就意味着游戏的正式开始                                   
    
    游戏初始化                          游戏循环                          
        设置游戏窗口                         设置刷新频率
        绘制图像初始位置                      检测用户交互
        设置游戏时钟                          更新所有图像位置
                                            更新屏幕显示
    i4.2 游戏循环的作用
        1.保证游戏不会直接退出
        2.变化图像位置--动画效果
            2.1 每隔1/60秒(每秒钟重复执行60次)移动一下所有图像的位置
            2.2 调用pygame.display.update()方法更新屏幕显示
        3.检测用户交互--按键,鼠标等
i5 游戏时钟
    i5.1 pygame专门提供了一个类pygame.time.Clock可以非常方便的设置屏幕绘制速度--刷新帧率
    i5.2 要使用时钟对象需要两步:
        1.在游戏初始化创建一个时钟对象
        2.在游戏循环中让时钟对象调用tick(帧率)方法
    i5.3 tick方法会根据上次被调用的时间,自动设置游戏循环中的延时
        代码实现
            clock=pygame.time.Clock()
            i=0
            while True:
                # 可以指定循环体内部的代码执行的频率
                clock.tick(60)
                print(i)
                i+=1
    i5.4 英雄的简单动画实现
        需求
            1.在游戏初始化定义一个pygame.Rect的变量记录英雄的初始位置
            2.在游戏循环中每次让英雄的y-1做向上移动
            3.y<=0将英雄移动到到屏幕的底部
            提示:
                1.每一次调用update()方法之前,需要把所有的游戏图像都重新绘制一遍
                2.而且应该最先重新绘制背景图像
            4.代码实现
                import pygame
                pygame.init()
                # 创建游戏的窗口 480*700
                screen = pygame.display.set_mode((480, 700))
                # 绘制图像的三个步骤
                # 1.加载背景图像数据
                bg = pygame.image.load("E:\\xianmingyu\\12飞机大战项目\\images\\background.png")
                # 2.blit绘制图像
                screen.blit(bg, (0, 0))
                #3.加载英雄图像
                hero=pygame.image.load("E:\\xianmingyu\\12飞机大战项目\\images\\me1.png")
                #4.blit绘制图像
                <在PyGame中的坐标原点在左上角(定义的窗口),向右X变大，向左X变小(可为负数),
                向下Y变大，向上Y变小(可为负数),下面的(200,300)理解为:x=200,y=500>
                
                screen.blit(hero,(150,300))
                # 5.可以在所有绘制工作绘制完成以后,统一调用display.update()方法
                pygame.display.update()
                #创建时钟对象
                clock=pygame.time.Clock()
                #定义rect记录飞机的初始位置
                hero_rect=pygame.Rect(150,300,102,126)
                #游戏循环->意味着游戏的正式开始
                while True:
                    # 可以指定循环体内部的代码执行的频率
                    clock.tick(60)
                    #修改英雄飞机的位置
                    hero_rect.y-=1
                    #y<=0将英雄移动到到屏幕的底部
                    if hero_rect.y<=0:
                        hero_rect.y=700
                    #再次绘制游戏背景,避免英雄飞机每次移动有阴影
                    screen.blit(bg,(0,0))
                    #调用blit方法绘制图像
                    screen.blit(hero,hero_rect)
                    #调用update()方法更新显示
                    pygame.display.update()
                pygame.quit()
    i5.5 在游戏循环中监听事件
        i5.5.1 事件 event
            1.就是游戏启动后,用户针对游戏所作的操作
            2.例如:点击关闭按钮,点击鼠标,按下键盘
        i5.5.2 监听
            1.在游戏循环中,判断用户的具体操作
                只有捕获到用户的具体操作,才能有针对性的做出响应
        i5.5.3 代码实现
            1.pygame中通过pygame.event.get()可以获得用户当前所作动作的事件列表
                用户可以同一时间做很多事情
            2.提示:这段代码非常的固定,几乎所有的pygame游戏都大同小异
i6 理解精灵和精灵组
    i6.1 精灵和精灵组
        1.在刚刚完成的案例中,图像加载,位置变化,绘制图像都需要程序员编写代码分别处理
        2.为了简化开发步骤,pygame提供了两个类
            2.1 pygame.sprite.Sprite--存储图像数据image和位置rect的对象
            2.2 pygame.sprite.Group

后面都是游戏实战开发,暂时不想看了,后续如果基础不牢,在回过来看             
                    
    
            
            
        
"""
import pygame
pygame.init()
hero_rect = pygame.Rect(100, 500, 120, 125)
pygame.quit()

print("英雄的原点%d %d" % (hero_rect.x, hero_rect.y))
print("英雄的尺寸%d %d" % (hero_rect.width, hero_rect.height))
print("%d %d"%hero_rect.size) #size是元组属性,也是显示矩形尺寸

