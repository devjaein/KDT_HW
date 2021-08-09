// 상품 데이터
const data = [
    { name: '초콜렛', price: 2000 },
    { name: '아이스크림', price: 1000 },
    { name: '컵라면', price: 1600 },
    { name: '볼펜', price: 2500 },
    { name: '아메리카노', price: 4000 },
    { name: '과자', price: 3000 },
    { name: '탄산수', price: 1200 },
    { name: '떡볶이', price: 3500 },
    { name: '노트', price: 1500 },
    { name: '껌', price: 500 }
];

// 사용자 입력 받기
const line = prompt('최대 금액을 입력해주세요.');
const amount = +line;

// 주어진 금액으로 살 수 있는 가장 비싼 상품을 구함
const item = getItemByAmount(data, amount); 

const msg = item ? 
    `${amount}원으로 살 수 있는 가장 비싼 상품은 [${item.name}]이고, 가격은 ${item.price}원입니다.` : 
    '살 수 있는 상품이 없습니다.';

// 결과 출력
alert(msg);

// 아래에 getItemByAmount 함수를 작성하세요.
function getItemByAmount(item, usePrice) { //item: 상품 데이터, usePrice: 사용자가 입력한 금액
    let max_price = 0; //최대 가격은 가장 작은 값인 0으로 초기화
    data.forEach( i => {//상품 데이터를 한번씩 반복
        if (usePrice - i.price >= 0) { //사용자가 입력한 금액에서 상품 데이터 금액을 뺐을 때 양수일 경우 구매 가능한 물품
            if (max_price < i.price) { //구매 가능한 물품 중에서 최대 금액이 반복을 통해 새로 들어온 금액보다 작을 경우
                max_price = i.price; // 새로 들어온 금액을 최대 금액으로 swap
            } 
        }
    })

    if (max_price === 0) 
        return null; //max_price가 상품 데이터 가격보다 낮아 swap가 안된 경우 null을 리턴
    else {
        for (let i = 0; i < data.length; i++) { //상품 데이터를 한번씩 반복
            if (max_price === data[i].price){ //max_price와 상품 데이터의 가격과 동일한 금액이면 
                return data[i]; //동일한 금액의 데이터의 인덱스를 반환
            } 
        }
    }
}
