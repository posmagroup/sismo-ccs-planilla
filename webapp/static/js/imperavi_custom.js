/**
 * Created by PyCharm.
 * User: aka-anto
 * Date: 23/11/12
 * Time: 11:59
 * To change this template use File | Settings | File Templates.
 */

$(document).ready(function() {

        $('#id_description').redactor({
        buttons:[ 'formatting', '|', 'bold', 'italic', 'deleted', '|',
            'unorderedlist', 'orderedlist', 'outdent', 'indent', '|',
             'table',  '|',
            'fontcolor', 'backcolor', '|', 'alignment', '|', 'horizontalrule']
    });

    $('#id_value').redactor({
        buttons:[ 'formatting', '|', 'bold', 'italic', 'deleted', '|',
            'unorderedlist', 'orderedlist', 'outdent', 'indent', '|',
            'table',  '|',
            'fontcolor', 'backcolor', '|', 'alignment', '|', 'horizontalrule']
    });


});

