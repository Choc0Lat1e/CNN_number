# Matplotlib 가이드북 (한눈에 보는 요약 + 예제)

간단 소개
- Matplotlib은 Python에서 가장 널리 쓰이는 2D 시각화 라이브러리입니다.
- 과학/공학/데이터 분석에서 그래프(선형, 산점도, 히스토그램 등)를 만들고 커스터마이즈할 때 주로 사용합니다.
- 고수준의 pyplot 인터페이스와 저수준의 Figure/Axes/Artist API를 모두 제공하여 빠른 시각화와 세밀한 제어가 가능합니다.

설치
```bash
# 일반 설치
pip install matplotlib

# Jupyter/Colab에서 권장 (특정 백엔드)
pip install matplotlib notebook
```

빠른 시작 예제
```python
import matplotlib.pyplot as plt
x = [0, 1, 2, 3]
y = [0, 1, 4, 9]
plt.plot(x, y, marker='o', color='tab:blue', linewidth=2)
plt.title("간단한 선 그래프")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()
```

핵심 개념(요약 표)

| 개념 | 설명 | 주로 사용하는 함수/속성 |
|---|---:|---|
| pyplot | MATLAB 스타일의 상태 기반 API — 빠르게 그릴 때 사용 | plt.plot, plt.scatter, plt.show |
| Figure | 전체 그림(캔버스) 객체 — 여러 Axes를 포함 | plt.figure(), fig.savefig() |
| Axes | 실제 데이터가 그려지는 좌표계(하나의 그래프 영역) | fig.add_subplot(), ax.plot(), ax.set_title() |
| Artist | Matplotlib 내 모든 그려지는 요소(텍스트, 선, 패치 등) | Text, Line2D, Patch 등 |
| rcParams | 전역 스타일/설정(폰트, 폰트크기, DPI 등) | plt.rcParams['font.size']=12 |

주요 플롯 타입(요약 표)

| 플롯 타입 | 설명 | 함수 | 간단 예시 |
|---|---:|---:|---|
| 선 그래프 | 연속값 데이터 추세 표현 | plt.plot | plt.plot(x,y) |
| 산점도 | 점으로 분포/관계 표현 | plt.scatter | plt.scatter(x,y) |
| 막대 그래프 | 범주형 데이터 비교 | plt.bar / plt.barh | plt.bar(categories, values) |
| 히스토그램 | 분포(빈도) 표시 | plt.hist | plt.hist(data, bins=30) |
| 박스플롯 | 분포의 요약(사분위) | plt.boxplot | plt.boxplot(data) |
| 파이 차트 | 비율 표현(권장 상황 제한적) | plt.pie | plt.pie(sizes, labels=...) |
| 등고선/이미지 | 2차원 스칼라 필드 시각화 | plt.contour, plt.imshow | plt.imshow(matrix, cmap='viridis') |
| 히트맵 | 행렬 형태 데이터 컬러맵 | sns.heatmap 또는 plt.imshow | sns.heatmap(df) |

자주 사용하는 스타일/옵션(요약 표)

| 목적 | 옵션/인자 | 예 |
|---|---:|---|
| 색상 | color='red' 또는 'tab:blue' 또는 cmap | plt.plot(x,y,color='C1') |
| 선 스타일 | linestyle='--', linewidth=2 | plt.plot(x,y,linestyle=':',linewidth=1.5) |
| 마커 | marker='o', markersize=6 | plt.plot(x,y,marker='s') |
| 축 라벨 | ax.set_xlabel / plt.xlabel | ax.set_ylabel("값") |
| 범례 | plt.legend(loc='best') | plt.plot(..., label='A'); plt.legend() |
| 그리드 | plt.grid(True) | plt.grid(ls='--', alpha=0.6) |
| 글꼴/크기 | plt.rcParams['font.size'] = 12 | plt.title(..., fontsize=14) |

Figure / Subplot 다루기 (예제)
```python
import matplotlib.pyplot as plt
fig, axes = plt.subplots(2, 2, figsize=(8,6))
axes[0,0].plot(x, y); axes[0,0].set_title('subplot 1')
axes[0,1].scatter(x, y); axes[0,1].set_title('subplot 2')
axes[1,0].hist(data); axes[1,0].set_title('hist')
axes[1,1].axis('off')  # 사용 안함
plt.tight_layout()
plt.show()
```

애노테이션과 텍스트
- ax.text(x, y, "라벨") — 좌표에 텍스트 추가
- ax.annotate("이벤트", xy=(x,y), xytext=(x+0.5,y+0.5), arrowprops=dict(...))

색상 지도(cmap)와 컬러바
```python
plt.imshow(matrix, cmap='viridis')
plt.colorbar()
```
자주 쓰는 cmap: 'viridis', 'plasma', 'inferno', 'magma', 'coolwarm', 'RdYlBu'

그래프 저장
```python
fig.savefig("plot.png", dpi=300, bbox_inches='tight', transparent=False)
# PDF/SVG 벡터 형식도 가능: .pdf, .svg
```

인터랙티브 모드 & 노트북
- Jupyter 노트북: %matplotlib inline (정적), %matplotlib notebook 또는 %matplotlib widget (인터랙티브)
- Matplotlib 백엔드에 따라 화면 표시와 상호작용 방법이 달라짐

스타일과 테마
- plt.style.use('seaborn') 또는 'ggplot', 'bmh', 'fast' 등
- 사용자 스타일을 rcParams로 설정하거나 matplotlib 스타일 파일(.mplstyle) 사용 가능

고급: 저수준 API
- Figure, Axes 객체를 직접 제어하면 축 단위로 더 세밀한 조절 가능
- 예: twin axes (ax.twinx()), inset_axes, transforms, custom Artists

성능 팁
- 많은 점(scatter로 수십만 개)을 그릴 때는 alpha, point size 최적화, 혹은 Datashader 같은 도구 사용 권장
- 반복적으로 업데이트해야 하는 애니메이션은 matplotlib.animation 또는 interactive 백엔드 사용

자주 겪는 문제와 해결
- 한글 깨짐: plt.rcParams['font.family'] = 'NanumGothic' 등 폰트 설정, 혹은 시스템에 폰트 설치 필요
- 축 레이블 잘림: plt.tight_layout() 사용
- 레전드가 데이터와 겹침: bbox_to_anchor 또는 loc 인자 조정
- 컬러맵 해석 문제: 연속값용과 범주형용 cmap 구분

참고 코드 모음(자주 쓰는 예제)
```python
# 선 + 마커 + 범례
plt.plot(x, y1, label='A', color='C0', marker='o')
plt.plot(x, y2, label='B', color='C1', linestyle='--')
plt.legend()

# 산점도에 회귀선 (numpy 사용)
import numpy as np
m, b = np.polyfit(x, y, 1)
plt.scatter(x, y)
plt.plot(x, m*np.array(x)+b, color='red')
```

비교: Matplotlib vs Seaborn vs Plotly (간단 표)

| 라이브러리 | 장점 | 용도 |
|---|---:|---|
| Matplotlib | 세밀한 제어, 범용성, 출판용 그래프 | 모든 기본 시각화, 커스터마이징 |
| Seaborn | 통계적 시각화, 미려한 기본 스타일 | 통계 플롯(히트맵, 카테고리), 빠른 미려한 출력 |
| Plotly | 인터랙티브, 웹에 쉽게 통합 | 대화형 대시보드, 웹 공유 |

추가 학습/레퍼런스
- 공식 문서: https://matplotlib.org/
- 튜토리얼: Matplotlib gallery (공식) — 다양한 예제 코드 포함
- 관련: Seaborn (통계 시각화), Plotly (인터랙티브)

요약(한 문장)
- Matplotlib은 Python에서 그래프를 직접 그리고 세밀하게 조정할 수 있게 해주는 핵심 라이브러리이며, 빠른 프로토타이핑부터 출판 품질의 시각화까지 폭넓게 사용됩니다.
