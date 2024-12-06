// 위에서 제공한 Kakao 지도 관련 스크립트


let polygons = [];
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
    if (isMouseOver) return;
    isMouseOver = true;

    polygon.setOptions({ fillColor: '#73f57a' });
    document.getElementById('descriptionText').innerHTML = area.name;
    var img = document.createElement('img');
    img.src = '/static/images/서울.jpg'; // 이미지 경로 설정
    img.alt = '설명 텍스트'; // 대체 텍스트 추가

    // 이미지를 지정된 div에 추가
    document.getElementById('main_info_image').appendChild(img);

    // Timeout을 사용해 오버레이 깜빡임 방지
    if (overlayTimeout) clearTimeout(overlayTimeout);

   // customOverlay.setContent('<div class="area">' + area.name + '</div>');
   // customOverlay.setPosition(mouseEvent.latLng);
   // customOverlay.setMap(map);
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
      //  customOverlay.setMap(null);
        isMouseOver = false;
    }, 50); // 100ms 딜레이
});

kakao.maps.event.addListener(polygon, 'click', function () { // 마우스로 클릭했을 때
    console.log('Clicked region:', area.name);
    polygon.setOptions({ fillColor: '#21d12b' });

return polygon;
});
}