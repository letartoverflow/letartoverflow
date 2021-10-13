  document.getElementById("times").style.display="none"
        document.getElementById("menu").style.maxHeight="0px"
   function opn(){
    document.getElementById("menu");
    menu.style.maxHeight="230px"
    navigator.vibrate(60);
     document.getElementById("bars").style.display="none"
     document.getElementById("times").style.display="block"
   }
   function cls(){
    document.getElementById("menu");
    menu.style.maxHeight="0px"
    navigator.vibrate(60);
     document.getElementById("bars").style.display="block"
     document.getElementById("times").style.display="none"
   }
    </script>
    <script type="text/javascript" charset="utf-8">
    document.getElementById('container'). style.display='none';
setTimeout(function () {
$('.loading_page ').fadeToggle();
document.getElementById('container'). style.display='block'
}, 1000); 
