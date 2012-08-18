/* ===========================================================
 * Like I'm 5ive
 * http://www.likeim5ive.com
 * ===========================================================
 * 
 * Author: Garrett Pennington
 * ========================================================== */

$(document).ready( function(){

    function vote(elem, direction){
		$.ajax({
			type: "POST",
			url: "/vote/" + $(elem).attr('data-type') + "/" + $(elem).attr('data-id') + "/",
			dataType: 'json',
			data: "csrfmiddlewaretoken=" + csrf_token,
			success: function(data){
			    alert('success!');
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

    
});
