window.onload = event => {
    shuffleQuestions(questions);
    // console.log(questions);
    document.getElementById("question").innerHTML = questions[0];
}

let buttonCounter = 0;
const submitBtn = document.getElementById("submit-btn");
const questionTitle = document.getElementById("question");

const questions = [
    "Question 1",
    "Question 2",
    "Question 3",
    "Question 4",
    "Question 5",
]

//understand this fully later
function shuffleQuestions(qList) {
    for (let i = qList.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        let temp = qList[i];
        qList[i] = qList[j];
        qList[j] = temp;
    }
}

//submit button only displays after certain number of true/false clicks (currently 5 for testing, will be 20)
function trueClick(){
    buttonCounter++;
    console.log(buttonCounter);
    if(buttonCounter >= 5){
        submitBtn.style.display = "inline-block";
    }
    else{
        questionTitle.innerHTML = questions[buttonCounter];
    }
}

function falseClick(){
    buttonCounter++;
    console.log(buttonCounter);
    if(buttonCounter >= 5){
        submitBtn.style.display = "inline-block";
    }
    else{
        questionTitle.innerHTML = questions[buttonCounter];
    }
}


