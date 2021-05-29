# Twitter 感情分析
## 概要
指定したキーワードに対して、<br>
ポジティブなツイートが多いか、ネガティブなツイートが多いかを数値化する。

## 例1
```
> python main.py

keyword: リモートワーク
searches count: 100
```
```
positive words:
[('いい', 9), ('収入', 8), ('簡単', 6), ('おかげ', 5), ('良い', 4), ('歓迎', 4), ('お金', 4), ('明日', 3), ('おすすめ', 3), ('可', 3)]
negative_words:
[('残業', 6), ('ウイルス', 4), ('騒音', 3), ('非常', 3), ('不安', 3), ('変', 3), ('緊急', 3), ('痛い', 2), ('疲れる', 2), ('太る', 2)]
-------------------------------
positive: 59/100
negative: 21/100
normal  : 20/100
score   : 0.5334285714285716
```
## 例2
```
> python main.py

keyword: 東京オリンピック
searches count: 1000
```
```
positive words:
[('株', 105), ('いい', 61), ('ため', 46), ('良い', 38), ('中止-NEGATION', 29), ('安全', 28), ('清水', 22), ('安心', 21), ('命', 21), ('出来る', 21)]
negative_words:
[('中止', 288), ('感染', 113), ('変異', 69), ('ウイルス', 59), ('反対', 52), ('緊急', 27), ('事態', 27), ('爆発', 26), ('逮捕', 24), ('不満', 23)]
-------------------------------
positive: 283/1000
negative: 489/1000
normal  : 228/1000
score   : -0.36656031746031714
```