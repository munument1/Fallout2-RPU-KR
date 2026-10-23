# RPU 한국어 번역 — v2.4.34-native.2

**공식 RPU 2.4.34용 한국어 번역 및 글자 잘림 수정 통합 패키지**

[**정식 릴리즈 및 다운로드**](https://github.com/munument1/Fallout2-RPU-KR/releases/tag/v2.4.34-native.2)

## 이번 업데이트 (2026-10-23)

- 도입부·장로·꿈·유조선 영상용 SVE 자막 24개 복원 및 배포 누락 수정.
- 인종·외형 설명 잘림은 한국어 텍스트 엔진 v1.2.4에서 별도로 수정(공식 sfall 4.5.1).
- 엔딩 동영상의 영어로 남은 자막 34종 번역 (`cuts` / `cuts_female`).
- 하단 메시지 기록창에서 긴 한글 오른쪽이 잘리는 오류 수정.
- 공식 RPU 2.4.34의 `f2_res.dll`이 기존 레저렉션 KR1.2에서 수정한 DLL 원본과 **SHA-256까지 동일**함을 확인한 뒤, 해당 CP949 픽셀 폭 기준 줄바꿈 코드를 동일하게 적용.
- 원본 DLL 해시, 수정 코드 진입점, ZIP 무결성, 자막 파일을 GitHub Actions에서 검증함.

## 다운로드 파일

- **[RPU-KR-v2.4.34-with-HRP-fix.zip](https://github.com/munument1/Fallout2-RPU-KR/releases/download/v2.4.34-native.2/RPU-KR-v2.4.34-with-HRP-fix.zip)** — 공식 RPU 2.4.34용 번역+글자 잘림 통합 패키지(권장)
- [korean-classic-data.zip](https://github.com/munument1/Fallout2-RPU-KR/releases/download/v2.4.34-native.2/korean-classic-data.zip) — 번역만 적용하는 패키지. HRP DLL 변경 없음
- [한국어 텍스트 엔진 v1.2.4](https://github.com/munument1/Fallout2-Korean-Text-Engine/releases/tag/v1.2.4) — 한글 출력 설치기

## 설치 방법

1. **공식 RPU 2.4.34가 설치된 Fallout 2 게임 폴더**를 백업하세요. 특히 `f2_res.dll` 원본을 보관하세요.
2. RPU 2.4.34에 다른 모드가 교체한 `f2_res.dll`이 없다면 권장 통합 ZIP을 `fallout2.exe`가 있는 폴더에 압축 해제하고 덮어씁니다.
3. 독립형 Korean Text Engine **v1.2.4** 설치기로 같은 폴더에 한글 출력을 적용합니다. 기존 엔진 설치본의 업그레이드는 해당 엔진 안내에 따라 복구 후 재설치합니다.
4. 기존 Fallout 2 / RPU 실행기로 게임을 시작합니다.

**중요:** 통합 ZIP의 수정된 `f2_res.dll`은 **공식 RPU 2.4.34** 전용입니다. 최신 HRP, 다른 모드팩, 자체 수정 DLL에는 호환성을 보장하지 않습니다. 그 경우에는 번역 전용 ZIP을 사용하세요.

게임 EXE와 기존 sfall `ddraw.dll`은 배포 ZIP에서 교체하지 않습니다.

## 검증 현황

GitHub Actions에서 공식 HRP 원본 SHA-256 및 수정된 함수 2곳을 검사했고, 자막 254개 파일과 번역 ZIP 테스트를 통과했습니다.

레저렉션 KR1.2에서는 같은 원본 DLL을 사용한 수정의 인게임 검증이 있었지만, **RPU 자체의 모든 플레이 환경에서 글자 잘림이 없어졌다고 전수 검증한 것은 아닙니다.** 재현되면 [이슈 #4](https://github.com/munument1/Fallout2-RPU-KR/issues/4)에 알려주세요.

[릴리즈 노트](docs/RELEASE_NOTES_V2_4_34_NATIVE_2.md) · [세부 검증 기록](docs/ISSUE_4_SUBTITLE_AND_CLIPPING_QA.md) · [이전 설치 안내](docs/LEGACY_INSTALLATION_KO.md)

이 저장소는 원본 게임·RPU의 변경되지 않은 바이너리나 sfall DLL을 배포하지 않습니다. 한글 출력 엔진은 별도의 [Fallout2-Korean-Text-Engine](https://github.com/munument1/Fallout2-Korean-Text-Engine)에서 관리합니다.
