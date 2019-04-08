import urllib.request

def main():
	req = urllib.request.urlopen("https://huyaimg.msstatic.com/cdnimage/anchorpost/1051/c3/1aefb66117d5b6c72c4c61fc9ac69f_2168_1554706476.jpg?imageview/4/0/w/338/h/190/blur/1/format/webp")
	
	img_content = req.read()

	with open ("1,jpg", "wb") as f:
		f.write(img_content)


if __name__ == "__main__":
	main()
