# 이슈 #4: 엔딩 자막 누락·글자 잘림 분리 검증

대상: https://github.com/munument1/Fallout2-RPU-KR/issues/4

## 소스에서 확인된 부분

- `mods/rpu/text/korean/cuts/nar_2.txt`, `nar_3.txt`와 같은 이름의
  `cuts_female` 파일은 영어 원문이었다. 이 네 파일의 두 줄을 한국어로 수정했다.
- `tools/build_translation.py`는 `mods/rpu`를 `data`로 합치고
  UTF-8 소스를 CP949로 변환한다. 번역 ZIP과 실제 게임 설치본은 별도로 대조해야 한다.
- `tools/audit_cut_subtitles.py`는 남성·여성 폴더의 한국어 없는 파일을
  목록으로 보고한다. `--verify-critical`은 수정한 `nar_2/3` 네 파일의
  한국어·행 번호·CP949 인코딩 및 남녀 일치에 실패하면 빌드를 막는다.
  후속 변경으로 영어 전용 자막 32종을 추가 번역했으며, 감사 도구는 이들 파일의
  번호 붙은 자막 행도 검사한다. 전 파일에서 영어만 존재하는 자막은 현재 0건이지만
  혼합 언어 문장과 실제 인게임 노출까지 전수 검수됐다는 뜻은 아니다.

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

## 후속 번역 검수 (2026-10-22)

- 영어만 남은 `nar_9`, `nar_10`~`nar_46` 가운데 보고된 미번역 파일 31종과
  추가 확인된 `nar_24`를 한국어로 옮겼다 (남성·여성 각 32개 파일).
- 번역문에는 원문과 같은 행 번호 및 순서를 유지했다. 화면별 종료/제어 표기로 추정되는
  `nar_34` 끝의 `x`, `nar_42/44/45/46` 끝의 단독 `1`은 원문 그대로 남겼다.
- 감사 도구는 전 파일에서 영어 전용 항목을 보고하고, 이 검수 완료 32종에서는
  각 번호 붙은 자막 행에 한글이 들어 있는지 검증하도록 확장했다.
- 원문과 번역문의 길이 차이가 있어 영상 자막 타이밍·출력 폭은 실제 게임에서 별도 확인해야 한다.

## 기존 잘림 수정과의 대조 (2026-10-22, GitHub 소스 기준)

**결론:** 이전 해결책은 확인됐지만, 이번 제보의 화면이 어떤 출력 경로인지와
제보자가 설치한 한글 엔진 바이너리 버전은 아직 모른다. 화면을 직접 열람한
재현 결과 없이 원인을 확정하거나 동일 바이너리 패치를 복사하지 않는다.

| 과거 수정 | 해당 화면/원인 | 현재 RPU와의 관계 |
| --- | --- | --- |
| Fallout2-Korean-Text-Engine 커밋 `25ca1646ec` (10/16) | 원본 wordWrap이 CP949 두 바이트 한글을 중간에서 자르던 문제, 게임 본문 폭 기준 줄 나눔 | 현 독립형 엔진에 포함. HRP 자체 메시지 기록창이 같은 함수를 호출하는지는 별도 확인 |
| 커밋 `72e5de6b60` (10/16) | 캐릭터 설명 카드의 임시 12줄 강제 잘림 철회 | 현 소스에 12줄 강제 제한 없음. 글자 겹침 없이 전부 화면에 보이는지는 별도 문제 |
| 커밋 `6053414955` (10/18), 엔진 v1.2.3 | 캐릭터 기술 18개 목록/슬라이더의 한 줄 간격 과다; 세 호출 주소(0x432A53, 0x436433, 0x436453)에만 11px 높이에서 1px 조정 | 제보 화면이 기술 목록이고 설치 DLL이 v1.2.3보다 오래된 경우 이미 해결된 이슈일 수 있음 |
| Fallout-1.5-Resurrection-KR 커밋 `ed95dc3b39e` (10/18), KR1.2 | **하단 메시지 기록창의 긴 한글이 오른쪽에서 잘림**. CP949 글자 단위/실제 픽셀 폭으로 HRP 줄맞춤 구현 | 증상이 같다면 참고할 핵심 원리. 그러나 Resurrection 전용 `f2_res.dll` 패치이며 RPU에 바이너리를 재사용할 수 없음 |

관련 소스:
- https://github.com/munument1/Fallout2-Korean-Text-Engine/blob/main/src/native_font_hooks.cpp
- https://github.com/munument1/Fallout2-Korean-Text-Engine/blob/main/src/font_standalone.cpp
- https://github.com/munument1/Fallout-1.5-Resurrection-KR/blob/main/tools/fix_resurrection_hrp.py
- https://github.com/munument1/Fallout-1.5-Resurrection-KR/blob/main/src/resurrection_monitor_fit.asm

레저렉션 KR1.2 패치는 **확인된 레저렉션 f2_res.dll 해시**만 허용하고,
해당 DLL의 RVA `0xF250`, `0xF2E0` 두 진입점을 `.krfit` 섹션으로 분기한다.
RPU의 `f2_res.dll`은 해시/함수 레이아웃 확인 전에는 이 위치가 같다고
판단할 수 없다. 현 네이티브 엔진 설치기는 원칙적으로 RPU의 원본 HRP DLL을
교체하지 않는다.

### 재현 분류 순서

1. 제보자의 **실제 fallout2font.dll SHA-256**과 엔진 설치본 출처를 확인한다.
   `fallout2font.ini`의 돋움 11 설정만으로 v1.2.3 DLL이라고 단정하지 않는다.
2. 잘리는 위치가 (A) 캐릭터 기술 목록/커서, (B) 캐릭터 설명 카드,
   (C) **하단 메시지 기록창**, (D) 기타 UI 중 무엇인지 구분한다.
   제보의 '기본/최대로 늘림'이 창 크기인지, 해상도 변경인지도 확인한다.
3. (A) v1.2.3 이전이면 안전한 복구 후 v1.2.3 재설치와 동일 화면 재시험.
   (B) 12줄 제거가 현 엔진에 반영됐는지 확인하고 원문 누락/영역 높이로 구분.
   (C) RPU의 `f2_res.dll` 해시 및 사용 중인 HRP 구성을 먼저 확인.
4. (C)가 확정되면 레저렉션 KR1.2와 **알고리즘만 비교**하고
   RPU 바이너리의 실제 함수 경로, 대상 바이트와 길이 측정 콜백을
   검증한 별도 소스 패치·회귀 시험으로 구현한다. 다른 버전 해시에는 실패 처리.
5. (D)는 해당 UI의 직전 메시지 길이, UI 폭/높이, 폰트 메트릭, 스크롤 처리와
   재현 가능한 호출 경로를 수집한 뒤 수정한다.

사용자 측 진단은 **원본 보존·읽기 전용**으로 실행한다. Windows PowerShell 예:

```powershell
Get-FileHash ".\fallout2font.dll" -Algorithm SHA256
Get-FileHash ".\f2_res.dll" -Algorithm SHA256
Get-Content ".\fallout2font.ini"
```

실제 게임 루트에서 실행하며 누락된 파일은 없는 그대로 기록한다.
개인 폴더 전체 경로나 세이브는 공개할 필요가 없다.

### 완료 조건

- 기존 v1.2.3 해결 범주면 수정 전/후 **동일 화면과 동일 문장** 비교로
  재발 여부 판단; 불필요한 중복 출력 엔진 패치 금지.
- 레저렉션과 같은 하단 기록창이면 RPU 현재 HRP 전용 수정 여부를 판단해
  실제 한글 문장과 여러 창 폭에서 오른쪽 글자 누락·CP949 분리 0건,
  상하 스크롤/이전 메시지 보존 확인.
- 모든 경우 이슈 #4의 게임 실증이 아직 없으므로 Issue는 열린 상태로 유지.
