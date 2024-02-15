let questions = null;
let num_of_questions = 0;

window.onload = event => {
    fetch("/data")
    .then(response => response.json())
    .then(response => {
        console.log("Data!");
        // console.log(response.data);
        questions = response.data;
        num_of_questions = questions.length;
        shuffleQuestions(questions);
        document.getElementById("question").innerHTML = questions[0];
    })
    .catch(error => console.log(error));
}

let buttonCounter = 0;
const submitBtn = document.getElementById("submit-btn");
const questionTitle = document.getElementById("question");

// const questions = [
//     "Question 1",
//     "Question 2",
//     "Question 3",
//     "Question 4",
//     "Question 5",
// ]

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
    answers.push(1); //add 1 for true answers
    buttonCounter++;
    if(buttonCounter >= num_of_questions){ //if max is reached, disable both buttons and display the submit button
        document.getElementById("true-btn").disabled = true;
        document.getElementById("false-btn").disabled = true;
        submitBtn.style.display = "inline-block";
    }
    else{
        questionTitle.innerHTML = questions[buttonCounter]; //next question in array is displayed
    }
}

function falseClick(){
    answers.push(0); //add 0 for false answers
    buttonCounter++;
    if(buttonCounter >= num_of_questions){ //if max is reached, disable both buttons and display the submit button
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

    // fetch('/process') //get data from flask app route that handles the process route
    // .then(response => response.text())
    // .then(text => {
    //     console.log('GET Request')
    //     console.log(text);
    // })

    fetch('/process', {

        //declare what type of content we are sending
        headers: {
            'Content-type': 'application/json' 
        },

        //specify HTTP method
        method: 'POST',

        //JSON to be sent
        body: JSON.stringify({
            "answers": answers
        })
    }).then(response => response.json())
    .then(data => {
        console.log(data)

        let num_of_true_answers = data.total;
        document.getElementById("true-num").innerHTML = num_of_true_answers;

        document.getElementById("results-container").style.display = 'block';
    })
    .catch(error => console.log(error))
}

