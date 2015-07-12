function viewport() {
    var e = window,
        a = 'inner';
    if (!('innerWidth' in window)) {
        a = 'client';
        e = document.documentElement || document.body;
    }
    return { width : e[a + 'Width'], height : e[a + 'Height']};
}

function setLayout() {
    var vp = viewport(),
        padding, visible_height, visible_width,
        main_img, old_img_width, new_img_width, width_delta;

    padding = $('header').height() * 7;
    visible_height = vp.height - padding;
    visible_width = $('#main article').width();
    main_img = $('article img')[0];
    if (main_img) {
        fit(main_img, false, 15);
    }
}
function split(val) {
    return val.split(/,\s*/);
}
function extractLast(term) {
    return split(term).pop();
}


function fit(selector, to, padding){
    var visible_height, visible_width,
        old_height, old_width,
        delta, landscape;
    padding = padding || 0;
    if (to) {
        visible_height = $(to).height() - padding;
        visible_width = $(to).width() - padding;
    } else {
        var vp = viewport();
        visible_height = vp.height - padding;
        visible_width = vp.width - padding;

    }
    $(selector).each(function() {
        var $el = $(this);
        old_width = $el.width();
        old_height = $el.height();
        landscape = old_width > old_height;
        if (landscape) {
            $el.css({
                width: Math.floor(visible_height / old_height * old_width),
                height: 'auto'
            });
        } else {
            $el.css({
                height: visible_height,
                width: 'auto'
            });
        }
        /* delta = (visible_width - $el.width())/2;
        $(this).css('margin-left', delta); */
    });

}

module.exports.fit = fit;
module.exports.viewport = viewport;
module.exports.setLayout = setLayout;
module.exports.extractLast = extractLast;