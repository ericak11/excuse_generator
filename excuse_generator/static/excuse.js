console.log('excuse.js loaded')
$( document ).ready(function(){
  $(".excuse_button").hover(
    function() {
      $( this ).addClass( "hover" );
    }, function() {
      $( this ).removeClass( "hover" );
    }
  );
});
