import cv2
import os
import numpy as np

#影片目錄
outputFolder = 'my_output'

#自動建立目錄
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

#圖片輸出用的計數器
outputCounter=0

#開啟網路攝影機
cap=cv2.VideoCapture(0)

#視訊大小設定,獲取禎寬度,獲取禎高度
sz = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fps = 20 #每秒輸出的fram,一般16~20

#輸出格式
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

#open and set props
vout = cv2.VideoWriter()
vout.open('outputHW.mp4',fourcc,fps,sz,True)

#初始化平均影像
ret,frame=cap.read()
avg = cv2.blur(frame,(4,4))
avg_float = np.float32(avg) #將影像存成float32的資料型態

cnt=0
while cnt<201:
    # 讀取一幅影格
    ret, frame = cap.read()
    ##putText輸出到視訊上,各引數依序是:照片/新增的文字/左上角座標/字型/字型大小/顏色/字型粗細
    cv2.putText(frame,str(cnt),(10,20),cv2.FONT_HERSHEY_PLAIN,1,(0,255,0),1,cv2.LINE_AA)
    vout.write(frame)
    cnt+=1
    
    # 若讀取至影片結尾，則跳出
    if ret == False:
      break

    # 模糊處理
    blur = cv2.blur(frame, (4, 4))

    # 計算目前影格與平均影像的差異值
    diff = cv2.absdiff(avg, blur)

    # 將圖片轉為灰階
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

    # 篩選出變動程度大於門檻值的區域
    ret, thresh = cv2.threshold(gray, 25, 255, cv2.THRESH_BINARY)

    # 使用型態轉換函數去除雜訊
    kernel = np.ones((5, 5), np.uint8)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)

    # 產生等高線
    cntImg, cnts, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    hasMotion=False
    for c in cnts:
        # 忽略太小的區域
        if cv2.contourArea(c) < 2500:
          continue
        hasMotion=True

        # 偵測到物體，可以自己加上處理的程式碼在這裡...

        # 計算等高線的外框範圍
        (x, y, w, h) = cv2.boundingRect(c)

        # 畫出外框
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    #畫出等高線
    cv2.drawContours(frame,cnts,-1,(0,255,255),2)  #frame=圖像;cnts=輪廓檢測模式;(0,255,255)=輪廓索引
    
    #顯示偵測結果影像
    cv2.imshow('frame',frame)
    cv2.waitKey(30)

    if hasMotion:
        #儲存有變動的影像
        cv2.imwrite('%s/output_%04d.jpg' %(outputFolder,outputCounter),frame) 
        outputCounter += 1
    
    # 更新平均影像
    cv2.accumulateWeighted(blur, avg_float, 0.01)
    avg = cv2.convertScaleAbs(avg_float)
cap.release()
