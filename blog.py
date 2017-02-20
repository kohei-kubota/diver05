import sys

blogs = []

def simple_blog():
    operation = ('以下より行う操作を選んでください\n',
    '1:ブログを作成する\n',
    '2:作成されたブログを見る\n',
    '3:ブログアプリを終了する\n')
    a, b, c, d = operation
    print(a + b + c + d)
    try:
        number = int(input())
    except ValueError:
        print("1から3を入力してください")
        return

    if number == 1:
        create(blogs)
    elif number == 2:
        if blogs:
            for blog_dict in blogs:
                for k,v in sorted(blog_dict.items(), reverse=True):
                    print(v)
    elif number == 3:
        sys.exit()
    else:
        print("1から3を入力してください")

# 引数がなくても動作する
def create(blogs):
    blog = {}
    blog["title"] = input()
    blog["content"] = input()
    blogs.append(blog)
    print(blogs)

while True:
    simple_blog()
