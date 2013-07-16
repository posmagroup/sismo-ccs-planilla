(function($) {




    $(document).ready(function(){



        $.get('/mapa/',function(data){



            $(data).insertAfter($("#calendarbox0"));


        });






    });



})(django.jQuery);
