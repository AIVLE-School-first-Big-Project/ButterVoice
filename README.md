<br>

# ๐ถ ButterVoice : CS ์๋ด์ฌ๋ฅผ ์ํ ๊ฐ์  ํํฐ๋ง ์๋น์ค
> 2022.04.11 ~ 2022.05.13 KT AIVLE ์ ๋จ/์ ๋ถ 2์กฐ ๋นํ๋ก์ ํธ<br>
>  *'ButterVoice'๋ ํญ์ธ๊ณผ ํ๋ฐ๊ณผ ๊ฐ์ ํ๊ฒฝ์ ๋ธ์ถ๋ CS์๋ด์ฌ๋ฅผ ์ํด ํ์์ ์์ฑ์ ๊ธฐ๋ฐ์ผ๋ก ๊ฐ์ ์ ๋ถ์ํ๊ณ  ์์ค์ด๋ ์๋ฌด์ ๋ถํ์ํ ๋จ์ด๋ค์ ์๋์ผ๋ก ํํฐ๋งํด์ ๋ค๋ ค์ฃผ๋ AI์๋น์ค์๋๋ค*
<img src="https://user-images.githubusercontent.com/37900424/167587333-419b0720-cb67-4e46-b269-f1fea3bc20b6.png" width="1000" height="352">

## ์กฐ์ ์๊ฐ
- `AI์ ๋จ/์ ๋ถ1๋ฐ 2์กฐ[18์กฐ]`
> ๊น๋ณด์ฐ(์กฐ์ฅ), ๊ฐ๊ฐ์, ์ ํค๋ฆฌ, ์ ๋ฌธ๊ฒฝ, ์ ์๋น


## ๋ชฉ์ฐจ
[1. ๊ฐ๋ฐ ๋ฐฐ๊ฒฝ ๋ฐ ๋ชฉ์ ](#1-๊ฐ๋ฐ-๋ฐฐ๊ฒฝ-๋ฐ-๋ชฉ์ )

[2. ๊ธฐ๋ฅ](#2-๊ธฐ๋ฅ-๋ฐ-UI/UX)

[3. ์๋น์ค FLOW](#3-์๋น์ค-FLOW)

[4. 3 Tier Architecture](#4-3-Tier-Architecture)

[5. DB ์ค๊ณ](#5-DB-์ค๊ณ)

[6. ๊ฐ๋ฐ ํ๊ฒฝ](#6-๊ฐ๋ฐ-ํ๊ฒฝ)

[7. ์ ์  ๊ฐ์ด๋](#7-์ ์ -)

***

## 1. ๊ฐ๋ฐ ๋ฐฐ๊ฒฝ ๋ฐ ๋ชฉ์ 
> ๐ก **'AI๊ธฐ์ ์ ํตํด ์ง์ ์ ์ธ ํญ์ธ๊ณผ ํ๋ฐ์ ๋ธ์ถ๋์ด์๋ CS์๋ดํ๊ฒฝ์ ๋ฐ๊พธ๊ธฐ ์ํด ๊ฐ๋ฐํ๊ฒ ๋์๋ค.'** ํ์ฌ ๊ณ ๊ฐ ์๋ด ์๋น์ค๋ ์๋์๋ต์ด๋ AI์๋น์ค๋ฅผ ์ด์ฉํด ๊ฐ๋จํ ์๋ฌด๋ ์ฒ๋ฆฌ๋๊ณ  ์์ง๋ง, ์ด๋ฌํ ์ธ๊ณต์ง๋ฅ ์๋น์ค๊ฐ ๋ณต์กํ ๊ณ ๊ฐ์ ์๊ตฌ๋ฅผ ๋ฃ๊ณ  ํด๊ฒฐํ๊ณ ์ ํ๋ ์๋ด์ฌ์ ์ญํ ์ ์์ ํ ๋์ฒดํ๊ธฐ์ ์ด๋ ค์์ด ์๋ค. ํ์ง๋ง, ์ด๋ฌํ CS์๋ฌด๋ ๊ฐ์ ์ ์ผ๋ก ๊ฒฉ์๋ ์ฌ๋๋ค์ ์ง์ ์ ์ผ๋ก ๋ํ๋ ์ผ์ด๋ค ๋ณด๋ ์ฌ์ ํ ๋ง์ ์๋ด์ฌ๋ค์ ๊ฐ์ ๋ธ๋์ผ๋ก ํผ๋ก๊ฐ์ ๋๋ผ๊ณ  ์๊ณ , ์ด๋ก ์ธํ ๊ทน๋จ์  ์ ํ ๋ฑ์ ์ฌํ์ ์ธ ๋ฌธ์ ๊ฐ ๊ณต๊ณต์ฐํ๊ฒ ์ผ์ด๋๊ณ  ์๋ค. ์ฆ, ์ฐ๋ฆฌ๋ ButterVoice๋ฅผ ํตํด ๊ธฐ์กด์ ์๋ดํ๊ฒฝ์ ํ์ ์ ์ผ์ผํค๊ณ ์ ํ๋ค.

<br>

- ๊ณ ๊ฐ์๋ด ์ ์ธ์ด์ ์ธ ํญ๋ ฅ์ผ๋ก ์ธํ ๊ฐ์ ๋ธ๋ ๋ฐ์

<br>

- `๊ธฐ์กด ์๋ด ์์คํ`
    - ์๋ ์๋ต์ด๋ AI์ฑ๋ด์ ํตํด์๋ ๊ฐ๋จํ ์๋ฌด๋ง ๋์ฒดํ  ์ ์์ 
    - ์ฌ์ ํ, ๋ณต์กํ ๊ณ ๊ฐ์ ์๊ตฌ์ฌํญ์ ์ฌ๋(์๋ด์ฌ)์ ์ํด์ ํด๊ฒฐ๋จ
    - ์คํ๋ ๋ฉํธ์ธ '์ง๊ธ ํตํ์ค์ธ ์๋ด์ฌ๊ฐ ๋๊ตฐ๊ฐ์ ๊ฐ์กฑ์๋๋ค'๋ก๋ ํญ๋ ฅ์ ์ธ ์ธ์ด๋ฅผ ๋ง์ ์ ์์
 
<br>

- ์์ ๊ฐ์ ์ฌํญ์ **๋ณด์**ํ๊ธฐ ์ํด **Butter Voice**(๋ฒํฐ ๋ณด์ด์ค)๋ฅผ ๊ธฐํ

<br>

- `๐ถ ButterVoice`
  - ํ์์ ์์ฑ์ ๊ธฐ๋ฐ์ผ๋ก ๊ฐ์ ์ ๋ถ์
  - ๊ฐ์ ์ํ๊ฐ ๊ฒฉ์๋์ด์์ผ๋ฉด ์๋ด์ฌ๊ฐ ๋ฃ๊ธฐ ํธํ ๋ชฉ์๋ฆฌ๋ก ๋ณ์กฐ
  - ์์ค์ด๋ ์๋ฌด์ ๋ถํ์ํ ๋จ์ด๋ค์ ์๋์ผ๋ก ํํฐ๋ง
  - ์๋ด ๋ด์ฉ์ ์๋์ผ๋ก ์์ฝ
  - ๊ธฐ์กด์ ์๋ด ํ๊ฒฝ์ ๊ธ์ ์ ์ผ๋ก ๊ฐ์ ํ  ์ ์์ ๊ฒ์ผ๋ก ์์

<br>


<br>

## 2. ๊ธฐ๋ฅ ๋ฐ UI/UX
- `์๋น์ค ์ฃผ์ ๊ธฐ๋ฅ`

<details>
  <summary>๋ฉ์ธ ํ๋ฉด</summary>
   <div markdown="1">       
     <br>
     <img src="https://user-images.githubusercontent.com/37900424/167593556-48e70081-1a25-4d6f-b3bd-fad01060fce0.gif" width="740" height="412">
     <br>
     <text>โ ๋ฒํฐ๋ณด์ด์ค์ ํํ๋ฉด์ผ๋ก ํ์๊ฐ์๊ณผ ๋ก๊ทธ์ธ์ ํ  ์ ์๋ ๋ฒํผ์ด ์๋ค</text>
   </div>
 </details>

 <details>
    <summary><strong>1) ๊ณ ๊ฐ๊ณผ ์๋ด์ฌ๋ฅผ ์ํ ํ์๊ฐ์/๋ก๊ทธ์ธ</strong></summary>
        <div markdown="1">  
            <h3>๐ ๊ณ ๊ฐ ํ์๊ฐ์</h3>
            <img src="https://user-images.githubusercontent.com/37900424/167593951-40108fc2-5f0e-4de0-b47f-6e9158c8fcca.png" width="700" height="412">
            <h3>๐ ์๋ด์ฌ ํ์๊ฐ์</h3>
            <img src="https://user-images.githubusercontent.com/37900424/167594017-ef9d7933-2321-4f06-a0c1-425ab7595cb8.png" width="700" height="412">
            <h3>๐ ๋ก๊ทธ์ธ</h3>
            <img src="https://user-images.githubusercontent.com/37900424/167591490-5825df2d-db94-44b9-9918-3a948bda1072.png" width="700" height="412">
        </div>
</details>
 
 <details>
  <summary><strong>2) ๊ณ ๊ฐ์ด ๋ก๊ทธ์ธ ํ์๋ ๋ค์ด๊ฐ๋ ๊ณ ๊ฐ ๋ฉ์ธ ํ์ด์ง</strong></summary>
   <div markdown="1"> 
    <br>      
     <img src="https://user-images.githubusercontent.com/37900424/167588687-ba52d2a5-bdc3-473b-a7ab-17808e5b9121.png" width="700" height="412">
     <br>
     <text>โ ๊ณ ๊ฐ์ด ์๋ดํ  ์ ์๋ ์๋ด์ฌ๋ฅผ ์ ํํด ์๋ด์ ์ ์ฒญํ  ์ ์๋ค</text>
   </div>
 </details>
 
 <details>
  <summary><strong>3) ๊ณ ๊ฐ์ด ์๋ด์ฌ์ ์ ํ์ฐ๊ฒฐ์ด ๋์์๋ ๋์ค๋ ํ์ด์ง</strong></summary>
   <div markdown="1">
     <br>      
     <img src="https://user-images.githubusercontent.com/37900424/167588939-154dae7b-b6ee-4481-a3a6-9981936e87c6.png" width="700" height="412">
     <img src="https://user-images.githubusercontent.com/37900424/167589023-d790e269-ddb8-499e-b900-0c6114a619b9.png" width="700" height="412">
     <br>
      <text>โ ์๋ด ์ ์๋ด ๋ฌธ๊ตฌ์ ๊ณ ๊ฐ์ด ์๋ด์ ์ข๋ฃํ๊ณ  ์ถ์ผ๋ฉด ๋๋ฅด๋ ์๋ด ์ข๋ฃ๋ฒํผ์ผ๋ก ๊ตฌ์ฑ</text>
   </div>
 </details>
 
 <details>
  <summary><strong>4) ์๋ด์ฌ์ ์๋ด์ด ์ข๋ฃ๋ ํ ์๋ด์ฌ์ ๋ํ ๋ณ์ ์ ์ค ์ ์๋ ๊ธฐ๋ฅ</strong></summary>
   <div markdown="1">  
   <br>     
     <img src="https://user-images.githubusercontent.com/37900424/167589301-13a71d5b-9388-480b-bca0-68a7a83e73fc.png" width="700" height="412">
     <br>
     <text>โ ์๋ด์ฌ์ ๋ํ ๋ณ์ ์ 1~5๊น์ง ์ค ์ ์๋ค</text>
   </div>
 </details>
 
 <details>
  <summary><strong>5) ์๋ด์ฌ๊ฐ ๋ก๊ทธ์ธํ์ ๋ ๋์ค๋ ์๋ด์ฌ ๋ฉ์ธ ํ์ด์ง</strong></summary>
   <div markdown="1">
   <br>
     <img src="https://user-images.githubusercontent.com/37900424/167589519-11745225-9cde-46b4-b0f6-ca0a83c50074.png" width="700" height="412">
     <br>
     <text>โ ์๋ด์ฌ๊ฐ ์ ํ๊ฐ ๊ฑธ๋ ค์จ ์์๋๋ก ์ ํ ๋๊ธฐ์๋ค์ ํ์ธ ํ  ์ ์๋ค </text>
   </div>
 </details>
 
 <details>
  <summary><strong>6) ์๋ด์ฌ๊ฐ ๊ณ ๊ฐ๊ณผ ์๋ด์ ์งํ์ค์ ๋์ค๋ ํ์ด์ง</strong></summary>
   <div markdown="1">  
     <br>
     <img src="https://user-images.githubusercontent.com/37900424/167589639-1e2351da-8657-4d84-8f31-a9cc0c664234.png" width="700" height="412">
     <br>
     <text>โ ๊ณ ๊ฐ ์๋ด ๋ฉ๋ด์ผ, ๊ณ ๊ฐ์ ๊ธฐ๋ณธ ์ ๋ณด, ๊ณ ๊ฐ๊ณผ ์๋ด์ ์ ๋ ์๋ด๋ด์ฉ ๊ธ์ฐ๊ธฐ ๋ฐ ์์  ๋ถ๋ถ์ผ๋ก ์ด๋ฃจ์ด์ ธ์๋ค</text>
     <br>
   </div>
 </details>
 
 <details>
  <summary><strong>7) ๊ด๋ฆฌ์๊ฐ ํ์์ผ๋ก ๋ฑ๋ก๋ ๊ณ ๊ฐ๊ณผ ์๋ด์ฌ์ ์ ๋ณด๋ฅผ ํ์ธํ  ์ ์๋ ๊ฒ์ํ</strong></summary>
   <div markdown="1">    
      <h3>๐ ์ ์ฒด ๊ฒ์ํ</h3>
     <img src="https://user-images.githubusercontent.com/37900424/167589721-b4aa89c8-0842-4c89-9b96-00a3b9316b87.png" width="700" height="412">
     <br>
      <h3>๐ฉ๐ปโ๐ซ ์๋ด์ฌ ์์ธ์ ๋ณด</h3>
        <img src="https://user-images.githubusercontent.com/37900424/167589786-ace9eba8-8e97-493f-9fa2-0da5ef66123d.png" width="700" height="412">    
       <h3>๐ฉ๐ป ๊ณ ๊ฐ ์์ธ์ ๋ณด</h3>
        <img src="https://user-images.githubusercontent.com/37900424/167589851-887aecff-4490-436a-918f-97acf01d563a.png" width="700" height="412">
     <br>
     <text>โ ๊ณ ๊ฐ์ ๋ณด๊ฒ์ํ/์๋ด์ฌ์ ๋ณด๊ฒ์ํ์ผ๋ก ์ด๋ฃจ์ด์ ธ์๋ค. ๊ณ ๊ฐ์์ธ์ ๋ณดํ์ด์ง์์๋ ๊ณ ๊ฐ์ ์๋ด๋ด์ฉ์ ๋ํด ์์  ๋ฐ ์ญ์ ๊ฐ ๊ฐ๋ฅํ๋ค</text>
   </div>
 </details>
 <br>

 - `AI ์ฃผ์ ๊ธฐ๋ฅ`
 <details>
    <summary><strong>1) ํ์์ ์์ฑ์ ๊ธฐ๋ฐ์ผ๋ก ๊ฐ์ ์ ๋ถ์</strong></summary>
    <text>โ CNN ๊ธฐ๋ฐ ์ ์ด ํ์ต์ ์ด์ฉํ ์์ฑ ๊ฐ์  ์ธ์</text>
 </details>
  <details>
    <summary><strong>3) ํ์์ ์ธ์ด ์ค์์ ์์ค์ด ์์ผ๋ฉด ํํฐ๋ง</strong></summary>
    <text>โ STT + ์์ค ํํฐ๋ง</text>
 </details>
  <details>
    <summary><strong>2) ๊ฐ์  ์ํ๊ฐ ๊ฒฉ์ ๋์ด์์ผ๋ฉด ๋ฃ๊ธฐ ํธํ ๋ชฉ์๋ฆฌ๋ก ๋ณ์กฐ</strong></summary>
    <text>โ Google์ gTTS ์ฌ์ฉ</text>
 </details>
 
  - `ํน๋ณํ ์ถ๊ฐ ๊ธฐ๋ฅ`
 <details>
    <summary><strong>1) WebRTC๊ธฐ๋ฐ P2P ์๋ด ์๋น์ค</strong></summary>
       <img src="https://user-images.githubusercontent.com/37900424/167592692-da61826c-1fc9-4bdb-b647-92d3e921fc0c.png" width="700" height="412"><br>
    <text>โ ์์ ์ ์ธ WebRTC ๊ธฐ๋ฅ์ ํตํด ์๋น์ค ์์ฑ๋ UP! </text>
 </details>
  <details>
    <summary><strong>2) Voice๋ฟ๋ง ์๋๋ผ ํ์ ํตํ ๊ฐ๋ฅ</strong></summary>
       <img src="https://user-images.githubusercontent.com/37900424/167592754-41d3a2a2-51a7-45fc-a87b-e49569f4c64e.png" width="700" height="412"><br>
    <text>โ ๊ณ ๊ฐ์ ์ผ๊ตด์ ๋ง์ฃผํ๋ฉฐ ๋น์ธ์ด์  ์ํต์ด ๊ฐ๋ฅ</text>
 </details>

<br>

<br>

## 3. ์๋น์ค FLOW
  - `์ฃผ์ ๊ธฐ๋ฅ Flow`
 ![์๋น์ค ํ๋ฆ](https://user-images.githubusercontent.com/37900424/163581807-3685f275-c2bd-43ed-8bfc-b6feeabf1de5.png)
  - `์๋น์ค Flow`
 ![์๋น์คFLOW](https://user-images.githubusercontent.com/37900424/163585048-496805b3-e3aa-4597-9d7d-736b017ab9fe.png)
<br>

## 4. 3 Tier Architecture
 
 ![์ํคํ์ณ](https://user-images.githubusercontent.com/37900424/163578007-4de44cbd-4a67-4b0a-b844-958384dfe695.png)


<br>

## 5. DB ์ค๊ณ
  - `ERD`
![Butter ERD](https://user-images.githubusercontent.com/43737828/167744005-b16d0eb8-c43c-40ea-836d-5a31434c264b.PNG)

<br>

## 6. ๊ฐ๋ฐ ํ๊ฒฝ

- `Front-End`

  |HTML|CSS|JS|Bootstrap|
  |:---:|:---:|:---:|:---:|
  |![html](https://user-images.githubusercontent.com/68097036/151471705-99458ff8-186c-435b-ac5c-f348fd836e40.png)|![css](https://user-images.githubusercontent.com/68097036/151471805-14e89a94-59e8-468f-8192-c10746b93896.png)|![js](https://user-images.githubusercontent.com/68097036/151471854-e0134a79-b7ef-4a0f-99fd-53e8ee5baf50.png)|![bootstrap](https://user-images.githubusercontent.com/68097036/151480381-2b23a8af-c6b4-43a6-96a6-ea69e0b953e0.png)|


- `Back-End and Cloud`

  |Python|Django|MySQL|HeidiSQL|WebRTC|AWS|
  |:---:|:---:|:---:|:---:|:---:|:---:|
  |![pngwing com](https://user-images.githubusercontent.com/68097036/151479684-a85d26d4-e79e-47c9-9023-bf6d92f57536.png)|![pngwing com (1)](https://user-images.githubusercontent.com/68097036/151466729-9cad0405-85ad-454e-815a-1a4fd065f8b7.png)|![pngwing com (2)](https://user-images.githubusercontent.com/68097036/151466853-2b56fd0f-3aa9-424e-b17b-1c7cd991ffbf.png)|<img src="https://user-images.githubusercontent.com/68097036/151467351-5a359330-8d81-47b9-a33f-f7a5e0d69319.png" width="120" height="120">|![WEBRTC](https://user-images.githubusercontent.com/37900424/163582496-b5df138c-07de-4e0b-a1b9-cea03b4f0fc3.png)|![AWS](https://user-images.githubusercontent.com/37900424/163412651-7bc435ac-ce9b-4de0-add1-f12b9abbc606.png)|


- `Etc`

  |Summernote|VS Code|Microsoft Teams|GitHub|Notion|
  |:---:|:---:|:---:|:---:|:---:|
  |![brand_summernote_icon_157332](https://user-images.githubusercontent.com/68097036/151470431-2b196263-3c3f-425d-8fd0-0d6cf440e3d1.png)|<img src="https://user-images.githubusercontent.com/68097036/151479933-01785e34-1283-4fca-a407-9fe284b50fa8.png" width="220" height="100">|![pngwing com (4)](https://user-images.githubusercontent.com/68097036/151467837-2cd89acd-2a92-45dd-b06b-e08e316b7695.png)|<img src="https://user-images.githubusercontent.com/68097036/151467910-0fda00cd-c08b-4869-a21e-a66d1d133ff5.png" width="220" height="100">|<img src="https://user-images.githubusercontent.com/68097036/151468186-82e630d3-8c3c-4c75-8243-e1efcba34926.png" width="220" height="130">|

<br>

<br>

## 7. ์ ์  ๊ฐ์ด๋
### **[1PC] ์คํ ๋ฐฉ๋ฒ**

#### 1.๊ฐ์ํ๊ฒฝ ์ค์ 

python -m venv (๊ฐ์ํ๊ฒฝ์ด๋ฆ)

#### 2. Requiremetns

pip install -r requirments.txt

#### 3. ์คํ

python manage.py runserver
<br>
### **[2PC] ์คํ ๋ฐฉ๋ฒ**

#### 1.๊ฐ์ํ๊ฒฝ ์ค์ 

python -m venv (๊ฐ์ํ๊ฒฝ์ด๋ฆ)

#### 2. Requiremetns

pip install -r requirments.txt

#### 3. IPํ์ธ

- CMD ์ฐฝ์์ ipconfig์๋ ฅ ํ ipv4 ์ฃผ์ ํ์ธ
- settings.py์ ALLOWED_HOSTS = ['ipv4 ์ฃผ์']

#### 4. ์คํ

python manage.py runsslserver 0.0.0.0:8000

<br><br><br>
<br><br><br>
###### Readme ํํ๋ฆฟ ์ฐธ๊ณ  : ์ ๋จ/์ ๋ถ1๋ฐ ์์ง์
