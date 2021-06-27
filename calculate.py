data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:      
        data.append( line)
        count += 1   #我希望每一千筆印一次
        if count % 100000 == 0:
            print(len(data))           
sum_len = 0
for d in data:
    sum_len = sum_len + len(d) #每次讀取一行獲得總數厚再存回去再抓第二行
print('留言平均長度為',sum_len/len(data))    #獲得平均長度


#篩選功能1
new = []     
for d in data:       
    if len(d) < 100:
       new.append(d)
print('一共有',len(new),'筆留言長度小於100')       
print(new[0])
print(new[1]) 


#篩選功能2
good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有',len(good),'筆留言有提到good')
print(good[0])
print(good[10]) 

#list compreehension
good =[d for d in data if 'good' in d]  #第一個d = good.append(d)
print(len(good))  
print(good[0])

great = [1 for d in data if 'great' in d] #把第一個用１塞進去
print(great)

bad =[ 'bad' in d for d in data]  #"bad in d，表示如果bad in d，會是是非題
print(bad)
 
