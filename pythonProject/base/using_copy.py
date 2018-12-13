"""浅copy"""
import copy
aa = [1,2,3]
bb = copy.copy(aa)
print(id(aa))    #11533088
print(id(bb))    #12014776
bb[0] =100
bb[1] =50
print(bb)        #[100, 2, 3]
print(aa)        #[1,2,3]
#由于数字不可变，修改的时候会替换旧的对象
print([id(x) for x in bb])
print([id(y) for y in aa])