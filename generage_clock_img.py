
import os,sys 
from PIL import Image, ImageDraw, ImageFont

# 安装Pillow
# pip3 install Pillow==9.5.0

def draw_cover(main_title, second_title, background, img_path):
    img = Image.open(background)
    draw = ImageDraw.Draw(img)

    W=img.width
    H=img.height

    #print("背景图片分辨率: %sx%s" % (W,H))

    # 定义主副标题的字体
    font_size_m = int(W/3)
    font_size_s = int(W/16)

    # 定义主副标题的高度（中线位于横图上下的黄金分割线）
    y_m = H*(1-0.618)-font_size_m/2
    y_s = H*0.618-font_size_s/2

    # 定义主副标题的字体
    main_title_style = ImageFont.truetype( "fonts/阿里巴巴普惠体H.ttf", font_size_m, encoding="utf-8")
    second_title_style = ImageFont.truetype( "fonts/阿里巴巴普惠体B.ttf", font_size_s, encoding="utf-8")

    # 测算主副标题的宽度
    padding = font_size_s/10
    l_m= draw.textlength(main_title, font=main_title_style)
    l_s = draw.textlength(second_title, font=second_title_style)

    #渲染主标题
    draw.text(( (W-l_m)/2, y_m ),main_title,"#FFFFFF", font=main_title_style )

    #渲染副标题
    #draw.rounded_rectangle(((W-l_s)/2-padding,y_s+padding,W-(W-l_s)/2+padding,y_s+font_size_s+padding*3),fill="#F4511E",radius=15)
    #draw.text(( (W-l_s)/2, y_s ),second_title,"#252525", font=second_title_style )

    img.save( img_path )
    print("图片输出到: %s" % img_path )
    return img 


if __name__ == "__main__":

    second_title = "一小时倒计时"
    main_title = "" 
    background = 'assets/2.jpg'

    i = 0
    for m in range( 0, 60 ):
        for s in range( 0, 60 ):
            main_title = f"{59-m:02d}:{59-s:02d}"
            img_path = f"output/{i:04d}.jpg"
            img = draw_cover( main_title, second_title, background, img_path )
            i+=1
    #img.show()
