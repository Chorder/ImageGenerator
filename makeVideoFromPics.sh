#ffmpeg -framerate 1 -i ./output/%04d.jpg -c:v libx264 -r 1 -pix_fmt yuv420p 3600fps.mp4
#

ffmpeg -framerate 1 -i ./output/%04d.jpg -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2" -c:v libx264 -r 1 -pix_fmt yuv420p 3600fps.mp4


