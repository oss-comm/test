# OSS Repository Check

`oss-repo-check`는 오픈소스 프로젝트에 처음 참여하는 사람이 저장소의 기본 기여 환경을 빠르게 확인할 수 있도록 만든 작은 Python CLI 도구입니다.

저장소 URL을 입력하면 다음 항목의 존재 여부를 확인합니다.

- README
- CONTRIBUTING 가이드
- Code of Conduct
- License
- Issue Template
- Pull Request Template

## 왜 만들었나요?

처음 오픈소스 프로젝트를 접하면 코드보다 먼저 프로젝트의 기여 규칙과 커뮤니티 문화를 이해해야 합니다. 이 프로젝트는 신규 기여자가 저장소의 온보딩 준비 상태를 빠르게 살펴보고, 어떤 문서를 먼저 읽어야 하는지 판단하는 데 도움을 주는 것을 목표로 합니다.

## 설치

```bash
python -m pip install -e .
```

## 사용법

```bash
oss-repo-check https://github.com/pallets/flask
```

또는 owner/repository 형식으로도 실행할 수 있습니다.

```bash
oss-repo-check pallets/flask
```

## 출력 예시

```text
Repository: pallets/flask
README                 OK
CONTRIBUTING            OK
CODE_OF_CONDUCT         OK
LICENSE                 OK
ISSUE_TEMPLATE          OK
PULL_REQUEST_TEMPLATE   MISSING

Score: 5/6
```

## 개발

```bash
python -m pip install -e .[dev]
pytest
```

## 첫 기여 아이디어

초보 기여자는 다음과 같은 작업부터 시작할 수 있습니다.

1. JSON 출력 옵션 추가
2. 검사 항목별 설명 메시지 개선
3. GitLab 저장소 지원
4. 네트워크 오류 메시지 개선
5. 테스트 케이스 추가

자세한 기여 절차는 [CONTRIBUTING.md](CONTRIBUTING.md)를 참고하세요.
