data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 
		if count % 1000 == 0:  # % 用來求餘數 ＃如果 count 是 1000 的倍數才印出來
			print(len(data))
print('檔案讀取完了，總共有', len(data), '筆資料')


# 算出每筆資料的平均長度

sum_len = 0
for d in data:
	sum_len += len(d)  # sum_len = sum_len + len(d) # 累積留言長度加總

print('留言的平均長度為', sum_len/len(data))


# 篩選長度小於 100 的留言

new = []   #建立新清單
for d in data:
	if len(d) < 100:
		new.append(d)  #如果長度小於 100 就把你裝入 new 這個新清單
print('一共有', len(new), '筆留言長度小於100個字元')