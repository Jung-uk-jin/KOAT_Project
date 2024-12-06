import { images } from '/static/js/images.js';

    const sliderInner = document.querySelector(".slider__inner");
    const sliderImg = document.querySelector(".slider__img");
    const sliderBtnPrev = document.querySelector(".prev");
    const sliderBtnNext = document.querySelector(".next");

    const sliderWidth = 400; // 고정된 너비
    const sliderHeight = 300; // 고정된 높이
    let currentIndex = 1;

    // 슬라이더 생성
    function generateSlider(images) {
        Object.keys(images).forEach((region) => {
            const sliderDiv = document.createElement("div");
            sliderDiv.classList.add("slider");

            const img = document.createElement("img");
            img.src = images[region];
            img.alt = region;

            sliderDiv.appendChild(img);
            sliderInner.appendChild(sliderDiv);
        });
    }

    // 슬라이드 초기화
    function initSlider() {
        const sliders = document.querySelectorAll(".slider");
        const firstClone = sliders[0].cloneNode(true);
        const lastClone = sliders[sliders.length - 1].cloneNode(true);

        sliderInner.appendChild(firstClone);
        sliderInner.insertBefore(lastClone, sliders[0]);

        sliderInner.style.width = `${(sliders.length + 2) * sliderWidth}px`;
        sliderInner.style.transform = `translateX(-${sliderWidth * currentIndex}px)`;
    }

    // 슬라이드 이동
    function gotoSlider(index) {
        const sliders = document.querySelectorAll(".slider");

        if (index >= sliders.length) {
            // 마지막 슬라이드에서 오른쪽 버튼 클릭시 첫 번째로 돌아가게
            currentIndex = 1;
            sliderInner.style.transition = "none"; // 애니메이션 없이 바로 이동
            sliderInner.style.transform = `translateX(-${sliderWidth * currentIndex}px)`;
            setTimeout(() => {
                sliderInner.style.transition = "all 400ms ease-in-out"; // 다시 애니메이션 적용
                currentIndex++;
                sliderInner.style.transform = `translateX(-${sliderWidth * currentIndex}px)`;
            }, 50); // 잠시 후 애니메이션이 적용되도록
        } else if (index < 0) {
            // 첫 번째 슬라이드에서 왼쪽 버튼 클릭시 마지막 슬라이드로 돌아가게
            currentIndex = sliders.length - 2;
            sliderInner.style.transition = "none"; // 애니메이션 없이 바로 이동
            sliderInner.style.transform = `translateX(-${sliderWidth * currentIndex}px)`;
            setTimeout(() => {
                sliderInner.style.transition = "all 400ms ease-in-out"; // 다시 애니메이션 적용
                currentIndex--;
                sliderInner.style.transform = `translateX(-${sliderWidth * currentIndex}px)`;
            }, 50); // 잠시 후 애니메이션이 적용되도록
        } else {
            sliderInner.style.transition = "all 400ms ease-in-out";
            sliderInner.style.transform = `translateX(-${sliderWidth * index}px)`;
            currentIndex = index;
        }
    }

    // 왼쪽 버튼 클릭
    sliderBtnPrev.addEventListener("click", () => {
        gotoSlider(currentIndex - 1);
    });

    // 오른쪽 버튼 클릭
    sliderBtnNext.addEventListener("click", () => {
        gotoSlider(currentIndex + 1);
    });

    // 초기화
    generateSlider(images);
    initSlider();