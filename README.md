# PDF 합치기 프로그램

여러 PDF 파일을 쉽게 병합할 수 있는 사용자 친화적인 애플리케이션입니다.

## 주요 기능

- 여러 PDF 파일 병합
- 직관적인 그래픽 사용자 인터페이스
- 파일 목록 관리 (추가, 제거, 순서 변경)
- 병합 진행 상황 시각화

## 설치 방법

### 필요 조건

- Python 3.6 이상
- PyPDF2 라이브러리

### pip를 이용한 설치

```bash
pip install pdf-merger
```

### 소스에서 설치

```bash
git clone https://github.com/reinhardt0926/pdf_merger.git
cd pdf_merger
pip install -e .
```

## 사용 방법

### 애플리케이션 실행

```bash
pdf_merger
```

또는 소스 코드에서 직접 실행:

```bash
python -m src.main
```

### 사용 예시

1. "PDF 파일 추가" 버튼을 클릭하여 병합할 PDF 파일을 선택합니다.
2. 필요한 경우 목록에서 파일을 선택하고 위/아래 버튼을 사용하여 순서를 변경합니다.
3. "PDF 병합하기" 버튼을 클릭하여 병합 프로세스를 시작합니다.
4. 저장할 위치와 파일 이름을 지정합니다.
5. 병합이 완료되면 성공 메시지가 표시됩니다.

## 배포용 실행 파일 만들기

### PyInstaller를 이용한 실행 파일 생성

```bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=resources/icons/pdf_img.ico --add-data "resources;resources" src/main.py
```

생성된 실행 파일은 `dist` 폴더에서 찾을 수 있습니다.

## 라이선스

이 프로젝트는 MIT 라이선스에 따라 배포됩니다. 자세한 내용은 [LICENSE](LICENSE) 파일을 참조하십시오.

