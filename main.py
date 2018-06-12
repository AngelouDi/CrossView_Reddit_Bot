from PIL import Image
import praw
import urllib.request


reddit = praw.Reddit(client_id='',
                     client_secret='',
                     username='',
                     password='',
                     user_agent='')


urllib.request.urlretrieve('', 'image.jpg') #saves url to file

image = Image.open('image.jpg') #opens an image

width = image.width #the width and the height of the image
height = image.height
half_width = int(round(width/2)) #we need to split it so we get the middle

right_eye = image.crop((0,0,half_width, height)) #in crossview the right and left are swapped
left_eye = image.crop((half_width+1, 0, width, height)) #so the left half is the right eye and vice versa

new_image = Image.new('RGB',(width, height)) #creates new image filew
new_image.paste(left_eye) #corrects eye sides for each eye
new_image.paste(right_eye,(half_width, 0, width, height))
new_image.save('New.jpg',format='jpeg') #creates the image file for parallel view