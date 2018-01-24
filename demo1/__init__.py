#coding:utf-8
# 测试
#print("hello word!");

# 新增数组
# l=["a","b","c"];
#print(l[:-1]);

# 用来测试数据相加
# l=l+["d","e"];
#print(l);

#用来测试数组截取
# m=[1,2,3,4,5];
#print(l[-1::-1]);
# lists=[[1,2,3],[4,5,6],[7,8,9]];

#用来测试遍历
# rowd=[row[1] for row in lists if row[1] % 5==0];
# print(rowd);

#用来测试遍历某个数组
# rowd1=[lists[i][i] for i in [0,1,2] ];
# print(rowd1);

#2017-12-18
#测试字符复制
# doub=[c * 3 for c in "abcdef"];
# print(doub);

#测试函数
# M=[[1,2,3],[4,5,6],[7,8,9]]
# g=(sum(row) for row in M);
# print(next(g));

#测试map属性
# M=[[1,2,3],[4,5,6],[7,8,9]]
# g=map(sum,M);
# print(list(g));

#2017-12-27
#re={"name":"bikaqiu","age":13,"address":["fist","second"],"pay":"56.6"};
#print(re["name"]);

#2018-1-3
# vr={"9":9,"5":5,"3":3,"1":1};
# kd=list(vr.keys());
# print(kd);
# kd.sort();
# print(kd);
# for key in vr.keys():print(vr[key]);
# v="abcrikfn";
# spr=[];
# for i in v:
#     print(i*2)
#     spr.append(i*2);
#     print(spr);

#2018-1-6
# D={"D":12,"f":34,"ui":65,"sr":"ed"};
# if "f" in D:
#     print("yes");

#元
# A=(1,2,3,4,5);
# B=(5,6,7);
# C=A+B;
# print(C);
# print(C[4]);
# A=A+(8,9);
# print(A);

#文件处理
# f=open("F:/test.txt", 'w');
# f.write('hello\n');
# f.write('world');
# f.close();
# b=open("F:/test.txt");
# text=b.read();
# print(text);
# print(text.split());
#键值对
# x=set('test');
# y={'a','b','c'};
# print(x);
# print(x-y);
#定义类型
# class student:
#     def __init__(self,name,age):
#         self.name=name;
#         self.age=age;
#     def lastName(self):
#         return self.name.split()[-1];
#     def addAge(self):
#         self.age=self.age*5
#         print(self.age);
        
# zgc=student('redcloudy',23);
# zgc.addAge();
# print(zgc.lastName());

#2018-1-15
# myfiler=open(r'F:\test.txt');
# line = myfiler.read();
# myfiler.close();
# print(line);

# test="""如果大海能够换回我的爱，就让我用一生等待。
# 你还要我怎么样？还想怎样？""";
# print(test);

#2018-1-24
# s="test";
# print(s);
# r=s.replace("s", "r");
# print(r);

print("abc%sefgh%sjkl" % ('d','i'));


