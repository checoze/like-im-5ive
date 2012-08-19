/* ===========================================================
 * Like I'm 5ive
 * http://www.likeim5ive.com
 * ===========================================================
 * 
 * Author: Garrett Pennington
 * ========================================================== */

$(function(){
    
    function vote(elem, direction){
		$.ajax({
			type: "POST",
			url: "/vote/" + $(elem).attr('data-type') + "/" + $(elem).attr('data-id') + "/",
			dataType: 'json',
			data: "csrfmiddlewaretoken=" + csrf_token + "&direction=" + direction,
			success: function(data){
			    if ( data.success ){
			        //alert( $(elem).attr('class'));
			        //alert(data.value);
			        $(elem).siblings('.lif-score').text("Score: " + data.value)
			    }
			    else{
			        console.log('Unable to vote')
			    }
			},
			error: function(){
			    console.log('Unable to vote')
            }
	    });
    }

    //Vote
    $('.lif-upvote').click(function(event){
        event.preventDefault();
        vote( $(this), 'up' );
    });
    $('.lif-downvote').click(function(event){
        event.preventDefault();
        vote( $(this), 'down' );
    });
    
    
    $('.dropdown-menu').click(function(e){
        e.stopPropagation();
    });
});

// Google Analtyics
/*
var _gaq = [['_setAccount', 'UA-34096189-1'], ['_trackPageview']];
(function(d, t) {
  var g = d.createElement(t),
      s = d.getElementsByTagName(t)[0];
  g.src = '//www.google-analytics.com/ga.js';
  s.parentNode.insertBefore(g, s);
}(document, 'script'));
*/