#open打開檔案給檔案名 'r'讀取模式 'w'寫的模式
#as當作一個簡稱，f是隨便給一個代稱(file)
#line隨便取的，我希望一行一行讀取，所以我先代稱為LINE
'''
apple

melon

water
'''
#跑出來每個都有空行，因為我們再輸入TXT檔案時候我們都還行了。加上print功能本身也會換行
#所以結果會跑出兩次換行，所以就多了一個空行
#.strip()可以把換行符號去掉
#有OPEN一般要附上CLOSE語言，因為PYTHON專有with語言就備有一來開就自動CLOSE功能
data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:      
        data.append( line)
        count += 1   #我希望每一千筆印一次
        if count % 100000 == 0:
            print(len(data))

   
data1 =[]     
with open('food.txt','r') as f:
    for line in f:      
        data1.append(line.strip()) 
        print(len(data1))
print(data1)   #如果放在跟上行並會列印一次長度一次DATA，一次長度，一次DATAraise
        

data2=[]    
with open('food.txt','r') as f:
    for line in f:  
        data2.append(line.strip())
        print(len(data2))
        print(data2)
        
        
#無法讀取中文資料 
data1 = []
with open('test.txt','r')  as f:
    for line in f:
        data1.append(line.strip())
        print(data1) 
        print(data1[0]) 
print('...................................................')
print(data1[1]) 
print('j' in data1)

