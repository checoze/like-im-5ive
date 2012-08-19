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
var _gaq = [['_setAccount', 'UA-34096189-1'], ['_trackPageview']];
(function(d, t) {
  var g = d.createElement(t),
      s = d.getElementsByTagName(t)[0];
  g.src = '//www.google-analytics.com/ga.js';
  s.parentNode.insertBefore(g, s);
}(document, 'script'));

// iOS-Orientationchange-Fix
(function(a){function m(){d.setAttribute("content",g),h=!0}function n(){d.setAttribute("content",f),h=!1}function o(b){l=b.accelerationIncludingGravity,i=Math.abs(l.x),j=Math.abs(l.y),k=Math.abs(l.z),(!a.orientation||a.orientation===180)&&(i>7||(k>6&&j<8||k<8&&j>6)&&i>5)?h&&n():h||m()}var b=navigator.userAgent;if(!(/iPhone|iPad|iPod/.test(navigator.platform)&&/OS [1-5]_[0-9_]* like Mac OS X/i.test(b)&&b.indexOf("AppleWebKit")>-1))return;var c=a.document;if(!c.querySelector)return;var d=c.querySelector("meta[name=viewport]"),e=d&&d.getAttribute("content"),f=e+",maximum-scale=1",g=e+",maximum-scale=10",h=!0,i,j,k,l;if(!d)return;a.addEventListener("orientationchange",m,!1),a.addEventListener("devicemotion",o,!1)})(this); 