data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:      
        data.append( line)
        count += 1   #我希望每一千筆印一次
        if count % 1000000 == 0:
            print(len(data))           

print('檔案讀取完了，總共有 ',len(data),'筆的資料')    #獲得平均長度
print(data[0])
     

wc ={} #wordcount

for d in data:
    words = d.split( )#也可以直接用split()，他自己預設就是空格，這樣遇到使用者輸入連續空白鍵，就不會產生空白字串(' ')
    for word in words:
        if word in wc:
            wc[word] +=1
        else:
            wc[word] = 1 #如果不再字典裡，新增新的KE進WC這個字典
for word in wc:
    if wc[word] >100000:
        print(word, wc[word])  
print(len(wc))
print(wc['Giselle'])

while True:
    word = input('請問你想要查什麼字: ')
    if word == 'q':
        break
    if word in wc:
        print(word,' 出現的次數:', wc[word])
    else:
        print('沒有這個字')
print('感謝使用')        