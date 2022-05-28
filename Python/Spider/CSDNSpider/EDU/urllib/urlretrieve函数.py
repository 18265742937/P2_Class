from urllib import request

# 获取网页源码并将源码写入到文件  urlretrieve(url,文件名)
# request.urlretrieve("https://www.sogou.com/","sougou.html")


# https://pic.baike.soso.com/ugc/baikepic2/18888/cut-20200315153127-1956922470_jpg_673_538_34165.jpg/300
# request.urlretrieve("https://pic.baike.soso.com/ugc/baikepic2/18888/cut-20200315153127-1956922470_jpg_673_538_34165.jpg/300", "shiyuanlimei.png")


# 可以下载图片
request.urlretrieve("http://shp.qpic.cn/ishow/2735082609/1598406105_84828260_10892_sProdImgNo_2.jpg/0", "壁纸.png")
