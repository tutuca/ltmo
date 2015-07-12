var $ = require('jquery'),
    utils = require('./utils');

$(function () {
    'use strict';
    var hash = window.location.hash;
    if (hash) {
        $(window).scrollTop($(hash).offset().top - 55);
    }

    $('.ui-autocomplete-input').on('autocompleteopen', function () {
        var autocomplete = $(this).data('autocomplete'),
            menu = autocomplete.menu;
        menu.activate($.Event({ type: 'mouseenter' }), menu.element.children().first());
    });
    $('#id_tags').on('keydown', function (event) {
        // don't navigate away from the field on tab when selecting an item
        if (event.keyCode === $.ui.keyCode.TAB &&
            $(this).data('autocomplete').menu.active) {
            event.preventDefault();
        }
    }).autocomplete({
        source: function (request, response) {
            $.getJSON('/tags/', {
                tag_name: utils.extractLast(request.term)
            }, response);
        },
        search: function () {
            var term = utils.extractLast(this.value);
            if (term.length < 2) {
                return false;
            }
        },
        focus: function () {
            return false;
        },
        select: function (event, ui) {
            event.preventDefault();
            var terms = split(this.value);
            terms.pop();
            terms.push(ui.item.value);
            terms.push('');
            this.value = terms.join('', '');
        }
    });
    $('.control').on('click', function (event) {
        event.preventDefault();
        var target = $(this).attr('href');
        $(target).toggle('blind', 300);
        if (target === '#leak-form') {
            window.setTimeout(function () {
                $('#id_description').focus();
                $('#leak-form').bind('keydown', function (event) {
                    if (event.keyCode === $.ui.keyCode.ESCAPE) {
                        $('#leak-form').hide('blind', 500)
                                       .unbind('keydown');
                    }
                });
            }, 400);
        }
    });
    utils.setLayout();
    window.setTimeout(function () {
        $('#messages .control').click();
    }, 1000);
});
