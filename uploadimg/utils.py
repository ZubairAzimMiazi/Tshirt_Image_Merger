import cv2
from PIL import Image
print(cv2.__version__)
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


# cv2.imread('D:\\image_merge_project\\uploadimg\\templates\\shirt.jpg')
def image_editor(logo, color, position):

    img = cv2.imread(str(BASE_DIR / 'uploadimg/static/images/shirt.jpg'))

    Image.open(logo).save("logo/logo.jpg")
    watermark = cv2.imread(str(BASE_DIR / 'logo/logo.jpg'))

    percent_of_scaling = 50
    new_width = int(img.shape[1] * percent_of_scaling/100)
    new_height = int(img.shape[0] * percent_of_scaling/100)
    new_dim = (new_width, new_height)
    print(new_dim, "new_dim")
    resized_img = cv2.resize(img, new_dim, interpolation=cv2.INTER_AREA)

    wm_w = watermark.shape[1]
    wm_h = watermark.shape[0]
    wm_dimension= (wm_w,wm_h)
    print(wm_dimension, "wm_dimension")

    if wm_dimension < new_dim :
        wm_scale = 50
        wm_width = int(watermark.shape[1] * wm_scale/100)
        wm_height = int(watermark.shape[0] * wm_scale/100)
        wm_dim = (wm_width, wm_height)
        resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)
    elif wm_dimension >(450,599) and  wm_dimension<(900,900):
        wm_scale = 20
        wm_width = int(watermark.shape[1] * wm_scale/100)
        wm_height = int(watermark.shape[0] * wm_scale/100)
        wm_dim = (wm_width, wm_height)
        resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)
    elif wm_dimension >= (900, 900) and wm_dimension<(2000,2000):
        wm_scale = 10
        wm_width = int(watermark.shape[1] * wm_scale/100)
        wm_height = int(watermark.shape[0] * wm_scale/100)
        wm_dim = (wm_width, wm_height)
        resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)
    elif wm_dimension>= (2000,2000) and wm_dimension<(2400,2400):
        wm_scale = 5
        wm_width = int(watermark.shape[1] * wm_scale/100)
        wm_height = int(watermark.shape[0] * wm_scale/100)
        wm_dim = (wm_width, wm_height)
        resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)
    elif wm_dimension>= (2400,2400):
        wm_scale = 2
        wm_width = int(watermark.shape[1] * wm_scale/100)
        wm_height = int(watermark.shape[0] * wm_scale/100)
        wm_dim = (wm_width, wm_height)
        resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)
    else:
        wm_scale = 2
        wm_width = int(watermark.shape[1] * wm_scale/100)
        wm_height = int(watermark.shape[0] * wm_scale/100)
        wm_dim = (wm_width, wm_height)
        resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)
    
    h_img, w_img, _ = resized_img.shape
    center_y = int(h_img/2.5)
    center_x = int(w_img/2)
    h_wm, w_wm, _ = resized_wm.shape
    top_y = center_y - int(h_wm/2)
    left_x = center_x - int(w_wm/2)
    bottom_y = top_y + h_wm
    right_x = left_x + w_wm
    roi = resized_img[top_y:bottom_y, left_x:right_x]

    result = cv2.addWeighted(roi, 1, resized_wm, 1, 0)
    resized_img[top_y:bottom_y, left_x:right_x] = result
    img = Image.fromarray(resized_img)

    return img