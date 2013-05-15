
(function($) {


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



    $(document).ready(function($) {
        // you can now use jquery / javascript here...


        //validacion en el admin para la condicion del terreno.
        $('#id_forma_terr').change(function() {
            forma_terreno = $('#id_forma_terr').val();
            if (forma_terreno == 1){
                opciones=["id_pend_terr","id_l_m_ladera","id_pend_talud", "id_sep_talud"];
                desactivar_opciones(opciones);
            }
            else{
                if (forma_terreno == 2){
                    opciones=["id_pend_talud", "id_sep_talud"];
                    desactivar_opciones(opciones);
                    opciones=["id_pend_terr","id_l_m_ladera"];
                    activar_opciones(opciones);
                }
                else{
                    opciones=["id_pend_terr","id_l_m_ladera"];
                    desactivar_opciones(opciones);
                    opciones=["id_pend_talud","id_sep_talud"];
                    activar_opciones(opciones);
                }
            }
        });



    });
})(django.jQuery);










