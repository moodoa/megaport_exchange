# megaport_exchange
用這個 app 來找到同名同姓的大港票買/賣家吧！

![alt text](https://miro.medium.com/v2/resize:fit:828/format:webp/1*4DwqO5pYPyb6OD95EdIqlw.png)


# 程式用法
![alt text](https://miro.medium.com/v2/resize:fit:828/1*uNSitUbN0bVIgu4kF0LoGA.gif)
#### 1.買票買爆！！：輸入自己的名字後把剩下的交給命運，系統會顯示之前所有同名同姓的使用者留言。如上圖。
#### 2.含淚賣出 QQ ：先幫QQ la。輸入自己的名字、票種、聯絡方式和任意一組數字當刪除碼，即可登錄留言。如上圖。
![alt text](https://miro.medium.com/v2/resize:fit:828/1*XM2mfoc2iLvxartrWcZLSw.gif)
#### 3.刪除資料XX：賣完票或忽然不想賣了嗎？輸入名字和刪除碼來刪除自己的留言ㄅ。如影片二。
#### 一些提醒：刪除碼不要太簡單，不然可能會被誤刪。可能會有個資被看到的風險，所以聯絡方式最好選個無關緊要又隱蔽的方法。

# 關於 AWS RDS 資料庫的設定
#### 1.進入 [AWS RDS 服務頁面](https://ap-northeast-1.console.aws.amazon.com/rds/home?) 後登入 AWS 帳號。
![alt text](https://cdn-images-1.medium.com/max/1000/1*UjO5DxwjoqJyFwIcnig1Rg.png)
#### 2.點選建立資料庫。依序選擇`標準建立`→`MySQL`→`免費方案`。
![alt text](https://cdn-images-1.medium.com/max/1000/1*8UZRkSDuaufwj0Y0BCIazw.png)
#### 3.主要使用者名稱和密碼要記得，在 Flask 主程式連資料庫時會用到。
![alt text](https://cdn-images-1.medium.com/max/1000/1*l1yfvlwGZLFP1zPB1a0lIw.png)
#### 4.公開存取這邊要選`是`，然後拉到最下面點`建立資料庫`。
#### 5.資料庫會需要花一段時間建立，此時進入[AWS EC2 服務頁面](https://ap-northeast-1.console.aws.amazon.com/ec2/v2/)做規則設定。
![alt text](https://cdn-images-1.medium.com/max/1000/1*26Ru2XncF5hRGmhOeW_Wxw.png)
#### 6.點選左方`網路和安全`中的`安全群組`。
![alt text](https://cdn-images-1.medium.com/max/1000/1*1grkKgRhsYrIenVGI1ZxWg.png)
#### 7.點選右下角`編輯傳入規則`。
![alt text](https://cdn-images-1.medium.com/max/1000/1*Uh1MH7SIV5WFj65EoHXP-w.png)
#### 8.先點選`刪除`後重新`新增規則`。類型選`所有流量`，來源選`隨處-IP4`並儲存。
![alt text](https://cdn-images-1.medium.com/max/1000/1*xhgEGS7nXqw-1Zr3OP3Ztg.png)
#### 9.下載[MySQL workbench](https://dev.mysql.com/downloads/file/?id=516912)。直接點選下方的`No thanks, just start my download.`可免註冊下載。
![alt text](https://cdn-images-1.medium.com/max/1000/1*V2spM04ViTF2fX7osm67vg.png)
#### 10.打開後點選`MySQL Connections`。在`Connection Name`輸入連線名字（隨意），`Hostname`輸入




