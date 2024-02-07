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

//to store questions that are answered as true
const answers = [];

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
    answers.push(questions[buttonCounter]); //add QID answered as true to answers array
    buttonCounter++;
    if(buttonCounter >= 5){ //if max is reached, disable both buttons and display the submit button
        document.getElementById("true-btn").disabled = true;
        document.getElementById("false-btn").disabled = true;
        submitBtn.style.display = "inline-block";
    }
    else{
        questionTitle.innerHTML = questions[buttonCounter]; //next question in array is displayed
    }
}

function falseClick(){
    buttonCounter++;
    if(buttonCounter >= 5){ //if max is reached, disable both buttons and display the submit button
        document.getElementById("true-btn").disabled = true;
        document.getElementById("false-btn").disabled = true;
        submitBtn.style.display = "inline-block";
    }
    else{
        questionTitle.innerHTML = questions[buttonCounter]; //next question in array is displayed
    }
}

function submitClick(){
    console.log(answers); 
}

