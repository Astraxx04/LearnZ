
//Person Name - Key, tool - 0 index, github - 1 index,, linkdin - 2 index,, imagepath - 3 index

const Peoples = {
  "Aditi Pandey": ["Jenkins, Frontend, Backend", "https://github.com/aditipandey16", "http://www.linkedin.com/in/-aditi-pandey", "/static/authentication/images/creator/aditi.jpeg"],
  "Ahmed Fadil": ["Selenium, Snyk", "https://github.com/ahmedfadil", "https://www.linkedin.com/in/ahmed-fadil-74aa8b21b/", "/static/authentication/images/creator/ahmed.jpeg"],
  "Akash Sil": ["Docker, Jenkins, AWS, Backend", "https://github.com/Orange-Tofu", "https://www.linkedin.com/in/akash-s-64b6b21b7", "/static/authentication/images/creator/akash.jpeg"],
  "Anujna G K": ["Selenium, Frontend", "https://github.com/anujnaaa", "https://www.linkedin.com/in/anujna-g-k-5a3a16232", "/static/authentication/images/creator/anujna.jpeg"],
  "Ayushi Sah": ["Docker, Frontend, Backend", "https://github.com/aazaleas", "https://www.linkedin.com/in/ayushi-sah-61a351224/", "/static/authentication/images/creator/ayushi.jpeg"],
  "Bhawesh Agarwal": ["AWS, Frontend, Backend", "https://github.com/Bhawesh02", "https://www.linkedin.com/in/bhawesh-agarwal-70b98b113/", "/static/authentication/images/creator/bhawesh.jpeg"],
  "Gagan S": ["Github, Backend", "https://github.com/Astraxx04", "https://www.linkedin.com/in/gagan-s-105706202", "/static/authentication/images/creator/gagan.jpeg"],
  "Janesh Walia": ["Docker, Backend", "https://www.github.com/Janesh7", "https://www.linkedin.com/in/janesh-walia-483378226", "/static/authentication/images/creator/janesh.jpeg"],
  "Lakshitha Ravichandra": ["Github, Frontend", "https://github.com/LakshithaR", "https://www.linkedin.com/in/lakshitha-ravichandra-4781001b6/", "/static/authentication/images/creator/lakshitha.jpeg"],
  "Konjeti Nidhi": ["Snyk, Frontend", "https://github.com/Sonuuuuuuu", "https://www.linkedin.com/in/konjeti-nidhi-96245a226/", "/static/authentication/images/creator/nidhi.jpeg"]
};


const CardContainer = document.getElementById("CardContainer");
//For Every person insert card 
Object.keys(Peoples).forEach(People => {
  //Creted div with class div;
  var div = document.createElement('div');
  div.classList.add("card");
  CardContainer.appendChild(div);
  //Creted div with class content and make card as parent;
  var div1 = document.createElement('div');
  div1.classList.add("content");
  div.appendChild(div1);
  //Creted div with class imgbx and make content as parent;
  var div2 = document.createElement('div');
  div2.classList.add("imgBx");
  div1.appendChild(div2);
  //create img with imgbx as parent
  var img = document.createElement('img');
  img.setAttribute("src", Peoples[People][3]);
  div2.appendChild(img);
  //Creted div with class contentBx and make content as parent
  var div4 = document.createElement('div');
  div4.classList.add("contentBx");
  div4.innerHTML = "<h3><b>" + People + "</b><br /></h3>";
  // div4.innerHTML = "<h3>" + People + "<br /><span>" + Peoples[People][0] + "</span></h3>";
  div1.appendChild(div4);
  //added git and likdin to card as parent
  var ul = document.createElement('ul');
  ul.classList.add("sci");
  div.appendChild(ul);
  var li = document.createElement('li');
  li.setAttribute("style", "\"--i: 1\"")
  li.innerHTML = "<a href=\"" + Peoples[People][1] + "\" target=\"_blank\"><i class=\"fa-brands fa-github\"></i></a>";
  ul.appendChild(li);
  var li1 = document.createElement('li');
  li1.setAttribute("style", "\"--i: 1\"")
  li1.innerHTML = "<a href=\"" + Peoples[People][2] + "\" target=\"_blank\"><i class=\"fa-brands fa-linkedin\"></i></a>";
  ul.appendChild(li1);

});