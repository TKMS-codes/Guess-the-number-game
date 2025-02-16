import random

min = int(input('最小値を入力してください>>'))
max = int(input('最大値を入力してください>>'))

#入力された最大値と最小値の範囲内で乱数を取得する
randomNum = random.randint(min, max)

#正解判定
isRight = False

for n in range(5):
    answer = int(input('数字を１つ入力してください>>'))
    if answer == randomNum:
        isRight = True
        print('正解です!!\nゲームを終了します')
        break

if(isRight == False):
   print('残念!試行回数の上限に達しました\nゲームを終了します')
