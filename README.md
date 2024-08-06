# grass-desktop-ubuntu
利用docker架設ubuntu 22.04運行grass-desktop-node 以達到兩倍收益  
如果覺得此項目還不錯可以幫我點個星星  
也可以使用我的[grass邀請碼](https://app.getgrass.io/register/?referralCode=mdoUst0zZ4r5FQa)(**不會影響原有積分**)

## 優缺點
### 優點
* 使用 grass-desktop-node 積分兩倍
* 利用網頁可以快速進入vnc查看當前裝況
### 缺點
* grass應用程式還是需要使用者自行輸入帳密進行登入
* 因為是使用ubuntu完整版導致image檔案過大

## 快速啟動 🚀
你可以依照下列方法快速使用，要注意下方指令要把your_email以及your_password替換為grass的帳號及密碼
- ### Docker cli 🐳
  ```bash
  docker run -d -p 5900:5900 -p 6080:6080 --name grass-desktop-node -e email=your_email -e password=your_password jianzhe61/grass-desktop-ubuntu
  ```
## 操作畫面
![螢幕擷取畫面 2024-08-06 153841](https://hackmd.io/_uploads/ryGsmIJ9A.png)

  
## 操作教學
1. 登入[http://localhost:6080/vnc.html](http://localhost:6080/vnc.html)會進入到novnc的介面(**注意 localhost 要取代為dockre宿主機的ip**)![螢幕擷取畫面 2024-08-06 151026](https://hackmd.io/_uploads/Sy-tnSkc0.png)

2. 接著按下連線即可連線到ubuntu，進入後會出現這個提示，按下remove即可![螢幕擷取畫面 2024-08-06 152127](https://hackmd.io/_uploads/rkHM1Ly5A.png)
3. 等待程式執行直到出現下方畫面，如果順利出現代表grass已經自動安裝完成
![螢幕擷取畫面 2024-08-06 152910](https://hackmd.io/_uploads/Hyxk-Lk5C.png)
4.點選左上角Applications，接著在Development找到Grass給他點下去![螢幕擷取畫面 2024-08-06 153121](https://hackmd.io/_uploads/By95-L150.png)
5.出現grass程式介面後要自行輸入帳號密碼進行登入(**如果要輸入大寫請用shirt加上英文健**)![螢幕擷取畫面 2024-08-06 153412](https://hackmd.io/_uploads/rkxzMLkcA.png)
6.可以把開機自動登入以及自動更新打開，到這邊就大功告成了![螢幕擷取畫面 2024-08-06 153756](https://hackmd.io/_uploads/BJbr7UJ5R.png)
