
from PIL import Image
import os
cwd = os.getcwd()
currentDir = os.getcwd() 
# imagePath =  cwd+ "\\test.jpg"
# outputPath = "Output Path" #example ./myWebPimage.webp
# quality = "Number of quality you want" #example 100

# im = Image.open(imagePath)
# im.save(outputPath,'webp',quality = quality)

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
	image = Image.open(ImgName)
	image = image.convert('RGB')
	try:
		image.save(path+'\\'+SaveImgAs+".webp", 'webp')
	except FileNotFoundError: 
		os.makedirs(path)
		image.save(path+'\\'+SaveImgAs+".webp", 'webp')


def RemoveExifData(ImgName,SaveImgAs):
	NewName = os.path.splitext(SaveImgAs)[0]
	image = Image.open(ImgName)
	data = list(image.getdata())
	image_without_exif = Image.new(image.mode, image.size)
	image_without_exif.putdata(data)
	# new_image = image_without_exif.resize((1080,550))
	try:
		# new_image.save(path+'\\'+NewName+".jpeg") # enable if want to set size of image to 1080x550
		# image_without_exif.save(path+'\\'+NewName+".jpeg")  # enable only to Remove Exif Data
		image_without_exif.save(path+'\\'+NewName+".png")  # enable only to Remove Exif Data
	except FileNotFoundError: 
		os.makedirs(path)
		# new_image.save(path+'\\'+NewName+".jpeg") # enable if want to set size of image to 1080x550
		# image_without_exif.save(path+'\\'+NewName+".jpeg") # enable only to Remove Exif Data
		image_without_exif.save(path+'\\'+NewName+".png") # enable only to Remove Exif Data
	# print("Processed "+ImgName + " Saved as " +NewName+".jpeg at" +path)
	print("Processed "+ImgName + " Saved as " +NewName+".png at" +path)

def SaveImgAsJpg(ImgName,SaveImgAs):
	NewName = os.path.splitext(SaveImgAs)[0]
	image = Image.open(ImgName)
	try:
		image.save(path+'\\'+NewName+".png")
	except FileNotFoundError: 
		os.makedirs(path)
		image.save(path+'\\'+NewName+".png")

# new_image = image.resize((


for i in file_names:
	# print(i)	
	# RemoveExifData(i,i)
	SaveImgAsJpg(i,i)
	# convertImgToWebp(i,i+"_w")