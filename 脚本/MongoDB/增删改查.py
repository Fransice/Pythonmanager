import pymongo


def system():
    print('◆您将进入数据库管理系统，数据无价、谨慎操作！◆')
    print('◇1:查看数据◇')
    print('◇2:增加数据◇')
    print('◇3:修改数据◇')
    print('◇4:删除数据◇')
    print('◇5:搜索数据◇')
    print('●6:退出数据库管理系统●')

    # 建立与mongodb的连接
    client = pymongo.MongoClient('localhost', 27017)
    # 得到数据库
    stu = client['stu']
    # 得到一个数据集合
    message = stu['message']

    while True:
        order = int(input('请输入相关指令：'))
        if order == 1:
            exit = message.count()
            if exit == 0:
                print('抱歉，数据库中目前没有相关数据！')
            else:
                for data in message.find():
                    content = data['name'] + data['age'] + data['sex']
                    print(content)
        elif order == 2:
            name = input('请输入学生姓名：')
            age = input('请输入学生年龄：')
            sex = input('请输入学生性别(男/女)：')
            data = {
                'name': name,
                'age': age,
                'sex': sex,
            }
            ###
            ###
            message.insert_one(data)
            print('添加成功！')

        elif order == 3:
            name = input('请输入要修改的学生姓名：')
            exit = message.count({'name': name})
            if exit != 0:
                age = input('请输入修改后的学生年龄：')
            ###
            ###
                message.update({'name': name}, {'$set': {'age': age}})
                print('修改成功')
            else:
                print('抱歉，数据库中没有这个学生的信息！')

        elif order == 4:
            name = input('请输入要删除的学生姓名：')
            exit = message.count({'name': name})
            if exit != 0:
                
            ###
            ###
                message.remove({'name': name})
                print('删除成功')
            else:
                print('抱歉，数据库中没有这个学生的信息！')
        elif order == 5:
            name = input('请输入要查询的学生姓名：')
            exit = message.count({'name': name})
            if exit != 0:
                
            ###
            ###
                data = message.find_one({'name': name})
                content = data['name'] + data['age'] + data['sex']
                print(content)
            else:
                print('抱歉，数据库中没有这个学生的信息！')

        elif order == 6:
            print('感谢您的使用！')
            break
        else:
            print('您的输入有误，请输入有效指令(1/2/3/4/5)')


if __name__ == '__main__':
    system()