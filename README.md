# spider-meitulu.com
## 漂亮妹子图网站的爬虫
- 低效
- 简陋
- 待todo

## 使用方法
- 基于python3
1. 修改setting里面待爬取的列表
    - item表（妹子的某个写真集首页）
    - person表（妹子的介绍页）
2. 在终端的程序目录下执行 `python main.py`  
    - 然后就自动运行了
    - item 会自动下载整个写真集
    - person 会找到这个妹子的所有写真集  
3. 文件自动保存在image文件夹下

## 不足
- 极为低效的单线程操作
- 编码转换问题，采取低效方案