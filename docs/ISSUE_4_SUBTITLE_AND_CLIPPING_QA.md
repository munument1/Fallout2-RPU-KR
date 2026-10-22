# 이슈 #4: 엔딩 자막 누락·글자 잘림 분리 검증

대상: https://github.com/munument1/Fallout2-RPU-KR/issues/4

## 소스에서 확인된 부분

- `mods/rpu/text/korean/cuts/nar_2.txt`, `nar_3.txt`와 같은 이름의
  `cuts_female` 파일은 영어 원문이었다. 이 네 파일의 두 줄을 한국어로 수정했다.
- `tools/build_translation.py`는 `mods/rpu`를 `data`로 합치고
  UTF-8 소스를 CP949로 변환한다. 번역 ZIP과 실제 게임 설치본은 별도로 대조해야 한다.
- `tools/audit_cut_subtitles.py`는 남성·여성 폴더의 한국어 없는 파일을
  목록으로 보고한다. `--verify-critical`은 수정한 `nar_2/3` 네 파일의
  한국어·행 번호·CP949 인코딩 및 남녀 일치만 실패 처리한다.
  영어가 남은 다른 파일은 아직 자동 번역하거나 임의로 검사 통과 처리하지 않는다.

## 실게임 확인이 필요한 부분

1. RPU 2.4.34 + 이번 번역 ZIP + 사용 중인 네이티브 엔진 설치기로 게임 준비.
2. 실제 선택된 `fallout2.cfg` 등의 `[system] language=korean`과
   `data/text/korean/cuts/nar_2.txt`, `nar_3.txt`의 설치 해시 확인.
   sfall의 `ddraw.ini`에서 별도 CFG 또는 여성 자막 경로를 사용하는지 확인.
3. 엔딩에서 `nar_2`와 `nar_3` 자막이 각각 두 줄 모두 한국어인지 확인.
   엔딩 분기는 테스트용 세이브나 합법적으로 확보한 재현 경로로 진입.
4. 잘림 화면은 엔진 적용 전후를 동일한 문장, 해상도, UI 배율, 창 모드로 캡처.
   `fallout2font.ini`에서 `[TEXT] Name/Size`, `[BUTTON] Name/Size`,
   `[MISC] Adjust/CodePage`도 기록한다.
5. 잘림 종류를 가로폭 초과, 세로줄 누락, 글리프 상하 절단, 스크롤 실패로 분류한다.
   `src/font_standalone.cpp`의 `TextOutput`, `TextOutputX`, `splitText`와
   `src/native_font_hooks.cpp`의 `NativeHeight`, `KoreanWordWrap`를
   해당 화면의 호출 경로가 확인된 뒤에만 수정한다.

**상태:** 자막 소스·패키징 회귀 방지까지만 검증. 실게임 자막 로딩 및 글자
잘림 재현은 미완료. 엔진 DLL, 실행 파일, sfall 설정은 수정하지 않았다.
