document.addEventListener('DOMContentLoaded' , function(){
  window.addEventListener('scroll' , myFunction);
  var navbar = document.getElementById("navbar");
  var sticky = navbar.offsetTop;

  function myFunction(){
    if (window.pageYOffset >= sticky){
      navbar.classList.add("sticky");
      document.getElementById("con").style.paddingTop = "40px";
    }
    else{
      navbar.classList.remove("sticky");
      document.getElementById("con").style.paddingTop = "0px";
    }
  }
});

function postgrad(){
  var check = document.getElementById("postgraduation1");
  var show = document.getElementById("postgraduation");
  if (check.checked == true){
    show.style.display = "block";
  }
  else{
    show.style.display = "none";
  }
}

function grad(){
  var check = document.getElementById("graduation1");
  var show = document.getElementById("graduation");
  if (check.checked == true){
    show.style.display = "block";
  }
  else{
    show.style.display = "none";
  }
}

function exp(){
  var check = document.getElementById("experienced");
  var show = document.getElementById("exp1");
  
  if (check.checked == true){
    show.style.display = "inline-block";
  }
  {
    show.style.display = "none";
  }
}



$(document).ready(function(){
  $("#myCarousel").carousel({interval: 4000});
  
  $(".left").click(function(){
    $("#myCarousel").carousel("prev");
  });
  
  $(".right").click(function(){
    $("#myCarousel").carousel("next");
  });
});


