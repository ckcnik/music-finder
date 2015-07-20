(function($) {
	
	"use strict";
	
//
//
//	//Take Dimensions of Several Things
//	function adjustMents() {
//
//		var windowWidth =	$(window).width();
//		var windowHeight =	$(window).height();
//		var docHeight = $(document).height();
//
//		$('.preloader').css('width',windowWidth);
//		$('.preloader').css('height',windowHeight);
//
//	}
//
//
//	//Hide Loading Box (Preloader)
//	function handlePreloader() {
//		$('.preloader').delay(2000).fadeOut(500);
//	}
//
//
//	//Testimonial Slider One
//	function testiSliderOne() {
//		//Testimonial Slider one
//		$('.testimonials-one .slider').bxSlider({
//			adaptiveHeight: true,
//			auto:true,
//			controls: false,
//			mode: 'fade',
//			pause: 5000,
//			speed: 1000,
//			pagerCustom: '.testi-pager'
//		});
//	}
//
//
//	//Testimonial Slider Two
//	function testiSliderTwo() {
//		//Testimonial Slider Two
//		$('.testimonials-two .slider').bxSlider({
//			adaptiveHeight: true,
//			auto:true,
//			controls: false,
//			pause: 5000,
//			speed: 1000,
//			pager:true
//		});
//	}
//
//
//	//Browse Topics Slider
//	function browseTopicsSlider() {
//		$('.browse-topics .slider').owlCarousel({
//			loop:true,
//			autoplay:true,
//			autoplayTimeout:5000,
//			margin:30,
//			responsiveClass:true,
//			slideSpeed : 2000,
//			responsive:{
//				0:{
//					items:1,
//					nav:false
//				},
//				480:{
//					items:1,
//					nav:false
//				},
//				768:{
//					items:2,
//					nav:false
//				},
//				1024:{
//					items:3,
//					nav:false
//				},
//				1100:{
//					items:4,
//					nav:false,
//					loop:true
//				},1200:{
//					items:4,
//					nav:false,
//					loop:true
//				}
//			}
//		});
//	}
//
//
//	//Accordion
//	function Accordion() {
//		$(".accordion-box").on('click', '.accord-btn', function() {
//
//			if($(this).hasClass('active')!=true){
//			$('.accordion .accord-btn').removeClass('active');
//
//			}
//
//			if ($(this).next('.accord-content').is(':visible')){
//				$(this).removeClass('active');
//				$(this).next('.accord-content').slideUp(700);
//			}else{
//				$(this).addClass('active');
//				$('.accordion .accord-content').slideUp(700);
//				$(this).next('.accord-content').slideDown(700);
//			}
//		});
//	}
//
//
//	// Elements Animation
//	function elementsAnimations() {
//		$('.animated').appear(function(){
//			var el = $(this);
//			var anim = el.data('animation');
//			var animDelay = el.data('delay');
//			if (animDelay) {
//
//				setTimeout(function(){
//					el.addClass( anim + " in" );
//					el.removeClass('out');
//				}, animDelay);
//
//			}
//
//			else {
//				el.addClass( anim + " in" );
//				el.removeClass('out');
//			}
//		},{accY: -150});
//	}
//
//
//	// Milestones Counter
//	function milestonesCounter() {
//		$('.milestone.in').each(function() {
//
//			var $t = $(this),
//				n = $t.find(".stat-count").attr("data-stop"),
//				r = parseInt($t.find(".stat-count").attr("data-speed"), 10);
//
//			if (!$t.hasClass("counted")) {
//				$t.addClass("counted");
//				$({
//					countNum: $t.find(".stat-count").text()
//				}).animate({
//					countNum: n
//				}, {
//					duration: r,
//					easing: "linear",
//					step: function() {
//						$t.find(".stat-count").text(Math.floor(this.countNum));
//					},
//					complete: function() {
//						$t.find(".stat-count").text(this.countNum);
//					}
//				});
//			}
//
//		});
//	}
//
///* ==========================================================================
//   When document is ready, do
//   ========================================================================== */
//
//	$(document).ready(function() {
//		elementsAnimations();
//		adjustMents();
//		browseTopicsSlider();
//		testiSliderOne();
//		testiSliderTwo();
//		Accordion();
//
//
//	});
//
///* ==========================================================================
//   When the window is scrolled, do
//   ========================================================================== */
//
//	$(window).scroll(function() {
//		milestonesCounter();
//	});
//
//
//
///* ==========================================================================
//   When document is loading, do
//   ========================================================================== */
//
//	$(window).load(function() {
//
//		handlePreloader();
//
//	});
//
//
///* ==========================================================================
//   When the window is resized, do
//   ========================================================================== */
//
//	$(window).resize(function() {
//
//	});
//

	//$('.table').height($(window).height());
    //$(window).resize(function () {
    //    $('.table').height($(window).height());
    //});


})(window.jQuery);
