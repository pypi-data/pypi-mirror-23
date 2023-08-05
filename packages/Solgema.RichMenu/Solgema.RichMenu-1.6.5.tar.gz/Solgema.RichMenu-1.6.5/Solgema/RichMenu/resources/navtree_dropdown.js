var delayHide;

jQuery.fn.extend({
  showRichMenu: function() {
    var tab = $(this);
    var smenu = $(this).children('.smenu').not('.smenu.always');;
    smenu.stop().clearQueue();
    tab.css('z-index', '300');
    tab.addClass('menuhover');
    smenu.animate({opacity: 1}, 100);
  },
  hideRichMenu: function() {
    var tab = $(this);
    var smenu = $(this).children('.smenu:visible').not('.smenu.always');;
    if (smenu.length>0){
      smenu.stop().clearQueue();
      tab.css('z-index', '200');
      smenu.animate({
        opacity: 0,
        }, 100, function() {
          tab.removeClass('menuhover');
      });
    } else {
      tab.removeClass('menuhover');
    }
  }
});

function hideMenus() {
  $("#portal-globalnav li").hideRichMenu();
}

function initRichMenu() {
  $("#portal-globalnav.hover li > .smenu").not('.smenu.always').css('opacity','0');
  $("#portal-globalnav.click li > .smenu").not('.smenu.always').css('opacity','0');
  $("#portal-globalnav.hover > li").on('mouseenter touchstart', function(event){
    if ($('.plone-navbar-toggle').is(":visible")) return;
    event.stopPropagation();
    $("#portal-globalnav").find('.menuhover').not($(this).parents()).not($(this)).hideRichMenu();
    $(this).showRichMenu();
    clearTimeout( delayHide );
  });
  $("#portal-globalnav.hover > li a").on('touch', function(event){
    if ($(this).parent().children().length == 1) return;
    event.preventDefault();
  });
  $("#portal-globalnav > li ul li").on('mouseenter touchstart', function(event){
    if ($('.plone-navbar-toggle').is(":visible")) return;
    event.stopPropagation();
    $("#portal-globalnav").find('.menuhover').not($(this).parents()).not($(this)).hideRichMenu();
    $(this).showRichMenu();
    clearTimeout( delayHide );
  });
  $("#portal-globalnav.hover").on('mouseleave touchend', function(event){
    if ($('.plone-navbar-toggle').is(":visible")) return;
    delayHide = setTimeout( hideMenus, 300);
  });
  $("#portal-globalnav.hover .menuPage li").on('mouseleave touchend', function(event){
    if ($('.plone-navbar-toggle').is(":visible")) return;
    $(this).hideRichMenu();
  });
  $("#portal-globalnav > li > a").on('click touchstart', function(event){
    if (!$('.plone-navbar-toggle').is(":visible") && !$("#portal-globalnav").hasClass('click')) return;
    if ($(this).parent().children().length == 1) return;
    event.preventDefault();
    event.stopPropagation();
    if (!$(this).parent().hasClass('menuhover')) {
        $("#portal-globalnav").find('.menuhover').not($(this).parents('li')).not($(this).parent()).hideRichMenu();
        $(this).parent().showRichMenu();
    } else {
        $(this).parent().hideRichMenu();
    }
  });
  $('html').click(function(event) {
    delayHide = setTimeout( hideMenus, 300);
  });
};

$(initRichMenu);
