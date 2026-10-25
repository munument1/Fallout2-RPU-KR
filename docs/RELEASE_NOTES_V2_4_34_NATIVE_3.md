# RPU 한국어 v2.4.34-native.3 (도입부 영상 자막 추가)

## 수정 사항

- **게임 도입부 영상의 한국어 자막 누락 수정**: 공식 RPU v2.4.34의 `data/text/english/cuts/intro.sve` 17개 타임코드를 기준으로 한국어 `intro.sve`를 번역해 추가했습니다.
- `data/text/korean/cuts/intro.sve` 및 `data/text/korean/cuts_female/intro.sve`를 모두 배포합니다. 기존 `ovrintro.sve`와는 다른 영상입니다.
- 한국어 영화 자막 총 **26개**(각 성별 폴더 13개)를 CP949로 인코딩하여 배포합니다. 필수 파일 목록과 ZIP 무결성 테스트에도 `intro.sve` 두 파일을 추가해 동일 누락 재발을 방지합니다.
- 기존 v2.4.34-native.2의 자막 번역, 공식 RPU 2.4.34 전용 HRP 기록창 글자 잘림 수정 등은 유지합니다.

## 설치 안내

- 공식 RPU **2.4.34** 설치 환경에서 기존 한국어판을 백업한 뒤 `RPU-KR-v2.4.34-with-HRP-fix.zip`을 `fallout2.exe`가 있는 폴더에 풀어 덮어쓰세요. `f2_res.dll`은 반드시 원본을 백업하세요.
- 다른 HRP/모드팩 또는 별도 수정 DLL을 사용한다면 HRP를 변경하지 않는 `korean-classic-data.zip`만 설치하세요.
- 한국어 출력에는 [독립형 Korean Text Engine v1.2.4](https://github.com/munument1/Fallout2-Korean-Text-Engine/releases/tag/v1.2.4)를 사용하세요. 기존 엔진에서 업그레이드하려면 해당 설치기 지침에 따라 복구 후 재설치하세요.

## 검증

- 영어 RPU 2.4.34 `intro.sve`와 번역본의 17개 영상 프레임 번호 일치, 두 성별 번역 내용 일치, 빈 자막 프레임 보존, 한국어/CP949 변환 검증.
- 릴리스 자동화는 자막 포함 여부와 ZIP 내부 매니페스트 해시, 기존 엔딩 자막 회귀 및 HRP 원본 해시/패치 구조를 검사한 다음 배포합니다.
- **실제 게임에서 도입부 영상을 끝까지 재생하며 자막을 눈으로 확인하는 인게임 검증은 별도로 필요합니다.**

제보: https://github.com/munument1/Fallout2-RPU-KR/issues/4#issuecomment-6399699726
