#実行する時は
#>python crawler.py 保存したいディレクトリ 画像のキーワード

from icrawler.builtin import GoogleImageCrawler
import sys
import os

argv = sys.argv

if __name__ == "__main__":
    
    if not os.path.isdir(argv[1]):
        os.makedirs(argv[1])

    max_num = int(input("max_num:"))
    crawler = GoogleImageCrawler(storage = {"root_dir" : argv[1]})
    crawler.crawl(keyword = argv[2], max_num = max_num)