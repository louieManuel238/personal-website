(function($){
  $('#contact_form').ajaxForm({
            success: function(){
                    alert("Successfully Added");
                },
            error: function(msg){alert("ERROR IN UPLOADING FILE");}
        });
  $(function(){
    $('.sidenav').sidenav();
    $('.slider').slider();
  }); // end of document ready
})(jQuery); // end of jQuery name space
 