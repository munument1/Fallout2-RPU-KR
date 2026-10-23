# RPU Version 35 개발판 대응 검토 — 2026-10-23

## 버전 및 출고 기준

- 공식 원본: https://github.com/BGforgeNet/Fallout2_Restoration_Project
- 최신 확인 정식 릴리스: [v2.4.34](https://github.com/BGforgeNet/Fallout2_Restoration_Project/releases/tag/v2.4.34) (2025-10-18 UTC).
- 검토한 개발 HEAD: [394b507435ea15af7c097c95a5209248110ffce1](https://github.com/BGforgeNet/Fallout2_Restoration_Project/commit/394b507435ea15af7c097c95a5209248110ffce1), 커밋 메시지 `Changelog: version 35`.
- 한국어 정식 패치: `v2.4.34-native.1`. 이 작업 브랜치는 배포용 패치를 수정하지 않는다.

## 원본 변경 검토 결과

공식 GitHub compare `v2.4.34...master`는 `diverged`, 개발 HEAD 쪽 992개 커밋으로 보고한다. 이는 버전 35의 정식 출시나 992개 번역 변경을 뜻하지 않는다. 비교 결과가 300개 파일로 잘려 있어 전체 변경 목록이라고 간주하지 않는다.

비교 결과에서 **영문 게임 표시 문자열 변경**이 실제 확인된 파일:

- `data/text/english/dialog/containr.msg` (10행 추가/13행 삭제)
- `data/text/english/dialog/dcrebdor.msg` (1/1)
- `data/text/english/dialog/dcrebecc.msg` (8행 추가)
- `data/text/english/credits.txt` (1/1)

**게임 데이터 및 호환성 관련**으로 확인된 파일:

- `data/data/city.txt`, `data/data/maps.txt`, `data/data/worldmap.txt`
- `data/maps/epamain1.map`, `data/maps/epamain2.map`, `data/maps/sftanker.map` 등 지도 바이너리
- `data/maps/gecksetl.map.json` 신규 파일
- `.github/workflows/build.yml` 빌드 변경

## 실제 업데이트 작업 기준

1. `data/text/english/` 변경 파일을 한국어 MSG의 **ID 및 영어 원문**과 대조하고 변경된 줄만 번역한다. 기존 한국어 MSG를 영문으로 덮어쓰지 않는다.
2. `data/data/`, 지도, SSL/스크립트 변경이 퀘스트·대화·저장 호환성에 미치는 영향을 확인한다. 신규 레코드가 있으면 기존 번역 및 키 보존 검사를 추가한다.
3. 한국어 텍스트 엔진과 `f2_res.dll` 수정은 **공식 새 빌드의 정확한 원본 해시·구조**를 확인한 후 별도로 검증한다. v2.4.34용 패치의 해시 검사를 우회하지 않는다.
4. 번역 빌드·placeholder·파일 인코딩·패키지 검사를 통과하고, 개발판 대상 게임 실행 검증을 수행한 뒤에만 Version 35 지원을 선언한다.

**현재 상태:** 원본 변경 영향 분석 착수. 이 문서는 번역 수정, 바이너리 호환성 확인 또는 Version 35 정식 지원 완료를 뜻하지 않는다.
