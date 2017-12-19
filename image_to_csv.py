import cv2

IMAGES_PATH = 'photos/'
FOLDERS = ['burger']

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

for folder in FOLDERS:
    load_images_from_folder(IMAGES_PATH + folder)
