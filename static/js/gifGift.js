
$(document).ready(function(){
   
    $(".calendarCell").click(function(){
        if ($(this).hasClass('activeCell')){
    		var thisElem = $(this).attr("id").split('_');
    		id = thisElem[1];
    		//alert(id);
    		if ($(this).attr("visibleElement") == "date"){
    		  $("#img_" + id).removeClass( "hiddenElement" );
    		  $("#text_" + id).addClass( "hiddenElement" );
    		  $(this).attr("visibleElement", "image");
    		  
    		  var ajaxUrl = "./setCookie/" + id + "/yes";
    		  
    		  $.get( ajaxUrl);
    		}else{
    		  $("#img_" + id).addClass( "hiddenElement" );
    		  $("#text_" + id).removeClass( "hiddenElement" );
    		  $(this).attr("visibleElement", "date");
    		  var ajaxUrl = "./setCookie/" + id + "/no";
    		  
    		  $.get( ajaxUrl);
    		}
        }
    });	
    
    
     /* fix big screens */
    if ($( window ).height() > 1001){ //1102 // avant 880
        $("#outPopUpDiv").addClass("outPopUp");
    }
    
    $( window ).resize(function() {
        
        if ($( window ).height() > 1001){

            if (!$("#outPopUpDiv").hasClass('outPopUp')){
                $("#outPopUpDiv").addClass('outPopUp');
            }
        }else{
            $("#outPopUpDiv").removeClass('outPopUp');
        }
    });

    
});