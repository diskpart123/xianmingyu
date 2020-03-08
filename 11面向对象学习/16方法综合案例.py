# -*- coding: utf-8 -*-
# @Time    : 2020/02/12 14:03
# @Author  : xianming yu
# @File    : 16方法综合案例.py

"""
方法综合案例
"""
"""
需求
    1. 设计一个 Game 类
    2. 属性：
       2.1 定义一个"类属性",top_score记录游戏的"历史最高分"
       2.2 定义一个 "实例属性" player_name 记录 "当前游戏的玩家姓名"
    3. 方法：
       3.1 "静态方法" show_help 显示游戏帮助信息
       3.2 "类方法" show_top_score 显示历史最高分
       3.3 "实例方法" start_game 开始当前玩家的游戏 
    4. 主程序步骤
       4.1 查看帮助信息
       4.2 查看历史最高分
       4.3 创建游戏对象，开始游戏
    5. 代码实现
        class Game(object):
            # 1.定义类属性,top_score用来表示"历史最高分"
            top_score = 0
        
            def __init__(self, player_name):
                # player_name用来表示当前玩家"姓名"
                self.player_name = player_name
        
            # 定义静态方法,用来查看帮助信息
            @staticmethod
            def show_help():
                print("帮助信息:让僵尸走进房间...")
        
            # 定义类方法,用来显示历史最高分
            @classmethod
            def show_top_score(cls):
                print("历史纪录:[%d]" % cls.top_score)
        
            # 定义实例方法,创建游戏对象，开始游戏
            def start_game(self):
                print("[%s]开始游戏..." % self.player_name)
                Game.top_score = 999

        调用:创建对象
            # 1. 查看游戏帮助
            Game.show_help()
            # 2. 查看游戏最高分
            Game.show_top_score()
            # 3. 创建游戏对象，开始游戏
            game = Game("小明")
            game.start_game()
            # 4. 游戏结束，查看游戏最高分
            Game.show_top_score()
        输出结果:
            帮助信息:让僵尸走进房间...
            游戏最高分为:[0]
            [小明]开始游戏...
            游戏最高分为:[999]
            
        
"""
class Game(object):
    # 1.定义类属性,top_score用来表示"历史最高分"
    top_score = 0

    def __init__(self, player_name):
        # player_name用来表示当前玩家"姓名"
        self.player_name = player_name

    # 定义静态方法,用来查看帮助信息
    @staticmethod
    def show_help():
        print("帮助信息:让僵尸走进房间...")

    # 定义类方法,用来显示历史最高分
    @classmethod
    def show_top_score(cls):
        print("历史纪录:[%d]" % cls.top_score)

    # 定义实例方法,创建游戏对象，开始游戏
    def start_game(self):
        print("[%s]开始游戏..." % self.player_name)
        Game.top_score = 999


# 1. 查看游戏帮助
Game.show_help()
# 2. 查看游戏最高分
Game.show_top_score()
# 3. 创建游戏对象，开始游戏
game = Game("小明")
game.start_game()
# 4. 游戏结束，查看游戏最高分
Game.show_top_score()






