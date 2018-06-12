from PIL import Image

image = Image.open('image.jpg')

width = image.width
height = image.height
half_width = int(round(width/2))

right_eye = image.crop((0,0,half_width, height))
left_eye = image.crop((half_width+1, 0, width, height))

new_image = Image.new('RGB',(width, height))
new_image.paste(left_eye)
new_image.paste(right_eye,(half_width, 0, width, height))
new_image.save('New.jpg',format='jpeg')