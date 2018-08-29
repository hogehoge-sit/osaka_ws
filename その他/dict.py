#coding: utf-8
"""
辞書作る
辞書型のkeyにこちらの入力情報を登録．中に意味などを格納する

json.load(file)    jsonファイルをdictに変換
json.dumps(dict)    dictをstringに変換
"""
import json
from time import sleep

def main():

	mydict = {}
	
		
	while True:
	
		with open("mydict.json", "r+", encoding="shift-jis") as f:
			f2 = json.load(f)
		speak = str(input("何か用ですか？"))
		
		#プログラムを終了する時
		if speak == "exit":
			print("終了します．．．")
			print(sleep(1))
			break    
				
		elif speak == "全部":
			print(f2)
				
		elif speak in f2:
			print(f2[speak])
			
		else:
			new_word = str(input("知らない言葉です．意味はなんですか？"))
			
			with open("mydict.json", "w", encoding="shift-jis") as fw:
				
				
				
				f2[speak] = new_word
				mydict2 = json.dumps(f2)
				fw.write(mydict2)
			
			print("覚えました")
		
		
	return
	
	
if __name__ == "__main__":
	main()