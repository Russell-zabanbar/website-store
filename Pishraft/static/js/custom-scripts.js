$(document).ready(function () {
    'use strict';

       //===== Page loader =====// 
        setTimeout(function () {
            $('#loader-page').fadeOut(function () {
            $(this).remove();
            });
        }, 1000);
        //===== Menu Nav =====//
        $('.navbar-menu-toggler').on('click', function(){
            // Slide and scale content
            $('.main-content').toggleClass('nav-active');
            $(".sidebar-nav").toggleClass('nav-active');
            $(".sidebar-filter").toggleClass('d-block bounceinup');
        });
        //===== Filter-card =====//
        $('.filtercard-toggle').on('click', function(){
        // Slide and scale content
        $(".card-filter").toggleClass('d-block bounceinup');
    });
          //===== Main Slider =====//
         $('.main-slider').owlCarousel({
            items:1,
            margin:30,
            stagePadding:0,
            smartSpeed:450,
            loop: true,
            dots: true,
        });
        
         //===== Featured Slider =====//
         $('.featured-products-area').owlCarousel({
            items: 3,
            margin: 15,
            loop: true,
            autoplay: true,
            smartSpeed: 800,
            autoplayTimeout: 5000,
            dots: true,
            nav: false,
            responsive: {
                1400: {
                    items: 5,
                },
                992: {
                    items: 5,
                },
                768: {
                    items: 4,
                },
                480: {
                    items: 3,
                },
            },
        });
        //===== Blog Related Slider =====//
        $('.blog-post-media').owlCarousel({
        items: 3,
        margin: 15,
        loop: true,
        autoplay: true,
        smartSpeed: 800,
        autoplayTimeout: 5000,
        dots: true,
        nav: false,
        responsive: {
            1400: {
                items: 5,
            },
            992: {
                items: 5,
            },
            768: {
                items: 4,
            },
            480: {
                items: 4,
            },
        },
    });
        //===== Product Details Slider =====//
        $('.product-details-slider').owlCarousel({
            stagePadding: 0,
            items: 1,
            margin: 10,
            loop: true,
            nav: true,
            autoplay: false,
            smartSpeed: 800,
            dots: false,
            navText: [('<i class="fa fa-angle-right"></i>'), ('<i class="fa fa-angle-left"></i>')]
        });
       //===== Product Quantity Button =====//
        $('.minus-btn').on('click', function (e) {
            e.preventDefault();
            var numProduct = Number($(this).next().val());
            if (numProduct > 1) $(this).next().val(numProduct - 1);
        });
        $('.plus-btn').on('click', function (e) {
            e.preventDefault();
            var numProduct = Number($(this).prev().val());
            $(this).prev().val(numProduct + 1);
        }); 
        //===== Favorite Button =====//
        $(".btn-favorite").on("click", function(e)
        {
            $(this).toggleClass("favorited") ;
        }) ;
    
         //===== Tabs Single Page =====//
         $(".checkout-tab").tabs({
            show: { effect: "slide", direction: "left", duration: 300, easing: "easeOutBack" } ,
            hide: { effect: "slide", direction: "right", duration: 300, easing: "easeInQuad" }
          });

         //===== Price Slider =====//
        $(function() {
        $( "#slider-range" ).slider({
            range: true,
            isRTL: true,
            min: 100,
            max: 1000,
            values: [ 0, 900 ],
            slide: function( event, ui ) {
            $( "#amount" ).val(  ui.values[ 0 ]  + " تومان " + " - " + ui.values[ 1 ] + " تومان " );
            }
        });
        $( "#amount" ).val(  $( "#slider-range" ).slider( "values", 0 )  + " تومان "  + " - "
             + $( "#slider-range" ).slider( "values", 1 ) + " تومان " );
        });

        //===== Check The Internet Connection =====//
        setInterval(function(){ 
            var ifConnected = window.navigator.onLine;
            if (!ifConnected) {
                document.getElementById("checkOnline").innerHTML = "Offline";
                $("#checkOnline").fadeIn(100);
                $(".alert").addClass("bg-danger");
            }else if(ifConnected){
                document.getElementById("checkOnline").innerHTML = "Online";
                $("#checkOnline").fadeOut(5000);
                $(".alert").removeClass("bg-danger");
                $(".alert").addClass("bg-success");
            }
            }, 1000);
        //===== Add To Cart Notification  =====//
        $('.basicSuccess').click(function () {
            Lobibox.notify('default', {
                icon: false,
                size: 'mini',
                position: 'top right',
                title: 'شما محصول را به سبد خرید خود اضافه کردید',
            });
        });  
    });