(function($) {
$( ".ui-autocomplete-input" ).live( "autocompleteopen", function() {
    var autocomplete = $( this ).data( "autocomplete" ),
        menu = autocomplete.menu;
    menu.activate( $.Event({ type: "mouseenter" }), menu.element.children().first() );
});
}( jQuery ));
function viewport(){
    e = window;
    a = 'inner';
    if ( !( 'innerWidth' in window ) ){
        a = 'client';
        e = document.documentElement || document.body;
    };
    return { width : e[ a+'Width' ] , height : e[ a+'Height' ] };
};  
function setLayout(){
    vp = viewport();
    padding = $('header').height() * 7;
    visible_height = vp.height - padding;
    visible_width = $('#main article').width();
    main_img = $('article img')[0];
    old_img_width = $('article img')[0].width;
    if (main_img) {
        new_img_width = (visible_width / old_img_width * visible_height) - padding;
        if (visible_height > main_img.height) {
                main_img.height = visible_height;
                main_img.width = new_img_width ;
        }
        width_delta = (visible_width - main_img.width)/2;
        $(main_img).css('margin-left', width_delta);
    }
};
$(function(){
    setLayout();
    var hash = window.location.hash;
    if (hash){
        $(window).scrollTop($(hash).offset().top-55);
    }
    
	function split( val ) {
		return val.split( /,\s*/ );
	}
	function extractLast( term ) {
		return split( term ).pop();
	}

    $('.control').click(function(){
        target = $(this).attr('href');
        $(target).toggle('blind', 300);
        if (target === '#leak-form'){
            window.setTimeout(function(){
                $('#id_description').focus();
                $('#leak-form').bind( "keydown", function(event) {
		                if ( event.keyCode === $.ui.keyCode.ESCAPE) {
			                $('#leak-form').hide('blind', 500)
			                               .unbind('keydown');
		                }
	                });

            },400)

        }
        return false;
        
    });
	$( "#id_tags" )
		.bind( "keydown", function( event ) {
		// don't navigate away from the field on tab when selecting an item
			if ( event.keyCode === $.ui.keyCode.TAB &&
					$( this ).data( "autocomplete" ).menu.active ) {
				event.preventDefault();
			}
		})
		.autocomplete({
			source: function( request, response ) {
				$.getJSON( "/tags/", {
					tag_name: extractLast( request.term )
				}, response );
			},
			search: function() {
				var term = extractLast( this.value );
				if ( term.length < 2 ) {
					return false;
				}
			},
			focus: function() {
				return false;
			},
			select: function( event, ui ) {
				var terms = split( this.value );
				terms.pop();
				terms.push( ui.item.value );
				terms.push( "" );
				this.value = terms.join( ", " );
				return false;
			}
		});
        window.setTimeout(function(){
            $('#messages .control').click()
            }, 1000);
})

