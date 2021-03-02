
from PIL import Image
import os
cwd = os.getcwd()
currentDir = os.getcwd() 
# imagePath =  cwd+ "\\test.jpg"
# outputPath = "Output Path" #example ./myWebPimage.webp
# quality = "Number of quality you want" #example 100

# im = Image.open(imagePath)
# im.save(outputPath,'webp',quality = quality)

saveImageAsExt = ".jpeg"

image_list = os.listdir()
print(image_list)

# for i in image_list:
# 	print(i)	


relevant_path = cwd
included_extensions = ['jpg','jpeg', 'bmp', 'png', 'gif']
file_names = [fn for fn in os.listdir(relevant_path)
              if any(fn.endswith(ext) for ext in included_extensions)]

print("-------------------------")
path = currentDir + "\\compressed\\"

	

def convertImgToWebp(ImgName,SaveImgAs):
	NewName = os.path.splitext(SaveImgAs)[0]
	image = Image.open(ImgName)
	image = image.convert('RGB')
	try:
		image.save(path+'\\'+NewName+".webp", 'webp')
	except FileNotFoundError: 
		os.makedirs(path)
		image.save(path+'\\'+NewName+".webp", 'webp')


def removeExifData(ImgName,SaveImgAs):
	NewName = os.path.splitext(SaveImgAs)[0]
	image = Image.open(ImgName)
	data = list(image.getdata())
	image_without_exif = Image.new(image.mode, image.size)
	image_without_exif.putdata(data)
	# new_image = image_without_exif.resize((1080,550))
	try:
		# new_image.save(path+'\\'+NewName+".jpeg") # enable if want to set size of image to 1080x550
		image_without_exif.save(path+'\\'+NewName+saveImageAsExt)  # enable only to Remove Exif Data
	except FileNotFoundError: 
		os.makedirs(path)
		# new_image.save(path+'\\'+NewName+".jpeg") # enable if want to set size of image to 1080x550
		image_without_exif.save(path+'\\'+NewName+saveImageAsExt) # enable only to Remove Exif Data
	# print("Processed "+ImgName + " Saved as " +NewName+".jpeg at" +path)
	print("Processed "+ImgName + " Saved as " +NewName+saveImageAsExt+" at" +path)

def SaveImgAsJpg(ImgName,SaveImgAs):
	NewName = os.path.splitext(SaveImgAs)[0]
	image = Image.open(ImgName)
	try:
		image.save(path+'\\'+NewName+saveImageAsExt)
	except FileNotFoundError: 
		os.makedirs(path)
		image.save(path+'\\'+NewName+saveImageAsExt)

def resizeImage(ImgName,SaveImgAs,newDimX,newDimY):
	NewName = os.path.splitext(SaveImgAs)[0]
	newImage = Image.open(ImgName)
	new_image=newImage.resize((newDimX,newDimY))
	try:
		new_image.save(path+'\\'+NewName+saveImageAsExt) 
	except FileNotFoundError: 
		os.makedirs(path)
		new_image.save(path+'\\'+NewName+saveImageAsExt)
	print("Processed "+ImgName + " Saved as " +NewName+saveImageAsExt+" at -" +path)

def divideImageDimensionsBY(ImgName,SaveImgAs,Valuex,ValueY):
	NewName = os.path.splitext(SaveImgAs)[0]
	newImage = Image.open(ImgName)
	new_image=newImage.resize((int(newImage.size[0]/Valuex),int(newImage.size[1]/ValueY)))
	try:
		new_image.save(path+'\\'+NewName+saveImageAsExt) 
	except FileNotFoundError: 
		os.makedirs(path)
		new_image.save(path+'\\'+NewName+saveImageAsExt)
	print("Processed "+ImgName + " Saved as " +NewName+saveImageAsExt+" at -" +path)


for i in file_names:
	# print(i)	
	# removeExifData(i,i)
	# SaveImgAsJpg(i,i)
	divideImageDimensionsBY(i,i,2,2)
	# convertImgToWebp(i,i+"_w")