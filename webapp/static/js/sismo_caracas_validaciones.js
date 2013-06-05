
(function($) {



    //$("div:contains('Información personal')").hide();

    function desactivar_opciones (opciones){


        for (i=0;i<opciones.length;i++)
        {

            $('#'+opciones[i]).attr('disabled','disabled');


        }

    }

    function activar_opciones (opciones){


        for (i=0;i<opciones.length;i++)
        {

            $('#'+opciones[i]).removeAttr('disabled');

        }

    }



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
        // you can now use jquery / javascript here...



        $('.inline-group h2').each(function () {


            val = $(this).html().toLowerCase();

            val2  = val[0].toUpperCase() + val.slice(1);

            $(this).html(val2);
           





        });

















        $("fieldset:contains('Información personal')").hide();




        //validacion en el admin para la condicion del terreno.
        $('#id_forma_terr').change(function() {
            forma_terreno = $('#id_forma_terr').val();
            if (forma_terreno == 1){
                opciones=["id_pend_terr","id_l_m_ladera","id_pend_talud", "id_sep_talud"];
                desaparecer_opciones(opciones);
            }
            else{
                if (forma_terreno == 2){
                    opciones=["id_pend_talud", "id_sep_talud"];
                    desaparecer_opciones(opciones);
                    opciones=["id_pend_terr","id_l_m_ladera"];
                    aparecer_opciones(opciones);
                }
                else{
                    opciones=["id_pend_terr","id_l_m_ladera"];
                    desaparecer_opciones(opciones);
                    opciones=["id_pend_talud","id_sep_talud"];
                    aparecer_opciones(opciones);
                }
            }
        });



        //validacion en el admin para el periodo de construccion.
        opciones=["field-anio_inici", "field-anio_fin", "field-fecha_infer"];
        desaparecer_opciones(opciones);
        opciones=["field-periodo"];
        aparecer_opciones(opciones);
        $('#id_periodo').change(function() {
            periodo = $('#id_periodo').val();
            opciones=["field-anio_inici", "field-anio_fin", "field-fecha_infer"];
            desaparecer_opciones(opciones);
            if (periodo == 1){

                opciones=["field-anio_inici", "field-anio_fin", "field-fecha_infer"];
                desaparecer_opciones(opciones);
                opciones=["field-anio_inici"];
                aparecer_opciones(opciones);

            }
            else{
                if (periodo == 2){

                    opciones=["field-anio_inici", "field-anio_fin", "field-fecha_infer"];
                    desaparecer_opciones(opciones);
                    opciones=["field-anio_inici", "field-anio_fin",];
                    aparecer_opciones(opciones);

                }
                if (periodo == 3){

                    opciones=["field-anio_inici", "field-anio_fin", "field-fecha_infer"];
                    desaparecer_opciones(opciones);
                    opciones=[ "field-anio_fin",];
                    aparecer_opciones(opciones);

                }
                else{

                }
            }
        });


        //validacion en el admin para el periodo de construccion.
        opciones=["field-anio_inici", "field-anio_fin", "field-fecha_infer"];
        desaparecer_opciones(opciones);
        $('#id_periodo_construccion_set-0-periodo').change(function() {

            opciones=["field-anio_inici", "field-anio_fin", "field-fecha_infer"];
            desaparecer_opciones(opciones);
            periodo = $('#id_periodo_construccion_set-0-periodo').val();
            if (periodo == 1){

                opciones=["field-anio_inici", "field-anio_fin", "field-fecha_infer"];
                desaparecer_opciones(opciones);
                opciones=["field-anio_inici"];
                aparecer_opciones(opciones);

            }
            else{
                if (periodo == 2){

                    opciones=["field-anio_inici", "field-anio_fin", "field-fecha_infer"];
                    desaparecer_opciones(opciones);
                    opciones=["field-anio_inici", "field-anio_fin",];
                    aparecer_opciones(opciones);

                }
                if (periodo == 3){

                    opciones=["field-anio_inici", "field-anio_fin", "field-fecha_infer"];
                    desaparecer_opciones(opciones);
                    opciones=[ "field-anio_fin",];
                    aparecer_opciones(opciones);

                }
                else{

                }
            }
        });




        //validacion en el admin para la condicion del terreno.

        opciones=["field-pend_terr","field-l_m_ladera","field-pend_talud", "field-sep_talud"];
        desaparecer_opciones(opciones);
        $('#id_condicion_terreno_set-0-forma_terr').change(function() {
            forma_terreno = $('#id_condicion_terreno_set-0-forma_terr').val();
            if (forma_terreno == 1){
                opciones=["field-pend_terr","field-l_m_ladera","field-pend_talud", "field-sep_talud"];
                desaparecer_opciones(opciones);
            }
            else{
                if (forma_terreno == 2){

                    opciones=["field-pend_talud", "field-sep_talud"];
                    desaparecer_opciones(opciones);
                    opciones=["field-pend_terr","field-l_m_ladera"];
                    aparecer_opciones(opciones);
                }
                else{

                    opciones=["field-pend_terr","field-l_m_ladera"];
                    desaparecer_opciones(opciones);
                    opciones=["field-pend_talud", "field-sep_talud"];
                    aparecer_opciones(opciones);
                }
            }
        });
    });




})(django.jQuery);










