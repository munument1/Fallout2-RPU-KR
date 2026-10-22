# 넥서스 모드 #186 업데이트 준비본 (2026-10-22)

대상: https://www.nexusmods.com/fallout2/mods/186

## 넥서스 파일 버전
- 기존: `2.4.34-kr1.1`
- 새 업로드 제안: **`2.4.34-kr1.2`** (GitHub 릴리즈는 `v2.4.34-native.1`)
- 권장 메인 파일: `RPU-KR-v2.4.34-with-HRP-fix.zip`
- 선택/별도 파일: `korean-classic-data.zip` (다른 HRP를 사용하는 사용자는 번역 전용 ZIP만)

## 요약 문구

Fallout 2 RPU 2.4.34용 한국어판. 영어로 남아 있던 엔딩 자막 34종을 번역하고, 하단 메시지 기록창에서 긴 한글 문장의 오른쪽이 잘리는 오류를 수정했습니다. Fallout 2 Korean Text Engine v1.2.3이 필요합니다.

## 변경 내역 / Changelog (2.4.34-kr1.2)

- 엔딩 자막의 `nar_2/3`을 포함한 영어 전용 34종을 한국어 번역(남/여).
- 기존 Fallout 1.5 Resurrection KR1.2에서 해결한 CP949 한글 줄바꿈 오류 수정 코드를 RPU 2.4.34에 적용.
- RPU 2.4.34 원본 `f2_res.dll`이 해당 수정의 검증된 원본과 SHA-256까지 동일함을 확인.
- 메시지창 줄바꿈에 실제 글꼴 픽셀 폭과 CP949 문자 경계를 반영.
- 자막 파일 254개, CP949 변환, 수정 DLL 구조 및 통합 ZIP 자동 검사 통과.
- 기존 RPU 실행 파일 및 sfall `ddraw.dll`은 교체하지 않음.

## 설치

1. 공식 **Fallout 2 Restoration Project, Updated 2.4.34**가 설치된 Fallout 2 폴더를 백업합니다.
2. **다른 모드가 `f2_res.dll`을 변경하지 않았다면** 권장 `RPU-KR-v2.4.34-with-HRP-fix.zip`의 모든 파일을 `fallout2.exe`가 있는 폴더에 덮어씁니다.
3. [Fallout 2 Korean Text Engine v1.2.3](https://www.nexusmods.com/fallout2/mods/185)를 설치합니다. 이미 설치된 1.2.3은 다시 설치할 필요 없습니다.
4. 평소 게임 실행기로 실행합니다.

**주의:** 통합판에 들어 있는 수정 `f2_res.dll`은 RPU 2.4.34 공식 원본 전용입니다. 모드팩이나 다른 버전의 HRP를 사용하는 경우 `korean-classic-data.zip`을 사용해야 합니다. 기존 DLL을 백업하세요.

## 검증 수준

RPU 2.4.34의 원본 DLL이 과거 레저렉션 KR1.2의 인게임 검증된 원본 DLL과 같음을 확인했습니다. CI에서 전체 자막 감사, 무손실 패키징, 수정된 DLL 함수 2곳, ZIP 구조를 검사했습니다. RPU 환경의 모든 화면/장시간 플레이를 별도 전수 확인한 것은 아닙니다.

## 공식 다운로드 링크

- 최신 GitHub 릴리즈: https://github.com/munument1/Fallout2-RPU-KR/releases/tag/v2.4.34-native.1
- 권장 통합판: https://github.com/munument1/Fallout2-RPU-KR/releases/download/v2.4.34-native.1/RPU-KR-v2.4.34-with-HRP-fix.zip
- 번역 데이터 전용: https://github.com/munument1/Fallout2-RPU-KR/releases/download/v2.4.34-native.1/korean-classic-data.zip
- 수정/제보 기록: https://github.com/munument1/Fallout2-RPU-KR/issues/4

---

이 파일은 **넥서스에 아직 직접 게시되지 않은 준비 문안**입니다. GitHub 업로드 파일 자체는 이미 공식 릴리즈 자산으로 생성·검증되었습니다.
