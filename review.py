data=[]
count = 0
with open ('reviews.txt', 'r')as f:
	for line in f:
		data.append(line)
		count +=1 
		if count % 1000 == 0:
			print(len(data))
print('檔案讀取完了，共有', len(data), '筆資料')

sum_len=0
for d in data:
	sum_len= sum_len + len(d)


print('平均是', sum_len/len(data))

new= []
for d in data:
	if len(d) < 100 :
		new.append(d)
print ('總夠有',len(new),'比留言長度小於100')
print (new[0])