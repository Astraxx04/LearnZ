
//Course name - Key,, current chapter - 0 index,, chapter name - 1 index

var NoOfSemester = 7;
var currentSem = 1;
const data = document.currentScript.dataset;
const user_id = data.usn;
//console.log(data.usn);

//const from html
const CourseContainer = document.getElementById("CourseContainer");
const dropdown = document.getElementById("dropdown");
const useinfo = document.getElementById("useinfo");

//User Usn
var span = document.createElement('span');
span.classList.add("user_id");
span.innerHTML = user_id;
useinfo.appendChild(span);

function setCookie(cname, cvalue, exdays) {
  const d = new Date();
  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
  let expires = "expires="+d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}

function getCookie(cname) {
  let name = cname + "=";
  let ca = document.cookie.split(';');
  for(let i = 0; i < ca.length; i++) {
    let c = ca[i];
    while (c.charAt(0) == ' ') {
      c = c.substring(1);
    }
    if (c.indexOf(name) == 0) {
      return c.substring(name.length, c.length);
    }
  }
  return "";
}



for (let index = 0; index < NoOfSemester; index++) {

  var a = document.createElement('a');
  a.setAttribute("id", "Sem_" + (index + 1));
  a.innerHTML = `<li>Semester ` + (index + 1) + `</li>`;
  dropdown.appendChild(a);
}
var sem_1 = document.getElementById('Sem_1');
sem_1.addEventListener('click', function () {
  currentSem = 1;
  //console.log(currentSem);
  remove_courses();
  add_courses();
});
var sem_2 = document.getElementById('Sem_2');
sem_2.addEventListener('click', function () {
  currentSem = 2;
  //console.log(currentSem);
  remove_courses();
  add_courses();
});
var sem_3 = document.getElementById('Sem_3');
sem_3.addEventListener('click', function () {
  currentSem = 3;
  //console.log(currentSem);
  remove_courses();
  add_courses();
});
var sem_4 = document.getElementById('Sem_4');
sem_4.addEventListener('click', function () {
  currentSem = 4;
  //console.log(currentSem);
  remove_courses();
  add_courses();
});
var sem_5 = document.getElementById('Sem_5');
sem_5.addEventListener('click', function () {
  currentSem = 5;
  //console.log(currentSem);
  remove_courses();
  add_courses();
}); var sem_5 = document.getElementById('Sem_5');
sem_5.addEventListener('click', function () {
  currentSem = 5;
  //console.log(currentSem);
  remove_courses();
  add_courses();
}); var sem_6 = document.getElementById('Sem_6');
sem_6.addEventListener('click', function () {
  currentSem = 6;
  //console.log(currentSem);
  remove_courses();
  add_courses();
});
var sem_7 = document.getElementById('Sem_7');
sem_7.addEventListener('click', function () {
  currentSem = 7;
  //console.log(currentSem);
  remove_courses();
  add_courses();
});


function remove_courses() {
  CourseContainer.innerHTML = "";
}

function add_courses() {

  courses[currentSem][0].forEach(Course => {
  //Creted div with class card;
  var div = document.createElement('div');
  div.classList.add("card");
  div.setAttribute("course_name",Course[0]);
  CourseContainer.appendChild(div);
  //Creted div with class course-preview and make card as parent;
  var div1 = document.createElement('div');
  div1.classList.add("course-preview");
  div1.innerHTML=`
  <h2>`+Course[0]+`</h2><a href="/teacher">
  <button class="btn" id="${Course[0]}">Continue</button></a>`;
  div.appendChild(div1);
  
});

var cards = document.getElementsByClassName("card");
Array.from(cards).forEach(function (card) {
  card.addEventListener('click',()=>{
    setCookie("course_name", card.getAttribute("course_name"), 1);
    //console.log(getCookie("course_name"));
  });
})





}




add_courses();



















