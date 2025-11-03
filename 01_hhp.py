import streamlit as st
import pandas as pd
import folium
from folium.plugins import MarkerCluster
from streamlit.components.v1 import html
from math import radians, cos, sin, asin, sqrt

st.set_page_config(page_title="서울 임산부 응급병원 찾기", layout="wide")

st.title("🤰 서울시 임산부 응급실 위치 지도")
st.caption("CSV 파일에서 병원 위치와 운영시간을 불러와 지도에 표시합니다. 마우스 오버 시 운영시간이 표시됩니다.")

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

# 경로: 사용자가 업로드했거나 내부에 있는 파일 경로를 기본으로 둡니다.
DEFAULT_CSV = '/mnt/data/서울시 응급실 위치 정보 (1).csv'

uploaded = st.file_uploader("CSV 파일 업로드 (기본값 사용 가능)", type=['csv'])
if uploaded is None:
    try:
        df = load_data(DEFAULT_CSV)
    except Exception as e:
        st.error(f"기본 CSV를 불러오는 데 실패했습니다: {e}")
        st.stop()
else:
    df = pd.read_csv(uploaded)

st.write("데이터 미리보기:")
st.dataframe(df.head())

# 컬럼 이름 유연하게 찾기
def find_column(df, candidates):
    for c in candidates:
        for col in df.columns:
            if c.lower() in col.lower():
                return col
    return None

lat_col = find_column(df, ['위도', 'latitude', 'lat', 'y'])
lon_col = find_column(df, ['경도', 'longitude', 'lng', 'lon', 'x'])
name_col = find_column(df, ['병원', '이름', 'name'])
open_col = find_column(df, ['운영', '시간', '영업', '진료', '평일'])
region_col = find_column(df, ['구', '지역', '읍', '동'])

if not lat_col or not lon_col or not name_col:
    st.error('CSV에 위도, 경도, 병원명 컬럼이 확인되지 않습니다. 컬럼명을 확인해주세요.')
    st.stop()

# 소수로 변환
df[lat_col] = pd.to_numeric(df[lat_col], errors='coerce')
df[lon_col] = pd.to_numeric(df[lon_col], errors='coerce')

def haversine(lat1, lon1, lat2, lon2):
    # 모든 파라미터는 소수
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km

st.sidebar.header("검색 및 필터")
use_location = st.sidebar.checkbox("내 위치 사용 (브라우저에서 좌표 복사 필요)")

st.sidebar.markdown("**현재위치 얻기 도움말**: '브라우저 위치 얻기' 버튼을 눌러 좌표를 복사한 뒤 아래에 붙여넣기 하세요. 배포 환경에 따라 자동 전송이 불가능할 수 있습니다.")
if st.sidebar.button("브라우저에서 내 위치 얻기 (팝업 열기)"):
    # 간단한 JS UI를 띄워 사용자가 브라우저에서 좌표를 복사할 수 있게 함
    js = '''
    <div style="font-family:Arial; padding:10px;">
    <h3>브라우저 위치 얻기</h3>
    <p>허용을 누르면 좌표가 화면에 표시됩니다. 복사해서 스트림릿 좌표 입력란에 붙여넣으세요.</p>
    <button onclick="getLocation()">허용하고 좌표 표시</button>
    <pre id="coords" style="background:#f0f0f0;padding:10px;margin-top:10px;"></pre>
    <script>
    function getLocation(){
        if (!navigator.geolocation){
            document.getElementById('coords').innerText = '이 브라우저는 Geolocation을 지원하지 않습니다.';
            return;
        }
        navigator.geolocation.getCurrentPosition(function(pos){
            var s = '위도(lat): ' + pos.coords.latitude + '\n경도(lon): ' + pos.coords.longitude + '\n정확도(m): ' + pos.coords.accuracy;
            document.getElementById('coords').innerText = s;
        }, function(err){
            document.getElementById('coords').innerText = '위치 정보를 얻을 수 없습니다. ('+err.message+')';
        });
    }
    </script>
    '''
    html(js, height=250)

lat_input = st.sidebar.text_input('내 위도(lat) 입력', '')
lon_input = st.sidebar.text_input('내 경도(lon) 입력', '')

# 지역 선택
regions = None
if region_col:
    regions = sorted(df[region_col].dropna().unique())
    region_choice = st.sidebar.selectbox('지역(구) 선택', options=['전체'] + regions)
else:
    region_choice = '전체'

# 필터 적용
filtered = df.copy()
if region_choice != '전체' and region_col:
    filtered = filtered[filtered[region_col] == region_choice]

# 기본 지도 중심: 서울 중심 좌표
seoul_center = (37.5665, 126.9780)

# 지도 생성
m = folium.Map(location=seoul_center, zoom_start=11)
marker_cluster = MarkerCluster().add_to(m)

for _, row in filtered.dropna(subset=[lat_col, lon_col]).iterrows():
    name = row[name_col]
    lat = row[lat_col]
    lon = row[lon_col]
    hours = row[open_col] if open_col else '운영시간 정보 없음'
    tooltip = f"{name} — {hours}"
    popup_html = f"<b>{name}</b><br>{hours}<br>위도: {lat}, 경도: {lon}"
    folium.Marker(location=(lat, lon), tooltip=tooltip, popup=popup_html).add_to(marker_cluster)

# 지도 출력
st.subheader('서울시 병원 지도 (호버: 운영시간 표시)')
map_html = m._repr_html_()
html(map_html, height=600)

# 사용자 위치로부터 거리 계산 및 추천
user_has_coords = False
user_lat = None
user_lon = None
if lat_input and lon_input:
    try:
        user_lat = float(lat_input.strip())
        user_lon = float(lon_input.strip())
        user_has_coords = True
    except:
        st.sidebar.error('좌표 형식을 확인하세요. 예: 37.5665')

st.sidebar.markdown('---')
if user_has_coords:
    st.sidebar.success('사용자 좌표가 설정되었습니다.')
    # 거리 계산
    filtered = filtered.copy()
    filtered['distance_km'] = filtered.apply(lambda r: haversine(user_lat, user_lon, r[lat_col], r[lon_col]), axis=1)
    nearest = filtered.sort_values('distance_km').reset_index(drop=True)
    st.subheader('내 위치 기준 가까운 병원 추천')
    st.write(f'사용자 위치: 위도 {user_lat}, 경도 {user_lon}')
    st.dataframe(nearest[[name_col, lat_col, lon_col, 'distance_km']].rename(columns={name_col:'병원명',lat_col:'위도',lon_col:'경도', 'distance_km':'거리(km)'}).head(10))
else:
    st.info('좌표를 입력하면 내 위치 기준으로 가까운 병원을 추천합니다. 또는 지역을 선택하세요.')

st.markdown('---')
st.caption('앱 사용 팁: 브라우저에서 좌표 얻기 버튼을 눌러 위도/경도를 복사한 뒤 사이드바에 붙여넣으세요. 배포 환경(예: Streamlit Cloud)에서는 브라우저의 위치 권한 동작이 다를 수 있습니다.')
