const firstNum = document.getElementById("number1");
const secondNum = document.getElementById("number2");
const thirdNum = document.getElementById("number3");

const attempts = document.getElementById("attempts");
const results = document.getElementById("results");
results.style = "width:100%;"
const resultImg = document.getElementById("game-result-img");
const submitBtn = document.getElementsByClassName("submit-button")[0];

// =============== true 값으로 바꾸면 콘솔창에서 정답을 볼 수 있습니다 ===============
const consoleAnswer = true;
//=========================================================================

const max_try = 9;
let myTry = 0;

function insertStrikeBall(strike,ball){
    let resultHtml = `<div style="box-sizing: border-box;
                                width:100%;height:50px;
                                padding-left:20px;
                                display:flex; justify-content: space-between;
                                ">
                        <p>${firstNum.value} ${secondNum.value} ${thirdNum.value}</p>
                        <p>:</p>
                        <div style="width:150px;height:100%;
                                    display:flex; justify-content: space-evenly; align-items: center;">
                            ${strike}
                            <div style="height:70%; aspect-ratio: 1/1;
                                        border-radius: 50%;
                                        background-color: green;
                                        display:flex; justify-content: center; align-items: center;">S</div>
                            ${ball}
                            <div style="height:70%; aspect-ratio: 1/1;
                                        border-radius: 50%;
                                        background-color: yellow;
                                        display:flex; justify-content: center; align-items: center;">B</div>
                        </div>
                    </div>`;
    return resultHtml;
}

function insertOut(){
    let resultHtml = `<div style="box-sizing: border-box;
                                width:100%;height:50px;
                                padding-left:20px;
                                display:flex; justify-content: space-between;
                                ">
                        <p>${firstNum.value} ${secondNum.value} ${thirdNum.value}</p>
                        <p>:</p>
                        <div style="width:150px;height:100%;
                                    display:flex; justify-content:right; align-items: center;">
                            <div style="height:70%; aspect-ratio: 1/1;
                                        border-radius: 50%; margin-right:13px;
                                        background-color: red;
                                        display:flex; justify-content: center; align-items: center;">O</div>
                        </div>
                    </div>`
    return resultHtml;
}

function makeRandAnswer(){ //랜덤값 3개 생성하는 함수
    let nums = [0,1,2,3,4,5,6,7,8,9];
   
    let randIndex = Math.floor(Math.random() * (nums.length));
    const firstVal = nums[randIndex];
    nums.splice(randIndex,1);

    randIndex = Math.floor(Math.random() * (nums.length));
    const secondVal = nums[randIndex];
    nums.splice(randIndex,1);

    randIndex = Math.floor(Math.random() * (nums.length));
    const thirdVal = nums[randIndex];
    nums.splice(randIndex,1);
    
    const result = [firstVal,secondVal,thirdVal];
    if(consoleAnswer){console.log(`answer : ${result}`)};
    return result;
}

const randAnswer = makeRandAnswer(); //랜덤값 3개 생성하는 함수

function isInputEmpty(){
    if(firstNum.value === "" || secondNum.value === "" || thirdNum.value === ""){
        return true
    }
    return false
}

function emptyInput(){
    firstNum.value = '';
    secondNum.value = '';
    thirdNum.value = '';
}

function BtnNonActivated(){ //버튼 비활성화 시키는 함수
    submitBtn.disabled = true;
    submitBtn.style = 'background-color:#595959; color:#858585;';
}

function ballStrikeOut(myAnswer,answer){
    let ballNumStrikeIncluded = 0;
    for (let i=0;i < answer.length ;i++){
        for (let j=0;j<myAnswer.length;j++){
            if(answer[i] === myAnswer[j]){
                ballNumStrikeIncluded += 1;
            };
        };
    };

    let strike_num = 0;
    for (let i=0;i < answer.length;i++){
        if(answer[i] === myAnswer[i]){
            strike_num += 1;
        }
    }

    ball_num = ballNumStrikeIncluded - strike_num;

    isOut = false;
    if (strike_num === 0 && ball_num === 0){
        isOut = true;
    }

    let result = {
        ball:ball_num,
        strike:strike_num,
        out:isOut
    }

    return result
};

function check_numbers(){
    let result = [Number(firstNum.value),Number(secondNum.value),Number(thirdNum.value)];
    let resultDict = ballStrikeOut(result,randAnswer)

    if(isInputEmpty()){//입력이 비어있으면 함수 종료
        emptyInput();
        return;
    }

    if (resultDict.strike === randAnswer.length){ //승리조건
        BtnNonActivated()
        results.innerHTML += insertStrikeBall(resultDict.strike,resultDict.ball);
        resultImg.src = 'success.png';
        emptyInput();
    } else{
        myTry += 1;
        attempts.innerText = max_try - myTry;
        if(resultDict.out){//아웃됨
            results.innerHTML += insertOut()
        } else {//아웃 안됨
            results.innerHTML += insertStrikeBall(resultDict.strike,resultDict.ball);
        }
        //횟수 초과 게임 끝
        if(myTry >= max_try){
            BtnNonActivated()
            resultImg.src = 'fail.png';
        }
        emptyInput();
    }
};