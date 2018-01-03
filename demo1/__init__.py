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
vr={"9":9,"5":5,"3":3,"1":1};
kd=list(vr.keys());
print(kd);
kd.sort();
print(kd);
for key in vr.keys():print(vr[key]);