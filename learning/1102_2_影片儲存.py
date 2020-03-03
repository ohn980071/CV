import cv2

#開啟網路攝影機
cap=cv2.VideoCapture(0)

#視訊大小設定,獲取禎寬度,獲取禎高度
sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

fps = 20 #每秒輸出的fram,一般16~20
#輸出格式
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

#open and set props
vout = cv2.VideoWriter()
vout.open('output.mp4',fourcc,fps,sz,True)
cnt=1
while cnt<201:
    _,frame = cap.read()
    ##putText輸出到視訊上,各引數依序是:照片/新增的文字/左上角座標/字型/字型大小/顏色/字型粗細
    cv2.putText(frame,str(cnt),(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),1,cv2.LINE_AA)
    vout.write(frame)
    cnt += 1

    cv2.imshow('vidio',frame)
    cv2.waitKey(30)

vout.release()
cap.release()