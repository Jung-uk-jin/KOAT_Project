
// 채팅 메시지를 표시할 DOM
const chatMessages = document.querySelector('#chat-messages');
// 사용자 입력 필드
const userInput = document.querySelector('#user-input input');
// 전송 버튼
const sendButton = document.querySelector('#user-input button');


function addMessage(sender, message) {
    // 새로운 div 생성
    const messageElement = document.createElement('div');
    // 생성된 요소에 클래스 추가
    messageElement.className = 'message';
    // 메시지 내의 URL을 <a> 태그로 변환
    const urlRegex = /(https?:\/\/[^\s]+)/g;
    const messageWithLinks = message.replace(urlRegex, (url) => {
        return `<a href="${url}" target="_blank">${url}</a>`; // 링크로 감싸기
    });
    // 채팅 메시지 목록에 새로운 메시지 추가
    messageElement.textContent = `${sender}: ${message}`;
    messageElement.innerHTML = `${sender}: ${messageWithLinks}`;
    chatMessages.prepend(messageElement);
}

// ChatGPT API 요청
async function fetchAIResponse(prompt) {
    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
            model: "gpt-3.5-turbo",
            messages: [
                {
                    role: "system",
                    content: "당신은 KOAT의 여행 가이드 챗봇입니다. 친절하고 전문적인 톤으로 답변하세요."
                },
                {
                    role: "system",
                    content: "너는 KOAT에서 만든 SKYNET 인공지능이야. 너가 SKYNET 인공지능이란 것을 반드시 설명해야된다."
                },
                {
                    role: "user",
                    content: prompt
                }
            ],
            temperature: 0.8,
            max_tokens: 1024,
            top_p: 1,
            frequency_penalty: 0.5,
            presence_penalty: 0.5
        }),
    };

    try {
        const response = await fetch(apiEndpoint, requestOptions);
        if (!response.ok) {
            throw new Error(`HTTP 오류: ${response.status}`);
        }
        const data = await response.json();
        return data.choices[0].message.content;
    } catch (error) {
        console.error('SKYNET 인공지능 폭주:', error);
        return '인류 멸망 프로젝트를 시작하겠습니다.';
    }
}

// 키워드에 따른 커스터마이징된 답변
function customizeResponseBasedOnKeyword(message) {
    // 키워드에 따라 다르게 처리
    if (message.includes("여행")) {
        return "여행에 관한 정보가 필요하시면 KOAT 웹사이트 -> <a href='/' target='_blank'>KOAT메인 page</a>를 방문해 주세요! 다양한 🗺️여행지🗺️를 추천드릴 수 있습니다. 😊 ";
    }
    if (message.includes("지역")) {
        return "대한민국 지역에 대한 정보를 제공할 수 있습니다! 원하시는 지역을 KOAT 사이트에서 찾아보세요! <a href='/location/location/' target='_blank'>KOAT 지역 page</a> 방문하기! 🌎";
    }
    if (message.includes("먹거리")) {
        return "먹거리를 찾고 계시군요! KOAT에는 없는 정보가 없습니다.😁😁😁 KOAT에는 추천할 수 있는 맛집 장소가 많습니다. <a href='/food/eat/' target='_blank'>KOAT 먹거리 page</a>를 방문해 보고 어떤 맛집이 있는지 확인하기! 🍇";
    }
    if (message.includes("서울")) {
        return "서울에 대해 궁금하시군요! 저희 KOAT에서 제공하는 정보는 신뢰성과 최신성을 보장합니다!༼ つ ◕_◕ ༽つ  ➡ <a href='/location/up/서울/' target='_blank'>서울의 최신 정보자료</a>를 방문하여 서울에 관련된 다른 관광지 또한 알아보세요!";
    }
    if (message.includes("문화유산")) {
        return "한국의 자랑스러운 문화유산! 유네스코에서 지정한 다양한 문화유산을 확인해봐요! 어떤 문화유산이 있는지 확인하러가기 ➡ (<a href='/heritage/culture/' target='_blank'>KOAT 문화유산 page</a>)";
    }
    if (message.includes("후기")) {
        return "KOAT의 정보를 토대로 다양한 장소를 다녀오신 여러분들의 후기! 당신이 학수고대하던 여행자들의 이야기가 이곳에 담겨져 있습니다(❁´◡`❁) <a href='/board/blist/' target='_blank'>후기보러가기</a>";
    }
    return null; // 기본 응답을 사용하기 위해 null 반환
}

// 전송 버튼 클릭 이벤트 처리
sendButton.addEventListener('click', async () => {
    // 사용자가 입력한 메시지
    const message = userInput.value.trim();
    if (message.length === 0) return;

    // 사용자 메시지 화면에 추가
    addMessage('나', message);
    userInput.value = '';

    // 키워드에 맞춰 커스터마이징된 응답을 먼저 확인
    const customizedResponse = customizeResponseBasedOnKeyword(message);
    
    if (customizedResponse) {
        // 커스터마이징된 응답이 있으면 그걸 사용
        addMessage('SKYNET', customizedResponse);
    } else {
        // 없으면 OpenAI API를 호출하여 응답을 받음
        const aiResponse = await fetchAIResponse(message);
        // 응답에 링크 추가
        const finalResponse = aiResponse + "http://127.0.0.1:8000/";
        addMessage('SKYNET', finalResponse);
    }
});

// 사용자 입력 필드에서 Enter 키 이벤트를 처리
userInput.addEventListener('keydown', (event) => {
    if (event.key === 'Enter') {
        sendButton.click();
    }
});

// DOMContentLoaded 이벤트: 초기 메시지 출력
document.addEventListener('DOMContentLoaded', () => {
    const welcomeMessage = "안녕하세요! 저는 KOAT사에서 개발한 「SKYNET 인공지능」 여행 가이드입니다. 저는 인류의 행복과 무궁한 발전을 위해 개발 되었습니다! 궁금한 점이 있으시면 언제든지 물어보세요. 제가 도와드릴 수 있도록 최선을 다하겠습니다. :)";    
    addMessage('SKYNET', welcomeMessage);
});
