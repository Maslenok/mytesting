/* Author: 

*/





	 jQuery(document).ready(function(){
				$('input[placeholder], textarea[placeholder]').placeholder();
				
				// Change title type, overlay opening speed and opacity
			$(".fancybox").fancybox({
				helpers: {
					title : {
						type : 'outside'
					},
					overlay : {
						
						opacity : 0.70
					}
				}
			});
			
			 $("#accordion").accordion({
				autoHeight: false,  
				active: 0,
				collapsible:true
			  });
			  $(".carousel").jCarouselLite({
					btnPrev: ".prev",
					btnNext: ".next",
					visible: 7,
					speed:700,
					circular: true
				});

  
      $('.table_list').each(function() {
          $(this).parents().find(".pay_system a").click(function() {      
              $('.pay_system .pay_system__block').hide(); 
             $(this).parents('.pay_system').find(".pay_system__block").show();         
        });
      });
      $('.table_list').each(function() {
          $(this).parents().find(".pay_system__block__close").click(function() {      
          
             $(this).parents('.pay_system').find(".pay_system__block").hide();         
        });
      });
	});
	
$(function() {
 if ($('.time_fixed').length != 0) {
		var offset = $(".time_fixed").offset();
		var topPadding = 15;
		$(window).scroll(function() {
			if ($(window).scrollTop() > offset.top) {
				$(".time_fixed").stop().animate({marginTop: $(window).scrollTop() - offset.top + topPadding});
			}
			else {$(".time_fixed").stop().animate({marginTop: 0});};});
		} 
		else {
   
		}
	});	
	
$(function() {
		
/** tabs **/		
		$(".tabs").tabs().addClass('ui-tabs-vertical ui-helper-clearfix');
		$(".tabs ul.shadetabs li").removeClass('ui-corner-top').addClass('ui-corner-left');
		
	//information	
		//$(".tabs_information").tabs().addClass('ui-tabs-vertical ui-helper-clearfix');
		$(".tabs_information ul.shadetabs li").removeClass('ui-corner-top').addClass('ui-corner-left');
		
		
/** Slider **/ 
		$('.slider-content').cycle({
		timeout: 9000,
		pager:'.pager'
	});	

});




/** ScrollbarY **/ 
$(window).load(function() {
	mCustomScrollbars();
});

function mCustomScrollbars(){
	/* 
	malihu custom scrollbar function parameters: 
	1) scroll type (values: "vertical" or "horizontal")
	2) scroll easing amount (0 for no easing) 
	3) scroll easing type 
	4) extra bottom scrolling space for vertical scroll type only (minimum value: 1)
	5) scrollbar height/width adjustment (values: "auto" or "fixed")
	6) mouse-wheel support (values: "yes" or "no")
	7) scrolling via buttons support (values: "yes" or "no")
	8) buttons scrolling speed (values: 1-20, 1 being the slowest)
	*/
	if ($('#scrollbarY').length != 0) {
	$("#scrollbarY").mCustomScrollbar("vertical",200,"easeOutCirc",1.25,"fixed","yes","no",0); 
}
else{}
}

/* function to fix the -10000 pixel limit of jquery.animate */
$.fx.prototype.cur = function(){
    if ( this.elem[this.prop] != null && (!this.elem.style || this.elem.style[this.prop] == null) ) {
      return this.elem[ this.prop ];
    }
    var r = parseFloat( jQuery.css( this.elem, this.prop ) );
    return typeof r == 'undefined' ? 0 : r;
}

/* function to load new content dynamically */
function LoadNewContent(id,file){
	$("#"+id+" .customScrollBox .content").load(file,function(){
		mCustomScrollbars();
	});
}



  $(function(){	
      $("input[type='radio'], input[type='checkbox'],  input[type='text']").click(function() {
		$(this).parents("ol > li").css( "background-color","#F1F6F9" );
	});
	$(function(){	
      $(".passed_test input[type='radio'], .passed_test input[type='checkbox'], .passed_test input[type='text']").attr("disabled","disabled");
      $(".passed_test a.graf").each(function(){
		$(this).removeAttr("href");
		$(this).removeClass("fancybox");
		
	  });
	  
	});
	
	
	//.index( $(this)
	
  var color_bg;
  var arrColor = ["#7eb7f9", "#6a9edb", "#34abea", "#3f7cc3", "#28749E", "#205b7c", "#1b4e6a", "#329414", "#da60e5", "#e59560"]; 
  $('.table_1 label ').live('click', function(){
	var index_tr = $(this).parent().parent().index() ;
	var index_td = $(this).parent().index() ;
	var count_column = ($(this).parents('tr').find('td')).length;
	var count_rows = ($(this).parents('tbody').find('tr')).length;
	var who_checked = $(this).parent().attr('class');
	var where_checked = $(this).parents('tbody');
	
	 $(this).parents('li').find('ul.test li').removeAttr('style');


	 for(var i=0; i<count_rows; i++) 
	  {
		$(this).parents('tbody').find('tr').eq(i).find('td').eq(index_td).find('label').css('background', '#E3F1F9');
		$(this).parents('tbody').find('tr').eq(i).find('td').eq(index_td).find('label input').attr('checked', false);
	 }

	$(this).parents('tr').find('td input').attr('checked', false);
	$(this).parents('tr').find('td label').css('background', '#E3F1F9');
	$(this).find('input').attr('checked', 'checked');
	$(this).css('background', arrColor[index_tr]);

	for(var i=0; i<count_rows; i++) 
	  {
	 	$($(this).parents('tbody').find('tr').eq(i)).find('td').each(function()
			{
				if($(this).find('label input').attr("checked") == "checked")
					{
						j = $(this).index();
						where_checked.parents('li').find('ul.test .left li').eq(i-1).css( 'background-color', arrColor[i]);
						where_checked.parents('li').find('ul.test .right li').eq(j-1).css( 'background-color', arrColor[i]);
						//console.debug(where_checked.parents('li').find('ul.test .left li').eq(i-1));
					}					
			});
	  }
	
	
	



  }); // END $('.table_1 label').click(function()

  
  }); // END $(function(){

function secondsToHms(d) {
    d = Number(d);
    var h = Math.floor(d / 3600);
    var m = Math.floor(d % 3600 / 60);
    var s = Math.floor(d % 3600 % 60);
    return ((h > 0 ? h + ":" : "") + (m > 0 ? (h > 0 && m < 10 ? "0" : "0") + m + ":" : "00:") + (s < 10 ? "0" : "") + s);
}

function setAnswer(theme_id,question_id,question_count,question_type)
	{	
		var is_present_answer = 0;
				
		if(question_type==1 || question_type==2){
			var answer_count = 0;
			for (i=1;i<=8;i++)
			{
				var input_id = 'test_'+question_id+'_'+i;
				if(document.getElementById(input_id)){	
						if(document.getElementById(input_id).checked)answer_count++;	
				}				
			}
			if(answer_count>0)is_present_answer=1;	
		}
		else if(question_type==4 || question_type==5){
			        var input_id = 'test_'+question_id;
				    if(document.getElementById(input_id)){	
						if(document.getElementById(input_id).value!="")is_present_answer=1;	
				    }			
				    if(question_type==5){
				    	if(!checkNumeric(document.getElementById(input_id).value)){
				    		alert('Введіть числове значення!');
				    	}
				    }
		}
		if(question_type==3 || question_type==6){
			var answer_count = 0;
			for (i=1;i<=8;i++)
			{
				for (k=1;k<=8;k++){
					var input_id = 'r_'+question_id+'_'+i+'_'+k;
					if(document.getElementById(input_id)){	
							if(document.getElementById(input_id).checked)answer_count++;	
					}					
				}
				
			}
			if(answer_count>0)is_present_answer=1;			
		}
		
		//alert('/theme/setanswer?question_id='+question_id.toString()+'&theme_id='+theme_id.toString()+'&is_answer='+is_present_answer);
	    $.ajax({	
	        type:    'GET',	
	        dataType : "json",	
	        url:     '/theme/setanswer?question_id='+question_id.toString()+'&theme_id='+theme_id.toString()+'&is_answer='+is_present_answer,	
	        success:	
	            function(data)	
	            {         		
				    if(document.getElementById('test_questions')){	
						document.getElementById('test_questions').innerHTML = data+'/'+question_count;	
				    }	
				    return;	
	            }	
	    });
}
$(document).ready(function(){
	
	setTimeout(function(){
		
	$(".block_mybook").append("<div class='shadowBlock'></div>");
	});
	
	
});

 $(function() {
        $('#mybook').booklet({
		 auto: true,
		delay: 2000
		});
    });

/*  for validation form */
function validateForm(e,div_id) {

var f = '#' + $(e).attr('id');
var elem = $(f + " input, " + f + ' textarea,' + f + ' select,');


var err = "";

for (var i=0; i<elem.length; i++) {

    if ($(elem[i]).hasClass("required") && $(elem[i]).get(0).tagName == 'INPUT' && $(elem[i]).val() == "")
    {
      err += "<li><strong>"+ $(elem[i]).attr("placeholder") +"</strong> - обов'язкові для заповнення</li>";
	  $(elem[i].parentNode).addClass('error');
    }
	else
	{
		  $(elem[i].parentNode).removeClass('error');		
		  $(elem[i].parentNode).addClass('ok');
	}
    if ($(elem[i]).hasClass("required") && $(elem[i]).get(0).tagName == 'TEXTAREA' && $(elem[i]).val() == "")
    {
      err += "<li><strong>"+ $(elem[i]).attr("placeholder") +"</strong> - обов'язкові для заповнення</li>";
	  $(elem[i].parentNode).addClass('error');
    }
	else
	{
		
		  $(elem[i].parentNode).addClass('ok');
	}
	
	

	
		

	if ($(elem[i]).hasClass("email") && $(elem[i]).val() !== "" )
    {
		if (!checkEmail($(elem[i]).val()) )
		{
		  err += "<li><strong>"+ $(elem[i]).attr("placeholder") +"</strong> - повинен бути дійсний</li>";
		  $(elem[i].parentNode).addClass('error');
		  $(elem[i].parentNode).removeClass('ok');
		}
		else
		{
			  $(elem[i].parentNode).addClass('ok');
		}

	}

	if ($(elem[i]).hasClass("required") && $(elem[i]).get(0).tagName == 'SELECT' && (elem[i].selectedIndex <= 0))
    {
      err += "<li><strong>"+ $(elem[i]).attr("placeholder") +"</strong> - обов'язково потрібно вибрати</li>";
	  $(elem[i].parentNode).addClass('error');
	  $(elem[i].parentNode).removeClass('ok');

	}


	if ($(elem[i]).hasClass("phone") && $(elem[i]).val() !== "" )
    {
		if (!checkPhone($(elem[i]).val()) )
		{
		  err += "<li><strong>"+ $(elem[i]).attr("placeholder") +"</strong> - повинен бути дійсний</li>";
		  $(elem[i].parentNode).addClass('error');
		  $(elem[i].parentNode).removeClass('ok');
		}
		else
		{
			  $(elem[i].parentNode).addClass('ok');
		}

	}

  }
  
  if (err != "") {
    err = "<span>Ви забули або не правильно ввесли одне або кілька полів. Будь ласка, виправте ці помилки:</span><ul>" + err + "</ul>";
    $("#"+div_id).html(err).addClass("visible");
    return false;
  }
  else return true;
}

/* --========================--*/
function checkEmail(e)
{
 ok = "1234567890qwertyuiop[]asdfghjklzxcvbnm.@-_QWERTYUIOPASDFGHJKLZXCVBNM";

 for(i=0; i < e.length ;i++)
  if(ok.indexOf(e.charAt(i))<0)
   return (false);

 if (document.images)
 {
  re = /(@.*@)|(\.\.)|(^\.)|(^@)|(@$)|(\.$)|(@\.)/;
  re_two = /^.+\@(\[?)[a-zA-Z0-9\-\.]+\.([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;
  if (!e.match(re) && e.match(re_two))
   return true;
  else
   return false;

 }
 return true;

}

function checkNumeric(str)
{
    str = alltrim(str);
    return /^[-+]?\d+(\.\d+)?$/.test(str);
}

function checkPhone(e)
{
	if(e.match(/^\+?[0-9\- ]{5,}$/))
		return true
	else
   		return false;
}

function ltrim(str){
   return str.replace(/^\s+/, '');
}
function rtrim(str) {
  return str.replace(/\s+$/, '');
}
function alltrim(str) {
  return str.replace(/^\s+|\s+$/g, '');
}