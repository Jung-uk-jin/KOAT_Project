import { images } from '/static/js/images.js';
let polygons = [];
let lastHoveredPolygon = null;  // 마지막으로 마우스가 올라갔던 폴리곤을 저장
init("/static/json/sido_2.json");

function removePolygon() {
    for (let i = 0; i < polygons.length; i++) {
        polygons[i].setMap(null);
    }
    polygons = [];
}

function init(path) {
    $.getJSON(path, function (geojson) {
        var units = geojson.features;

        $.each(units, function (index, unit) {
            var coordinates = unit.geometry.coordinates;
            var name = unit.properties.SIG_KOR_NM;

            var ob = new Object();
            ob.name = name;
            ob.path = [];

            $.each(coordinates[0], function (index, coordinate) {
                ob.path.push(new kakao.maps.LatLng(coordinate[1], coordinate[0]));
            });

            polygons.push(displayArea(ob));
        });
    });
}

function displayArea(area) {
    var polygon = new kakao.maps.Polygon({
        map: map,
        path: area.path,
        strokeWeight: 2,
        strokeColor: '#004c80',
        strokeOpacity: 1,
        fillColor: '#fff',
        fillOpacity: 1,
    });

    let isMouseOver = false;
    let overlayTimeout = null; // Timeout 관리용 변수

    kakao.maps.event.addListener(polygon, 'mouseover', function (mouseEvent) { // 마우스가 폴리곤 위로 올라갔을 때 
        // 마지막에 마우스가 올라갔던 폴리곤의 색을 원래대로 돌려놓기
        if (lastHoveredPolygon && lastHoveredPolygon !== polygon) {
            lastHoveredPolygon.setOptions({ fillColor: '#fff' }); // 원래 색으로 되돌리기
        }

        // 새로운 폴리곤에 색을 변경
        polygon.setOptions({ fillColor: '#73f57a' });

        // 마지막으로 마우스가 올라갔던 폴리곤을 업데이트
        lastHoveredPolygon = polygon;

        // 설명 텍스트 갱신
        document.getElementById('descriptionText').innerHTML = area.name;

        // 이미지 바로 갱신
        var imgContainer = document.getElementById('slider__img');//main_info_image
        imgContainer.innerHTML = '';  // 기존 이미지들 제거

        // 해당 지역에 맞는 이미지 설정
        var img = document.createElement('img');
        img.src = images[area.name] || '/static/images/default.jpg'; // 기본 이미지 경로 설정
        img.alt = area.name + ' 이미지';
        img.style.width = '400px'; // 이미지 크기 설정
        img.style.height = '300px'; // 이미지 크기 비율 유지

        // 이미지 바로 추가
        imgContainer.appendChild(img);

        // Timeout을 사용해 오버레이 깜빡임 방지
        if (overlayTimeout) clearTimeout(overlayTimeout);
    });

    kakao.maps.event.addListener(polygon, 'mousemove', function (mouseEvent) { // 마우스가 안에서 이동할 때 
        // 마우스가 이동할 때 오버레이 위치를 업데이트
        if (isMouseOver) {
            customOverlay.setPosition(mouseEvent.latLng);
        }
    });

    kakao.maps.event.addListener(polygon, 'mouseout', function () { // 마우스가 바깥으로 나갔을 때
        if (!isMouseOver) return;

        // 지연 시간을 두고 오버레이를 제거
        overlayTimeout = setTimeout(() => {
            polygon.setOptions({ fillColor: '#fff' });
            isMouseOver = false;
        }, 50); // 100ms 딜레이
    });

    kakao.maps.event.addListener(polygon, 'click', function () { // 마우스로 클릭했을 때
        console.log('Clicked region:', area.name);
        polygon.setOptions({ fillColor: '#21d12b' });
        // 지역 이름을 기반으로 이동할 URL 설정
        let regionPage = `/location/up/${encodeURIComponent(area.name)}`;

        // 해당 URL로 페이지 이동
         window.location.href = regionPage;
    });

    
    return polygon;
    
}