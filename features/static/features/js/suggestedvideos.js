
$(document).ready(function(){
    let apiKey = "AIzaSyA_LrwXq6Zxzb0t9U3DDrTeU-p9nv8Z6tc.."
 
    //$("form").submit((e) => {
      //  e.preventDefault()
        //let search = $("#search").val()
        videoSearch(apiKey,"three schema architecture",4)
        videoSearch(apiKey,"dbms",2)
    //})
})
 
function videoSearch(apiKey,search,maxResults){

    $("#videos").empty()

    $.get("https://www.googleapis.com/youtube/v3/search?key=" + apiKey + "&type=video&part=snippet&maxResults=" + maxResults + "&q=" + search + "&sp=CAM%253D",(data) => {
        console.log(data)
 
        let video = ''
 
        data.items.forEach(item => {
            video = `
            <iframe width="512" height="288" src="http://www.youtube.com/embed/${item.id.videoId}" frameborder="0" allowfullscreen></iframe>
            `
            $("#videos").append(video)
        });
    })
}

var dat = [];
//fetch function
fetch('data.json').then(
    function(u){ return u.json();}
    ).then(
    function(json){
    data_function(json); //calling and passing json to another function data_function
    }
    )
    
    //another functions
    function data_function(data){
    data.forEach(function (da) {
        dat.push(da);
    });

    }

console.log(typeof(dat));    

function searchkey(){
    
}


  