from PIL import Image
import PIL
import json

img = Image.open('/home/d4/arducam_images/039_rpi_v3_imx477_cam0.jpeg')
file = open('/home/d4/openpose_json/039_rpi_v3_imx477_cam0_keypoints.json')

data = json.load(file)

left_crop = data['part_candidates'][0]['3'][0]
right_crop = data['part_candidates'][0]['6'][0]
top_crop = data['part_candidates'][0]['1'][1]
bottom_crop = data['part_candidates'][0]['8'][1]

#crop according to dimensions
cropped_img = img.crop((left_crop, top_crop, right_crop, bottom_crop))

# save image
cropped_img.save("/home/d4/myflection/opencv_color/cropped_image.jpg")

