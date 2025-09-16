
import os,sys 
from PIL import Image, ImageDraw, ImageFont

# 安装Pillow
# pip3 install Pillow==9.5.0

def draw_cover(main_title, second_title, img_path, background ):
    
    img = Image.open(background)
    draw = ImageDraw.Draw(img)

    W=img.width
    H=img.height

    #print("背景图片分辨率: %sx%s" % (W,H))

    # 定义主副标题的字体
    font_size_m = int(W/10)
    font_size_s = int(W/20)

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
    print("图片输出到: %s" % img_path)
    return img 


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage:")
        print("  python %s 主标题 副标题 保存路径 背景图片 " % __file__)
        exit()

    main_title = sys.argv[1]
    second_title = sys.argv[2]
    img_path = sys.argv[3] 
    background = sys.argv[4] if len(sys.argv) > 4 else 'assets/0.jpg'

    img = draw_cover( main_title, second_title, img_path, background )
    #img.show()
