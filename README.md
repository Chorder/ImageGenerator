# ImageGenerator

一个制作视频封面的脚本，可以批量生成视频（文章）的封面图片。

示例：

<img src="./example.jpg" width="350" alt="示例图片">


## Usage

### 1. 安装Pillow(9.5.0)

```bash
pip3 install Pillow==9.5.0
```

### 2. 运行

*背景图片参数是可选的，如果没有指定，默认用assets/0.jpg*

```bash
python generage_cover.py 主标题 副标题 保存路径 [背景图片]
```

### 3. 应用

generage_clock_img.py是基于generage_cover.py的一个特殊修改，可以生成60张图片，内容是从00:00~59:59

生成好的文件放在output目录，然后可以执行下面的命令(makeVideoFromPics.sh中的内容，需要先安装ffmpeg)：

```bash
ffmpeg -framerate 1 -i ./output/%04d.jpg -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -r 1 -pix_fmt yuv420p 3600fps.mp4
```

这样就可以生成一个每秒1帧，一共3600帧的一小时倒计时视频。



