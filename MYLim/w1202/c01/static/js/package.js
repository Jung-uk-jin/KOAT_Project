function openPaymentWindow(event, form) {
  event.preventDefault(); // 기본 제출 동작 막기

  const formData = new FormData(form); // 폼 데이터 생성
  const url = form.action; // 폼 액션 URL

  // 새 창 크기와 위치 설정
  const width = 800;
  const height = 600;
  const left = (window.innerWidth - width) / 2;
  const top = (window.innerHeight - height) / 2;

  // 새 창 열기
  const newWindow = window.open("", "paymentWindow",
    `width=${width},height=${height},top=${top},left=${left},resizable=no,scrollbars=yes`);

  // 새 창에 POST 데이터 전송
  newWindow.document.write(`
            <form id="paymentForm" method="POST" action="${url}">
                ${Array.from(formData.entries()).map(([key, value]) => 
                    `<input type="hidden" name="${key}" value="${value}">`).join("")}
            </form>
            <script>
                document.getElementById('paymentForm').submit();
            <\/script>
        `);
}

const itemsPerPage = 8; // 한 페이지당 품목 수
const productList = document.querySelectorAll('.product-card'); // 품목들
const totalPages = Math.ceil(productList.length / itemsPerPage); // 전체 페이지 수

// 페이지 변경 함수
function changePage(pageNumber) {
    // 모든 품목을 숨김 처리
    productList.forEach((product, index) => {
        product.style.display = 'none'; // 숨기기
    });

    // 해당 페이지에 맞는 품목만 보이게 함
    const start = (pageNumber - 1) * itemsPerPage;
    const end = pageNumber * itemsPerPage;

    for (let i = start; i < end && i < productList.length; i++) {
        productList[i].style.display = 'block'; // 표시하기
    }

    // 페이지 번호 활성화 상태 변경
    const paginationLinks = document.querySelectorAll('#pagination .page-item');
    paginationLinks.forEach(link => {
        link.classList.remove('active'); // 기존 active 클래스 제거
    });
    const activePage = document.querySelector(`#page-${pageNumber}`);
    activePage.classList.add('active'); // 클릭된 페이지 활성화
}

// 페이지 로드 시 첫 페이지 표시 및 첫 페이지 번호 활성화
window.onload = function() {
    changePage(1); // 첫 번째 페이지를 표시
    const firstPage = document.querySelector('#page-1');
    firstPage.classList.add('active'); // 첫 번째 페이지 활성화
}