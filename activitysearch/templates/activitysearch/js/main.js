$(document).ready(function(){

    /*  hide-show mobile menu  */
    $("#menu_icon").click(function(){
        $("#nav_menu").toggleClass("show_menu");
        return false;
    });

		$('a#time').click(function() {
    		$(this).toggleClass("down");
  });

});
