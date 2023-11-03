def viewPicture():
  file = pickAFile()
  pict = makePicture(file)
  pixel = getPixel(pict, 0, 0)
  pixels = getPixels(pict)
  print "width is", getWidth(pict), "height is", getHeight(pict)
  print "The value of the pixel at 0, 0 is: ", pixel
  print "A different way to get the pixel at 0, 0 is: ", pixels[0]
  explore(pict)

def printColor():
  color=pickAColor()
  print color
  
#program 16, page 69
def negative(picture):
  for px in getPixels(picture):
    red=getRed(px)
    green=getGreen(px)
    blue=getBlue(px)
    negColor=makeColor(255 - red, 255 - green, 255 - blue)
    setColor(px, negColor)
  show(picture)
  repaint(picture)
    
def negative2(picture):
  for x in range(0,getWidth(picture)):
    for y in range(0,getHeight(picture)):
      pixel = getPixel (picture, x, y)
      red = getRed(pixel)
      green = getGreen(pixel)
      blue = getBlue(pixel)
      negColor = makeColor(255 - red, 255 - green, 255 - blue)
      setColor(pixel, negColor)
  show(picture)
  repaint(picture)

def returnPicture():
  file=pickAFile()
  pict=makePicture(file)
  return pict
  
def changePixel(picture):
   for px in getPixels(picture):
     negatePixel(px)
   show(picture)
   repaint(picture)
   
def negatePixel(pixel):
  red = getRed(pixel)
  green = getGreen(pixel)
  blue = getBlue(pixel)
  negColor = makeColor(255 - red, 255 - green, 255 - blue)
  setColor(pixel, negColor)
    
def changePixel2(picture, option):
#  valid option values are:
#  1. Negate the image
#  2. Lighten the picture
#  3. Reduce the red
#  4. Convert to Grayscale
#  5. Blend with white
  if int(option)==1:
    for px in getPixels(picture):
      negatePixel(px)
  elif int(option)==2:
    for px in getPixels(picture):
      lightenPixel(px)
  elif int(option)==3:
    for px in getPixels(picture):
      reduceRedPixel(px)
  elif int(option)==4:
    for px in getPixels(picture):
      grayScalePixel(px)
  elif int(option)==5:
    for px in getPixels(picture):
      blendWhite(px,.30) #second argument specifies proportion of white
  else:
    print "not implemented yet"   
  show(picture)
  repaint(picture)
      
    
def lightenPixel(pixel):
  color=getColor(pixel)
  color=makeLighter(color)
  setColor(pixel, color)
  
def reduceRedPixel(pixel):
  value=getRed(pixel)
  setRed(pixel,value*0.5)

def grayScalePixel(pixel):
  newRed = getRed(pixel)*0.299
  newGreen = getGreen(pixel)*0.587
  newBlue = getBlue(pixel)* 0.114
  luminance = newRed+newGreen+newBlue
  setColor(pixel, makeColor(luminance,luminance,luminance))
   
def blendWhite(pixel, amount):
  newRed = 255*amount + getRed(pixel)*(1-amount)
  newGreen = 255*amount + getGreen(pixel)*(1-amount)
  newBlue = 255*amount + getBlue(pixel)*(1-amount)
  setColor(pixel, makeColor(newRed, newGreen, newBlue))
  
#modified from page 86 program 24
#use setMediaPath() before calling this function--can have argument of your chosen directory--otherwise, file picker
def copyCaterpillar():
  catFile=getMediaPath("caterpillarSmall.jpg")
  catPict=makePicture(catFile)
  width=getWidth(catPict)
  height=getHeight(catPict)
  canvas=makeEmptyPicture(width,height)
  #Now, do the actual copying
  for x in range(0, width):
    for y in range(0, height):
      color=getColor(getPixel(catPict, x, y))
      setColor(getPixel(canvas, x, y), color)
  show(catPict)
  show(canvas)
  return canvas
  
#use setMediaPath() before calling this function
def copyAndMirrorCat():
  catFile=getMediaPath("caterpillarSmall.jpg")
  catPict=makePicture(catFile)
  width=getWidth(catPict)
  height=getHeight(catPict)
  canvas=makeEmptyPicture(width,height)
  #Now, do the actual copying
  for x in range(0, width/2):
    for y in range(0, height):
      color=getColor(getPixel(catPict, x, y))
      setColor(getPixel(canvas, x, y), color)
      setColor(getPixel(canvas,width-x-1,y),color)
  show(catPict)
  show(canvas)
  return canvas
  
  
def writePict(pict,name):
  file=getMediaPath(name)
  writePictureTo(pict,file)
  