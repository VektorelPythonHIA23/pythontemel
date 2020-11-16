
import cv2

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
yuz_cas = cv2.CascadeClassifier(r"EDIZ\OPENCV\cascades\haarcascade_frontalface_default.xml")
eye_cas = cv2.CascadeClassifier(r"EDIZ\OPENCV\cascades\haarcascade_eye.xml")
gozluk_res = cv2.imread(r"EDIZ\OPENCV\glass.png",-1)
def transparentOverlay(src, overlay, pos=(0, 0), scale=1):
    overlay = cv2.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image
 
    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
    return src

take = True
while True:
    if take:
        ret,frame = cap.read()
        gri = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        
        # yuzler = yuz_cas.detectMultiScale(gri,1.3,5)




        cv2.imshow("resim",frame)
    else:
        cv2.imshow("resim",res)
    if cv2.waitKey(2) & 0xFF == ord("t"):
        yuzler = yuz_cas.detectMultiScale(gri,1.3,5)
        for x,y,w,h in yuzler:
            if h>0 and w>0:
                gozluk_min = int(y + 1.5*h/5)
                gozluk_max = int(y + 2.5*h/5)
                gozluk = gozluk_max-gozluk_min
                roi = frame[y:y+h,x:x+w]
                roiglass = frame[gozluk_min:gozluk_max,x:x+w]
                gozluk_resim = cv2.resize(gozluk_res,(w,gozluk),cv2.INTER_CUBIC)
                transparentOverlay(roiglass,gozluk_resim)
        take = False
        res = frame.copy()
        from pygame import mixer  # Load the popular external library
        mixer.init()
        mixer.music.load(r'EDIZ\OPENCV\ogretmen.mp3')
        mixer.music.play()
    if cv2.waitKey(2) & 0xFF == ord("s"):
        take = True
        try:
            mixer.music.stop()
        except:
            pass        

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
