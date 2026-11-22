# .github

Mitdol Labs(밑돌랩스) 조직의 공개 저장소입니다. 조직 첫 화면(https://github.com/MitdolLabs)에 보이는 소개 글을 담습니다.

| 파일 | 무엇 |
| --- | --- |
| `profile/README.md` | 조직 첫 화면에 그대로 보이는 소개 글 |
| `profile/banner-light.svg`, `profile/banner-dark.svg` | 소개 글 맨 위의 배너. 지금은 테마와 관계없이 라이트 배너만 보여 줍니다(2026-11-22). 다크 배너는 파일만 만들어 둡니다 |
| `profile/make_banner.py` | 배너 두 장을 만드는 스크립트 |

- 배포는 없습니다. `main`에 올리면 조직 첫 화면에 바로 반영됩니다.
- 배너는 회사 홈페이지(https://mitdollabs.com) 첫 화면과 같은 그림(쌓은 돌 맨 위의 밑돌이, 먹색 한 가지)에 배경(산, 구름, 해·달, 풀)을 옅게 깐 것입니다. `profile/make_banner.py <profile 폴더>`로 다시 만듭니다. 밑돌이의 모양은 비공개 저장소 `brand`의 `character/mitdori.svg`가 기준입니다.
- 소개 글의 문장은 홈페이지 첫 화면과 같게 둡니다. 한쪽을 바꾸면 다른 쪽도 바꿉니다.
- 배너 안에는 글자를 넣지 않습니다. GitHub는 SVG를 그림으로 보여 주므로 글꼴이 보는 사람 기기에 따라 달라집니다. 제목과 문장은 `profile/README.md`에 둡니다.
- 이 저장소는 공개입니다. 비밀값·개인정보·출시 전 내부 정보는 넣지 않습니다.
