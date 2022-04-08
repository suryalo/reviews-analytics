import time
import progressbar

data = []
count = 0
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 
		bar.update(count)
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
		new.append(d)  #如果 (if) 長度小於 100 就把你裝入 new 這個新清單
print('一共有', len(new), '筆留言長度小於100個字元')


# 篩選留言中有提到 “good" 的留言
good =[]
for d in data:
	if 'good' in d:
		good.append(d)  #如果 (if) “good" 這個字有在留言（d) 裡，就把你裝入good這個清單
print('一共有', len(good), '筆留言提到 good')


# 文字計數
start_time = time.time()
wc = {}  #word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1  # 新增 key 進字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])
end_time = time.time()
print('花了', round(end_time - start_time, 2), 'seconds')

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字：')
	if word == 'q':
		break
	elif word in wc:
		print(word, '出現過的次數為：', wc[word])
	else:
		print('這個字沒有出現過喔！')

print('感謝使用本查詢功能')



