<div align="center">
  <h1>📊 메이플스토리 디스코드 봇</h1>
  <p>캐릭터 환산, 테섭 정보, 아즈모스 손익 계산정보 확인</p>
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/discord.py-2.5.2-blue?logo=discord" />
  <img src="https://img.shields.io/badge/license-GNU--GPL--v3-blue" />
</div>

---

## 📌 프로젝트 소개

길드원들이 자주쓰는 기능들을<br>
'인터넷 실행 -> 사이트 검색'<br>
과정없이 편하게 쓰게 하려고 제작한 디스코드 봇입니다.


다음과 같은 기능 제공.

- 캐릭터 환산 확인(스카우터)
- 보스 배율 바로가기
- 테스트 서버 공지 확인(정확히는 업데이트(=패치내역) 부분만)
- 아즈모스 손익 계산기

---

## 🚀 주요 기능

✅ prefix 명령어(!) 지원  
✅ 실시간 정보 조회 및 링크 버튼 제공  

---

## 🖼️ 미리보기 (사용 예시)
< **환산** 명령어 사용 예시 ><br>
![image](https://github.com/user-attachments/assets/d0d4dd2f-18d6-4ec1-896c-ef0d69aa98db)
![image](https://github.com/user-attachments/assets/285f8608-6ecc-4852-b52b-2d83535da1d5)<br><br>
< **테스트서버 정보** 명령어 사용 예시 ><br>
![image](https://github.com/user-attachments/assets/ab792407-fffc-4d05-b517-2d4bd5a29afe)<br><br>
< **아즈모스 손익계산** 명령어 사용 예시 ><br>
![image](https://github.com/user-attachments/assets/65d92499-82e4-4f38-ab3c-7c00b6d1ba88)



---

## 🔧 설치 방법

### 1. 의존성 설치

```bash
pip install -r requirements.txt
```


### 2. 환경 변수 설정

1. `env.example` 파일을 열고 `DISCORD_BOT_TOKEN`에 실제 봇 토큰을 입력하세요.

```env
DISCORD_BOT_TOKEN=your_real_token_here
```
2. 파일명을 `.env`로 변경합니다.

---
## 🧪 사용 방법

* `!스카우터` `!환산 [캐릭터명]`<br>
  └ 캐릭터명 입력 시 해당 캐릭터 환산 정보 링크로 이동  
　  입력하지 않으면 메이플 환산 메인 사이트로 이동

* `!보스` `!배율 [캐릭터명]`<br>
  └ 캐릭터명 입력 시 해당 캐릭터 보스 배율 정보로 이동  
　  입력하지 않으면 메이플 환산 메인 사이트로 이동

* `!테섭` `!업데이트` `!업뎃`<br>
  └ 테스트월드 최신 공지사항 목록 출력

* `!손익`, `!가격`, `!주화`<br>
  └ 아즈모스 손익 계산 결과 출력


---

## ⚠️ 주의 사항

* 이 봇은 [환산 주스탯](https://maplescouter.com)과 [메이플스토리 테스트월드](https://maplestory.nexon.com/Testworld/Main), [메애기](https://meaegi.com)의 데이터를 참고합니다.
* 넥슨 또는 공식 메이플스토리와는 무관한 **비공식 프로젝트**입니다.

---

## 📜 라이선스

이 프로젝트는 [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)을 따릅니다.

---

## 🙌 문의

* 개선 제안이나 버그는 Issues 탭을 통해 알려주세요.
