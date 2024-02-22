//object to store questions and if they are answered true or false
let questions = {};
let num_of_questions = 0;

let buttonCounter = 0;
const submitBtn = document.getElementById("submit-btn");
const questionTitle = document.getElementById("question");

//to store array of 1s and 0s (true and false answers to questions) to be sent for processing
const answers = [];


window.onload = event => {
    //get questions from csv  
    fetch("/data")
    .then(response => response.json())
    .then(response => {
        console.log("Data!");
        console.log(response.data);
        //create one list to hold question values as returned from JSON data, and one list to hold formatted questions for displaying to user
        question_names_unformatted = response.data;
        question_names_formatted = [];

        //add each question to "questions" object with "answered" value set to 0
        //add properly formatted questions with correct gramamr to second questions list
        question_names_unformatted.forEach((elem, index) => {
            questions[elem] = 0;

            //formatting
            if(index == 4 || index == 5 || index == 7 || index == 10 || 
                index == 13 || index == 14){
                    question_names_formatted[index] = "Is your animal " + elem + "?";
                }
            else if(index == 6 || index == 15 || index == 16){
                question_names_formatted[index] = "Is your animal a " + elem + "?";
            }
            else if(index == 8 || index == 12){
                question_names_formatted[index] = "Does your animal have a " + elem + "?";
            }
            else if(index == 2){
                question_names_formatted[index] = "Does your animal lay " + elem + "?";
            }
            else if(index == 9){
                question_names_formatted[index] = "Does your animal " + elem + " air?";
            }
            else if(index == 17){
                question_names_formatted[index] = "Is your animal commonly active at " + elem + "?";
            }
            else {
                question_names_formatted[index] = "Does your animal have " + elem + "?";
            }
        })

        console.log(JSON.stringify(questions, null, 4));

        //the total number of questions, based on incoming csv data
        num_of_questions = question_names_unformatted.length;
        //randomly order questions for asking user, both lists are randomized in the same order
        shuffleQuestions(question_names_unformatted, question_names_formatted);
        //display first question
        document.getElementById("question").innerHTML = question_names_formatted[0];
    })
    .catch(error => console.log(error));
}


//understand this fully later
function shuffleQuestions(qList1, qList2) {
    for (let i = qList1.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        let temp = qList1[i];
        qList1[i] = qList1[j];
        qList1[j] = temp;
        //shuffle second list in exact same way
        temp = qList2[i];
        qList2[i] = qList2[j];
        qList2[j] = temp;     
    }

    console.log(qList1);
    console.log(qList2);
}

//submit button only displays after certain number of true/false clicks (currently 5 for testing, will be 20)
function trueClick(){
    //get current question name and find it in object, change "answered" value to 1 for respective question
    current_question_unf = question_names_unformatted[buttonCounter];
    questions[current_question_unf] = 1;
    buttonCounter++;
    if(buttonCounter >= num_of_questions){ //if max is reached, disable both buttons and display the submit button
        document.getElementById("true-btn").disabled = true;
        document.getElementById("false-btn").disabled = true;
        submitBtn.style.display = "inline-block";
    }
    else{
        questionTitle.innerHTML = question_names_formatted[buttonCounter]; //next question in formatted questions array is displayed
    }
}

function falseClick(){
    buttonCounter++;
    if(buttonCounter >= num_of_questions){ //if max is reached, disable both buttons and display the submit button
        document.getElementById("true-btn").disabled = true;
        document.getElementById("false-btn").disabled = true;
        submitBtn.style.display = "inline-block";
    }
    else{
        questionTitle.innerHTML = question_names_formatted[buttonCounter]; //next question in formatted questions array is displayed
    }
}

function submitClick(){
    console.log(JSON.stringify(questions, null, 4));

    for(let x in questions) {
        answers.push(questions[x]);
    }
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

        //TODO: fix the var names
        let animal_result = data.total;

        document.getElementById("question-container").style.display = "none";
        document.getElementById("submit-container").style.display = "none";

        document.getElementById("animal-result").innerHTML = animal_result;

        document.getElementById("results-container").style.display = 'block';
    })
    .catch(error => console.log(error))
}

function correctAnswer(){
    document.getElementById("verify-answer").style.display = "none";
    document.getElementById("next-steps-true").style.display = "block";
    document.getElementById("reload-btn").style.display = "block"; //display button to reload page and play game again
}

function wrongAnswer(){
    document.getElementById("verify-answer").style.display = "none";
    document.getElementById("next-steps-false").style.display = "block";
}
function addAnimal(){
    document.getElementById("new-animal-btn").disabled = true;
    
    let new_animal = document.getElementById('new-animal').value;
    // console.log(answers);

    fetch('/addAnimal', {
        //declare what type of content we are sending
        headers: {
            'Content-type': 'application/json' 
        },

        //specify HTTP method
        method: 'POST',

        //JSON to be sent
        body: JSON.stringify({
            "animal" : new_animal,
            "answers": answers
        })
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("response").innerHTML = data.message;
        document.getElementById("reload-btn").style.display = "block";  //display button to reload page and play game again

    })
    

}

function reloadPage(){
    window.location.reload();
}