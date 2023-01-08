var current_course = getCookie("course_name");
var set_cour = document.getElementById("id_quiz_course_name");
set_cour.setAttribute("value",current_course);
console.log(current_course);