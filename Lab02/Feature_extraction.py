##Maryam Hashmi
#Lab 02 Machine Learning
#Feature Extraction for signature verification

from PIL import Image, ImageDraw

Signature="sign"
Binary="binary"
boxed="boxed"
#Opening Image
image = Image.open(Signature+'.jpg')
img = image.convert('1')
img.save(Binary+'.jpg')
#img.tobytes()

width,height=img.size
print ("width: ",width,"height: ", height)
limg=img.load()



#Finding the bounding box dimensions and centroid
w=0
h=0

#Bounding box
left=width
top=height
right=0
bottom=0

#Centroid
count=0
sum_x=0
sum_y=0
num_pixels=0

print 'left:',left,'top:',top,'right:',right,'bottom:',bottom
for w in range(0,width):
    for h in range(0,height):
#        print ("w:",w,"h:",h,"  ",img[w,h], end='')
        if limg[w,h]==0:
            if w<left:
                left=w
            if w>right:
                right=w
            if h<top:
                top=h
            if h>bottom:
                bottom=h
#            for centroid
            sum_x+=w
            sum_y+=h
            count+=1
#            .
        h=h+1
    w=w+1


print 'left:',left,'top:',top,'right:',right,'bottom:',bottom
avg_x=sum_x/count
avg_y=sum_y/count

print 'centeroid: ',avg_x,avg_y
#Drawing bounding box
im=img.copy()
img_draw=ImageDraw.Draw(im)
img_draw.rectangle((left,top,right,bottom), fill=None, outline=(0))
img_draw.point((avg_x,avg_y),fill=0)
img_draw.rectangle((left,top,avg_x,avg_y),  outline=(0))
img_draw.rectangle((avg_x,top,right,avg_y),  outline=(0))
img_draw.rectangle((avg_x,avg_y,right,bottom),  outline=(0))
img_draw.rectangle((left,avg_y,avg_x,bottom),  outline=(0))
im.save(boxed+'.jpg')



image=Image.open(boxed+'.jpg')
image=image.load()
bw_t={}

prev=255
curr=0
counter=0
for x in range(left,avg_x):
    for y in range (top,avg_y):
        curr=image[x,y]
        if (prev==0 and curr==255):
            counter+=1
        prev=curr
bw_t['top_left']=counter

prev=255
curr=0
counter=0
for x in range(avg_x,right):
    for y in range (top,avg_y):
        curr=image[x,y]
        if (prev==0 and curr==255):
            counter+=1
        prev=curr
bw_t['top_right']=counter      

prev=255
curr=0
counter=0
for x in range(avg_x,right):
    for y in range (avg_y,bottom):
        curr=image[x,y]
        if (prev==0 and curr==255):
            counter+=1
        prev=curr
bw_t['bottom_left']=counter  

prev=255
curr=0
counter=0
for x in range(left,avg_x):
    for y in range (avg_y,bottom):
        curr=image[x,y]
        if (prev==0 and curr==255):
            counter+=1
        prev=curr
bw_t['bottom_right']=counter 
        
print "\n \nBlack to white transition values in segmented triangles."           
for i in bw_t.keys():
    print i, bw_t[i]
        


       
    
