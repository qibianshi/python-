import urllib.request
import gevent
from gevent import monkey

monkey.patch_all()


def downloader(img_name, img_url):
    req = urllib.request.urlopen(img_url)

    img_content = req.read()

    with open(img_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "3.jpg", "https://huyaimg.msstatic.com/cdnimage/anchorpost/1051/c3"
                                          "/1aefb66117d5b6c72c4c61fc9ac69f_2168_1554706476.jpg?imageview/4/0/w/338"
                                          "/h/190/blur/1/format/webp"),

        gevent.spawn(downloader, "4.jpg", "https://huyaimg.msstatic.com/cdnimage/anchorpost/1026/a4"
                                          "/e4b3a2ceb431ab4a6fd71d6c925a2e_2168_1551096613.jpg?imageview/4/0/w/338/h"
                                          "/190/blur/1/format/webp")

    ])


if __name__ == "__main__":
    main()
