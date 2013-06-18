
(function($) {




    function desaparecer_opciones (opciones){



        for (i=0;i<opciones.length;i++)
        {

            $('.'+opciones[i]).hide();
            $('#'+opciones[i]).hide();


        }

    }

    function aparecer_opciones (opciones){


        for (i=0;i<opciones.length;i++)
        {

            $('.'+opciones[i]).show();
            $('#'+opciones[i]).show();

        }

    }




    $(document).ready(function($) {

        opciones=["field-anio_inici", "field-anio_fin"];
        desaparecer_opciones(opciones);
        opciones=["field-periodo"];
        aparecer_opciones(opciones);

        // Para el manejo de los distintos periodos
        $('#id_periodo').change(function() {
            periodo = $('#id_periodo').val();
            opciones=["field-anio_inici", "field-anio_fin"];
            desaparecer_opciones(opciones);
            if (periodo == 1){


                opciones=["field-anio_inici"];
                aparecer_opciones(opciones);

            }
            else{
                if (periodo == 2){


                    opciones=["field-anio_inici", "field-anio_fin",];
                    aparecer_opciones(opciones);

                }
                if (periodo == 3){


                    opciones=[ "field-anio_fin",];
                    aparecer_opciones(opciones);

                }
                else{


                    opciones=["field-periodo"];
                    aparecer_opciones(opciones);

                }
            }
        });


        $('#id_anio_construccion_set-0-anio').change(function() {


            $.get('/periodo_given_year/'+this.value, function(data) {

                id_periodo = data['id'];

                 $('#id_anio_construccion_set-0-periodo').children('option').each(function () {

                    if ($(this).val() == id_periodo){

                        $(this).attr('selected','selected');

                    }

                });


            });



        });

        $('#id_anio_construccion_set-0-periodo').change(function() {

            value = $(this).children('option').filter(":selected").val();

            $.get('/year_given_periodo/'+value, function(data) {

                year= data['year'];
               
                $('#id_anio_construccion_set-0-anio').val(year);


            });

        });





    });




})(django.jQuery);










