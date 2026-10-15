# 이전 설치 안내 — 참고용

아래는 새 출력 엔진 전환 이전의 문서다. 현재 설치 방법으로 사용하지 않는다. 이전 릴리스와 이력을 설명하기 위해 보존한다.

# 폴아웃 2 복원 프로젝트 (Fallout 2 Restoration Project - RPU) 한국어 패치

> [!IMPORTANT]
> **한국어 번역 리소스 전용 저장소 안내**
> - 본 저장소는 오리지널 모드(`Fallout2_Restoration_Project`)의 전체 소스 코드를 포함하지 않으며, **한국어 번역 리소스 파일만 업로드하여 관리 및 배포하는 독립 저장소**입니다.
> - 모드를 사용하기 위해서는 반드시 원본 모드가 먼저 설치되어 있어야 합니다. 원본 모드는 아래 링크를 통해 다운로드해 주세요.
> - 원본 모드 프로젝트: [BGforgeNet/Fallout2_Restoration_Project](https://github.com/BGforgeNet/Fallout2_Restoration_Project)
> - 
> - 
> - [CREDIT]
> - 정글생선
> - PT-76
> - 다음 제작자 분들의 번역을 이어 진행했습니다.

---

## 원본 프로젝트 설명 (Fallout 2 Restoration Project, updated)

이 모드는 폴아웃 2를 위한 [killap의 Restoration Project](http://killap.net/)를 기반으로 최신 환경에 맞게 개선 및 업데이트된 버전입니다.

[**최신 버전 다운로드**](https://github.com/BGforgeNet/Fallout2_Restoration_Project/releases/latest)
| [**설치 가이드**](#설치-가이드)
| [**버그 제보**](#버그-제보-및-기능-제안)
| [**다국어 지원 정보**](docs/translations.md)
| [**번역 지침 가이드**](docs/translation_guidelines.md)
| [**추가 모드**](#추가-모드-목록)

---

### 설치 가이드

- RPU는 아무런 모드도 설치되지 않은 순정(Vanilla) 게임 상태에서 설치해야 합니다.
- 설치를 마친 후에는 반드시 **새 게임**을 시작해야 정상적으로 적용됩니다. (기존 RPU 혹은 이전 RPU 버전에서 [업데이트](docs/update.md)하는 경우는 제외)

#### Windows 환경
1. [최신 릴리즈 페이지](https://github.com/BGforgeNet/Fallout2_Restoration_Project/releases/latest)에서 `rpu_v*.exe` 파일을 다운로드합니다.
2. 실행 후 설치 프로그램의 대상 경로를 폴아웃 2 게임 디렉토리로 지정하고, 원하는 언어 및 옵션을 선택하여 설치를 진행합니다.
3. 설치 완료 후 `mods/upu.ini` 및 `mods/rpu.ini` 파일을 메모장 등으로 열어 다양한 편의성 옵션을 상세하게 구성할 수 있습니다.
4. 더 풍부한 경험을 원하시면 아래의 [권장 추가 모드](#권장-추가-모드)들을 확인해 보세요.

#### 한국어 패치 적용
1. 이 저장소의 **Releases** 페이지에서 최신 한국어 패치를 다운로드합니다.
2. 압축 파일의 내용을 RPU가 설치된 Fallout 2 게임 디렉터리에 복사합니다.
3. 배포물에는 한글 Sfall `ddraw.dll`, `LangFont.ini`, `fonts` 폴더가 포함되어 있습니다.
4. 설치본마다 설정이 다르므로 `fallout2.cfg` 전체를 교체하지 마십시오. 기존 파일의 `[system]` 섹션에서 `language` 값만 다음처럼 변경합니다.

   ```ini
   [system]
   language=korean
   ```

이미 `language=` 줄이 있다면 새 줄을 추가하지 말고 기존 값만 변경합니다. 기존 `ddraw.ini`, `sfall.dat`와 CFG의 다른 설정은 유지하십시오.

#### Linux / MacOS 환경
- 다음 [안내 문서](docs/linux.md)를 참조해 주세요.

---

### 추가 모드 목록

#### 모드 기본 포함 내역
본 RPU 패키지에는 다음 모드들이 기본적으로 포함되어 있습니다:
- [비공식 패치 (Unofficial Patch)](https://github.com/BGforgeNet/Fallout2_Unofficial_Patch)
- [고음질 오디오 (High quality music)](https://github.com/BGforgeNet/Fallout2-HQ-music)
- [주인공 외형 선택 모드 (Hero Appearance)](https://github.com/BGforgeNet/Fallout2_Hero_Appearance)
- [동료 아머 외형 반영 (NPC armor)](https://github.com/BGforgeNet/Fallout2_NPC_Armor)
- [동료 명령 단축키 (Party Orders)](https://github.com/BGforgeNet/Fallout2_Party_Orders)
- [캐시디 말하는 머리 추가 (Cassidy talking head)](https://github.com/BGforgeNet/Fallout2_Cassidy_Head)
- 개선된 월드맵 (Enhanced worldmap)
- [화염방사기 연출 모션 추가 (Extended Flamer animations)](https://www.nma-fallout.com/threads/the-extended-flamer-attack-mod.192732/)
- 추가 소총 및 와키자시 모션 추가
- 개선된 신비로운 낯선 사람 (Improved Mysterious Stranger)
- 고해상도 패치 (High resolution patch)

#### 권장 추가 모드
보다 쾌적한 게임플레이(QoL)를 위해 다음 모드들을 추가로 확인해 보시는 것을 권장합니다:
- [무손실 음원 패치 (Lossless music)](https://github.com/BGforgeNet/Fallout2-HQ-music)
- [FO2tweaks (각종 세부 편의성 설정)](https://github.com/BGforgeNet/FO2tweaks)
- [인벤토리 필터 (Inventory Filter)](https://github.com/rotators/InventoryFilter)

---

### 버그 제보 및 기능 제안

1. [GitHub Issues 페이지](https://github.com/BGforgeNet/Fallout2_Restoration_Project/issues) 또는 [BGforge 포럼](https://forums.bgforge.net/viewforum.php?f=39)을 방문해 주세요.
2. 새로운 이슈/글을 등록하고 버그에 대해 자세히 설명합니다. (각 버그는 서로 별개의 글로 작성해야 합니다.)
3. 버그가 발생하는 상황의 **세이브 파일**과 **스크린샷**을 반드시 첨부해 주세요.

---

### 추가 참조 링크
- [변경 이력 (Changelog)](docs/changelog.md)
- [RPU 추가 콘텐츠 설명 (스포일러 포함)](docs/rp-new_content.md)
- [RPU 전체 공략 가이드 (강한 스포일러 포함)](https://f2rp.bgforge.net/)
- [알려진 문제점 목록 (Known issues)](docs/known.md)
- [크래시/팅김 현상 제보 방법](https://github.com/BGforgeNet/Fallout2_Unofficial_Patch/blob/master/docs/crash.md)
- [기여자 정보 (Credits)](docs/credits.md)
- (한글호환패치 [소스코드](https://github.com/munument1/-KR-SFall-Unofficial-Translation))
