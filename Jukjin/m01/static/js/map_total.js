import { images } from '/static/js/images.js';

let polygons = [];
let lastHoveredPolygon = null;  // 마지막으로 마우스가 올라갔던 폴리곤을 저장
let currentIndex = 1;  // 현재 슬라이드 인덱스
const sliderWidth = 400;  // 슬라이드 이미지의 너비
const sliderHeight = 300;  // 슬라이드 이미지의 높이

const sliderInner = document.querySelector('.slider__inner');  // 슬라이드 내부
const sliderImg = document.querySelector('.slider__img');  // 이미지 컨테이너
const sliderBtnPrev = document.querySelector('.prev');  // 왼쪽 버튼
const sliderBtnNext = document.querySelector('.next');  // 오른쪽 버튼

// 슬라이드 생성
function generateSlider(images) {
    Object.keys(images).forEach((region) => {
        const sliderDiv = document.createElement('div');
        sliderDiv.classList.add('slider');

        const img = document.createElement('img');
        img.src = images[region];
        img.alt = region;

        sliderDiv.appendChild(img);
        sliderInner.appendChild(sliderDiv);
    });
}

// 슬라이드 초기화
function initSlider() {
    const sliders = document.querySelectorAll('.slider');
    const firstClone = sliders[0].cloneNode(true);
    const lastClone = sliders[sliders.length - 1].cloneNode(true);

    sliderInner.appendChild(firstClone);
    sliderInner.insertBefore(lastClone, sliders[0]);

    sliderInner.style.width = `${(sliders.length + 2) * sliderWidth}px`;
    sliderInner.style.transform = `translateX(-${sliderWidth * currentIndex}px)`;
}

// 슬라이드 이동
function gotoSlider(index) {
    const sliders = document.querySelectorAll('.slider');

    if (index >= sliders.length) {
        currentIndex = 1;
        sliderInner.style.transition = 'none';
        sliderInner.style.transform = `translateX(-${sliderWidth * currentIndex}px)`;
        setTimeout(() => {
            sliderInner.style.transition = 'all 400ms ease-in-out';
            currentIndex++;
            sliderInner.style.transform = `translateX(-${sliderWidth * currentIndex}px)`;
        }, 50);
    } else if (index < 0) {
        currentIndex = sliders.length - 2;
        sliderInner.style.transition = 'none';
        sliderInner.style.transform = `translateX(-${sliderWidth * currentIndex}px)`;
        setTimeout(() => {
            sliderInner.style.transition = 'all 400ms ease-in-out';
            currentIndex--;
            sliderInner.style.transform = `translateX(-${sliderWidth * currentIndex}px)`;
        }, 50);
    } else {
        sliderInner.style.transition = 'all 400ms ease-in-out';
        sliderInner.style.transform = `translateX(-${sliderWidth * index}px)`;
        currentIndex = index;
    }
}

// 왼쪽 버튼 클릭
sliderBtnPrev.addEventListener('click', () => {
    gotoSlider(currentIndex - 1);
});

// 오른쪽 버튼 클릭
sliderBtnNext.addEventListener('click', () => {
    gotoSlider(currentIndex + 1);
});

// 폴리곤을 생성하는 함수
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

// 폴리곤 표시 함수
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
    let overlayTimeout = null;  // Timeout 관리용 변수

    kakao.maps.event.addListener(polygon, 'mouseover', function (mouseEvent) {
        // 마지막에 마우스가 올라갔던 폴리곤의 색을 원래대로 돌려놓기
        if (lastHoveredPolygon && lastHoveredPolygon !== polygon) {
            lastHoveredPolygon.setOptions({ fillColor: '#fff' });
        }

        // 새로운 폴리곤에 색을 변경
        polygon.setOptions({ fillColor: '#73f57a' });

        // 마지막으로 마우스가 올라갔던 폴리곤을 업데이트
        lastHoveredPolygon = polygon;

        // 설명 텍스트 갱신
        document.getElementById('descriptionText').innerHTML = area.name;

        // 이미지 바로 갱신
        var imgContainer = document.getElementById('slider__img');
        imgContainer.innerHTML = '';  // 기존 이미지들 제거

        // 해당 지역에 맞는 이미지 설정
        var img = document.createElement('img');
        img.src = images[area.name] || '/static/images/default.jpg';  // 기본 이미지 경로 설정
        img.alt = area.name + ' 이미지';
        img.style.width = '400px';
        img.style.height = '300px';

        // 이미지 바로 추가
        imgContainer.appendChild(img);

        // Timeout을 사용해 오버레이 깜빡임 방지
        if (overlayTimeout) clearTimeout(overlayTimeout);
    });

    kakao.maps.event.addListener(polygon, 'mousemove', function (mouseEvent) {
        if (isMouseOver) {
            customOverlay.setPosition(mouseEvent.latLng);
        }
    });

    kakao.maps.event.addListener(polygon, 'mouseout', function () {
        if (!isMouseOver) return;

        // 지연 시간을 두고 오버레이를 제거
        overlayTimeout = setTimeout(() => {
            polygon.setOptions({ fillColor: '#fff' });
            isMouseOver = false;
        }, 50);
    });

    kakao.maps.event.addListener(polygon, 'click', function () {
        console.log('Clicked region:', area.name);
        polygon.setOptions({ fillColor: '#21d12b' });

        // 해당 지역에 맞는 이미지로 슬라이더 업데이트
        updateSliderForRegion(area.name);
    });

    return polygon;
}

// 지역 클릭 시 슬라이더를 해당 이미지로 업데이트
function updateSliderForRegion(region) {
    const regionImages = images[region] ? [images[region]] : ['/static/images/default.jpg'];

    sliderInner.innerHTML = '';  // 기존 슬라이더 초기화
    regionImages.forEach(imageSrc => {
        const sliderDiv = document.createElement('div');
        sliderDiv.classList.add('slider');

        const img = document.createElement('img');
        img.src = imageSrc;
        img.alt = region;

        sliderDiv.appendChild(img);
        sliderInner.appendChild(sliderDiv);
    });

    // 슬라이더 재초기화
    currentIndex = 0;
    initSlider();
}

// 초기화
generateSlider(images);
initSlider();
init("/static/json/sido_2.json");
