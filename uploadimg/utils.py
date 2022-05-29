import cv2
from PIL import Image
print(cv2.__version__)
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


# cv2.imread('D:\\image_merge_project\\uploadimg\\templates\\shirt.jpg')
def image_editor(logo, color, position, image_back):
    print(color)
    print(position)
    if (color=='grey'):
        img = cv2.imread(str(BASE_DIR / 'uploadimg/static/images/grey_shirt.jpg'))
    elif (color=='white'):
        img = cv2.imread(str(BASE_DIR / 'uploadimg/static/images/white_shirt.jpg'))
    else:
        img = cv2.imread(str(BASE_DIR / 'uploadimg/static/images/black_shirt.jpg'))
    #####For Front#####
    if logo:
        #### If pocket size has been choosen ####
        if (position=='pocket'):
            Image.open(logo).save("logo/logo_front.png")
            watermark = cv2.imread(str(BASE_DIR / 'logo/logo_front.png'))

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
            #####If width is larger than height######
            if (wm_w>wm_h):

                if wm_w >0 and wm_w<350 :
                    wm_scale = 15
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.7)
                    center_x = int(w_img/1.4)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/1)
                elif wm_w>=350 and wm_w <500 :
                    wm_scale = 10.140
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.7)
                    center_x = int(w_img/1.4)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/1)
                
                elif wm_w >= 500 and  wm_w<1000:
                    wm_scale = 7
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.7)
                    center_x = int(w_img/1.4)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/1)

                elif wm_w >= 1000 and wm_w<1500:
                    wm_scale = 4.837
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    print(wm_dim)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.7)
                    center_x = int(w_img/1.4)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/1)

                elif wm_w>= 1500 and wm_w<2000:
                    wm_scale = 3.3421
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width,wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.7)
                    center_x = int(w_img/1.4)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/1)

                elif wm_w>= 2000 and wm_w<2500:
                    wm_scale = 2.304
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.7)
                    center_x = int(w_img/1.4)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/1)

                elif wm_w>= 2500 and wm_w<3000:
                    wm_scale = 1.5927
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.7)
                    center_x = int(w_img/1.4)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/1)

                else:
                    wm_scale = 1.0993
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.7)
                    center_x = int(w_img/1.4)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/1)
    
                bottom_y = top_y + h_wm
                right_x = left_x + w_wm
                roi = resized_img[top_y:bottom_y, left_x:right_x]

                result = cv2.addWeighted(roi, 0, resized_wm, 1, 0)
                print (result)
                resized_img[top_y:bottom_y, left_x:right_x] = result
                filename = str(BASE_DIR / 'media/Front.jpg')
                cv2.imwrite(filename, resized_img)
                img = Image.fromarray(resized_img)
            #####If height is larger than width######
            #Scaledown ratio 1.44
            else:
                if wm_h < 500 :
                    wm_scale = 13
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/1.4)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/1)
                
                elif wm_h >= 500 and  wm_h<1000:
                    wm_scale = 9
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/1.4)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/1)

                elif wm_h >= 1000 and wm_h<1500:
                    wm_scale = 6.2
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/1.45)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/1)
                elif wm_h >= 1500 and wm_h<2000:
                    wm_scale = 4.3
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/1.4)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/1)

                elif wm_h>= 2000 and wm_h<2500:
                    wm_scale = 2.97
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/1.4)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/1)

                elif wm_h>= 2500 and wm_h <3000:
                    wm_scale = 2.05
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/1.4)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/1)

                else:
                    wm_scale = 1.42
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/1.4)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/1)
    
                bottom_y = top_y + h_wm
                right_x = left_x + w_wm
                roi = resized_img[top_y:bottom_y, left_x:right_x]

                result = cv2.addWeighted(roi, 0, resized_wm, 1, 0)
                print (result)
                resized_img[top_y:bottom_y, left_x:right_x] = result
                filename = str(BASE_DIR / 'media/Front.jpg')
                cv2.imwrite(filename, resized_img)
                img = Image.fromarray(resized_img)

        #### If chest size has been choosen ####
        else:
            Image.open(logo).save("logo/logo_front.png")
            pngimg = cv2.imread(str(BASE_DIR / 'logo/logo_front.png'))
            cv2.imwrite('logo/logo_front.jpg', pngimg, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
    
            watermark = cv2.imread(str(BASE_DIR / 'logo/logo_front.jpg'))

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

            if (wm_w>wm_h):
                if wm_w <350:
                    wm_scale = 40
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)

                elif wm_w >=350 and  wm_w<500:
                    wm_scale = 32
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                elif wm_w >= 500 and wm_w<750:
                    wm_scale = 25.6
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                elif wm_w >= 750 and wm_w<1000:
                    wm_scale = 18
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                
                elif wm_w>= 1000 and wm_w<1500:
                    wm_scale = 12.67
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                
                elif wm_w>= 1500 and wm_w<2000:
                    wm_scale = 8.92
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                elif wm_w>= 2000 and wm_w<2500:
                    wm_scale = 6.28
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                elif wm_w>= 2500 and wm_w<3000:
                    wm_scale = 4.42
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                
                else:
                    wm_scale = 3.11
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.6)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
            
            elif wm_h>wm_w:
                if wm_h<350:
                    wm_scale = 40
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                
                elif wm_h >=350 and  wm_h<500:
                    wm_scale = 32
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                
                elif wm_h >= 500 and wm_h<750:
                    wm_scale = 25.6
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.2)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                
                elif wm_h >= 750 and wm_h<1000:
                    wm_scale = 15.6
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)

                elif wm_h>= 1000 and wm_h<1500:
                    wm_scale = 12.67
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                
                elif wm_h>= 1500 and wm_h<1750:
                    wm_scale = 10.795
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.2)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                
                elif wm_h>= 1750 and wm_h<2000:
                    wm_scale = 8.92
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                elif wm_h>= 2000 and wm_h<2500:
                    wm_scale = 6.28
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                elif wm_h>= 2500 and wm_h<3000:
                    wm_scale = 4.42
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                else:
                    wm_scale = 3.11
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
            #####if square or other shapes####
            else:
                if wm_h<350:
                    wm_scale = 40
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                
                elif wm_h >=350 and  wm_h<500:
                    wm_scale = 32
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                
                elif wm_h >= 500 and wm_h<750:
                    wm_scale = 25.6
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                
                elif wm_h >= 750 and wm_h<1000:
                    wm_scale = 15.6
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                
                elif wm_h>= 1000 and wm_h<1500:
                    wm_scale = 12.67
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.2)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                
                elif wm_h>= 1500 and wm_h<2000:
                    wm_scale = 8.92
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                elif wm_h>= 2000 and wm_h<2500:
                    wm_scale = 6.28
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                elif wm_h>= 2500 and wm_h<3000:
                    wm_scale = 4.42
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)
                else:
                    wm_scale = 3.11
                    wm_width = int(watermark.shape[1] * wm_scale/100)
                    wm_height = int(watermark.shape[0] * wm_scale/100)
                    wm_dim = (wm_width, wm_height)
                    resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                    h_img, w_img, _ = resized_img.shape
                    center_y = int(h_img/2.3)
                    center_x = int(w_img/2)
                    h_wm, w_wm, _ = resized_wm.shape
                    top_y = center_y - int(h_wm/2)
                    left_x = center_x - int(w_wm/2)

            bottom_y = top_y + h_wm
            right_x = left_x + w_wm
            roi = resized_img[top_y:bottom_y, left_x:right_x]

            result = cv2.addWeighted(roi, 0, resized_wm, 1, 0)
            print (result)
            resized_img[top_y:bottom_y, left_x:right_x] = result
            filename = str(BASE_DIR / 'media/front.jpg')
            cv2.imwrite(filename, resized_img)
            img = Image.fromarray(resized_img)

    ###################### For back of the t-shirt ##################

    if image_back:
        Image.open(image_back).save("logo/logo_back.png")

        if (color=='grey'):
            img = cv2.imread(str(BASE_DIR / 'uploadimg/static/images/grey_shirt_back.jpg'))
        elif (color=='white'):
            img = cv2.imread(str(BASE_DIR / 'uploadimg/static/images/white_shirt_back.jpg'))
        else:
            img = cv2.imread(str(BASE_DIR / 'uploadimg/static/images/black_shirt_back.jpg'))

        Image.open(image_back).save("logo/logo_back.png")
        watermark = cv2.imread(str(BASE_DIR / 'logo/logo_back.png'))

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

        if (wm_w>wm_h):
            if wm_w <350:
                wm_scale = 40
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/3)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)

            elif wm_w >=350 and wm_w<500:
                wm_scale = 32
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/3)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
            elif wm_w >= 500 and wm_w<750:
                wm_scale = 25.6
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/3.0)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
            elif wm_w >= 750 and wm_w<1000:
                wm_scale = 18
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/3)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
                
            elif wm_w>= 1000 and wm_w<1500:
                wm_scale = 12.67
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/3)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
                
            elif wm_w>= 1500 and wm_w<2000:
                wm_scale = 8.92
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/3)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
            elif wm_w>= 2000 and wm_w<2500:
                wm_scale = 6.28
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/3)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
            elif wm_w>= 2500 and wm_w<3000:
                wm_scale = 4.42
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/3)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
                
            else:
                wm_scale = 3.11
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/3)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)     
        elif wm_h>wm_w:
            if wm_h<350:
                wm_scale = 40
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
                
            elif wm_h >=350 and  wm_h<500:
                wm_scale = 32
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
                
            elif wm_h >= 500 and wm_h<750:
                wm_scale = 25.6
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
                
            elif wm_h >= 750 and wm_h<1000:
                wm_scale = 15.6
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)

            elif wm_h>= 1000 and wm_h<1500:
                wm_scale = 12.67
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
                
            elif wm_h>= 1500 and wm_h<1750:
                wm_scale = 10.795
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
                
            elif wm_h>= 1750 and wm_h<2000:
                wm_scale = 8.92
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
            elif wm_h>= 2000 and wm_h<2500:
                wm_scale = 6.28
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
            elif wm_h>= 2500 and wm_h<3000:
                wm_scale = 4.42
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
            else:
                wm_scale = 3.11
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
        #####if square or other shapes####
        else:
            if wm_h<350:
                wm_scale = 40
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
                
            elif wm_h >=350 and  wm_h<500:
                wm_scale = 32
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
                
            elif wm_h >= 500 and wm_h<750:
                wm_scale = 25.6
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
                
            elif wm_h >= 750 and wm_h<1000:
                wm_scale = 15.6
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
                
            elif wm_h>= 1000 and wm_h<1500:
                wm_scale = 12.67
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
                
            elif wm_h>= 1500 and wm_h<2000:
                wm_scale = 8.92
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
            elif wm_h>= 2000 and wm_h<2500:
                wm_scale = 6.28
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
            elif wm_h>= 2500 and wm_h<3000:
                wm_scale = 4.42
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)
            else:
                wm_scale = 3.11
                wm_width = int(watermark.shape[1] * wm_scale/100)
                wm_height = int(watermark.shape[0] * wm_scale/100)
                wm_dim = (wm_width, wm_height)
                resized_wm = cv2.resize(watermark, wm_dim, interpolation=cv2.INTER_AREA)

                h_img, w_img, _ = resized_img.shape
                center_y = int(h_img/2.6)
                center_x = int(w_img/2)
                h_wm, w_wm, _ = resized_wm.shape
                top_y = center_y - int(h_wm/2)
                left_x = center_x - int(w_wm/2)

        bottom_y = top_y + h_wm
        right_x = left_x + w_wm
        roi = resized_img[top_y:bottom_y, left_x:right_x]

        result = cv2.addWeighted(roi, 0, resized_wm, 1, 0)
        print (result)
        resized_img[top_y:bottom_y, left_x:right_x] = result
        filename = str(BASE_DIR / 'media/back.jpg')
        cv2.imwrite(filename, resized_img)
        img = Image.fromarray(resized_img)

        return img
    return img