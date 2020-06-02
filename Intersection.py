def Intersection(tuple1,tuple2):
    if (tuple2[0]>=tuple1[0] and tuple2[0]<=tuple1[1]) or (tuple2[1]<=tuple1[1] and tuple2[0]<=tuple1[0] and tuple2[1]>=tuple1[0]) or (tuple1[0]>=tuple2[0] and tuple1[0]<=tuple2[1]) or (tuple1[1]<=tuple2[1] and tuple1[0]<=tuple2[0] and tuple1[1]>=tuple2[0]):
        return False
    return True

tuple1=(1,8)
tuple2=(14,16)
print(Intersection(tuple1,tuple2))