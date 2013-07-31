
(function($) {

    /*
     Funcion que recibe un arreglo de ids
     o class de y oculta los htmls asociados
     a los mismos
     */
    function desaparecer_opciones (opciones){


        for (i=0;i<opciones.length;i++)
        {

            $('.'+opciones[i]).hide();
            $('#'+opciones[i]).hide();


        }

    }

    /*
     Funcion que recibe un arreglo de ids
     o class de y muestra los htmls asociados
     a los mismos

     */
    function aparecer_opciones (opciones){


        for (i=0;i<opciones.length;i++)
        {

            $('.'+opciones[i]).show();
            $('#'+opciones[i]).show();

        }

    }


    $(document).ready(function($) {

        // Agrega el Label fecha inferida al Dom
        $('<label id="fecha_inferida" class="required" style="margin-left: 55%"> Fecha Inferida </label>').insertAfter($("#id_anio_construccion_set-0-anio"));

        // Definiendo el arreglo de campos ocultos inicialmente
        opciones=["fecha_inferida","field-anio_inici", "field-anio_fin","field-fecha_inf"];

        //Ocultando los campos
        desaparecer_opciones(opciones);

        // Muestra el div con la clase field-periodo pues al ocultar los demas tambien se
        // oculto este porque no tiene un id y comparte una de las clases que se ocultaron
        opciones=["field-periodo"];
        aparecer_opciones(opciones);

        //Detecta los cambios en el combo del periodo para saber cuantos campos debe mostrar.
        $('#id_periodo').change(function() {

            // Obtengo el valor seleccionado
            periodo = $('#id_periodo').val();

            // Desaparezco los campos para "resetear" las opciones
            opciones=["field-anio_inici", "field-anio_fin"];
            desaparecer_opciones(opciones);


            if (periodo == 1){ // Si selecciono la opcion Antes de

                opciones=["field-anio_inici"];
                aparecer_opciones(opciones);

            }
            else{
                if (periodo == 2){  // Si selecciono la opcion Entre


                    opciones=["field-anio_inici", "field-anio_fin",];
                    aparecer_opciones(opciones);

                }
                if (periodo == 3){ // Si selecciono la opcion Despues de


                    opciones=[ "field-anio_fin",];
                    aparecer_opciones(opciones);

                }
                else{ // Si selecciono --------

                    opciones=["field-periodo"];
                    aparecer_opciones(opciones);

                }
            }
        });

        // Detecta los cambios en el input de año del admin de Inspeccion
        $('#id_anio_construccion_set-0-anio').change(function() {

            // Llamada al view que devuelve el periodo dado el año
            $.get('/periodo_given_year/'+this.value, function(data) {

                id_periodo = data['id'];

                 $('#id_anio_construccion_set-0-periodo').children('option').each(function () {

                    if ($(this).val() == id_periodo){
                        $(this).attr('selected','selected');
                        // Desactiva el check que le indicara al modelo si es fecha inferida.
                        $('input[name=anio_construccion_set-0-fecha_inf]').attr('checked', false);
                        // Oculta los campos que indican que la fecha es inferida
                        opciones=["field-fecha_inf","fecha_inferida"];
                        desaparecer_opciones(opciones);



                    }

                });


            });



        });

        // Detecta los cambios en el input de año del admin de Inspeccion
        $('#id_anio_construccion_set-0-periodo').change(function() {

            // Obtengo el valor seleccionado
            value = $(this).children('option').filter(":selected").val();

            // Llamada al view que devuelve elaño dado el periodo
            $.get('/year_given_periodo/'+value, function(data) {

                year= data['year'];

                $('#id_anio_construccion_set-0-anio').val(year);
                // Activa el check que le indicara al modelo si es fecha inferida.
                $('input[name=anio_construccion_set-0-fecha_inf]').attr('checked', true);
                $('input[name=anio_construccion_set-0-fecha_inf]').attr('disable', 'disable');
//              // Muestra los campos que indican que la fecha es inferida
                opciones=["fecha_inferida"];
                aparecer_opciones(opciones);

            });

        });


    });




})(django.jQuery);










