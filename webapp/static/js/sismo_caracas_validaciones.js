
(function($) {

    var uso = 0;
    var adosamiento = 0;
    var adosamiento2 = 0;
    var ladera =0;
    var base =0;

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

    /*
     Funcion que recibe una referencia a un div,
     ya sea por id o por clase, revisa todos los
     checkbox del mismo y determina si al menos
     uno fue seleccionado. Tambien recibe el atributo
     excluir ya que el admin tiene sus propios checkboxs
     ocultos y se debe evitar validar esos.
     */
    function validar_al_menos_uno_seleccionado(referencia_div, excluir){

        counter = 0;
        zero_counter = 0;
        $(referencia_div).find('input[type=checkbox]').each(function () {
            name = this.name;
            if (name.search(excluir) ==-1){

                val = (this.checked ? "1" : "0");
                counter = counter +1;
                if (val==0){

                    zero_counter=zero_counter+1;

                }

            }

        });
        if (zero_counter==counter){

           return false;
        }
        else{

            return true;

        }
    }

    /*
     Funcion que valida que si selecciono la opcion
     'otro uso' se debe colocar el valor de ese otro uso.
     */
    function validar_uso_especifico(){

        if (uso==1){ // Uso se setea a uno cuando el usuario selecciona esta opcion

            val = $('#id_uso_set-0-otro_uso').val();

            if (val.length==0){
                error('Debe especificar el uso','#uso_set-0');
                return false;
            }
            else{

                return true;
            }
        }
        else{

            return true;
        }
    }

    /*
     Funcion que valida que si selecciono la opcion
     'adosamiento' se debe colocar el valor de la separacion del edificio
     */
    function validar_separacion_edificio(){

        if ((adosamiento==1) || (adosamiento2==1)){ //adosamiento y adosamiento2 se setean a uno cuando el usuario selecciona alguna de estas opciones

            val = $('#id_irregularidad_set-0-sep_edif').val();

            if (val==""){

                error('Debe especificar la separacion entre los edificios','#irregularidad_set-0');
                return false;
            }
            else{

                return true;
            }
        }
        else{

            return true;
        }
    }

    /*
     Funcion que valida que si selecciono la opcion
     'ladera' se debe colocar el valor de pendiente del terreno y localización del terreno
     */
    function validar_ladera(){

        if ((ladera==1)){ // ladera se setea a uno cuando el usuario selecciona esta opcion

            val = $('#id_condicion_terreno_set-0-pend_terr').children('option').filter(":selected").text();

            if (val=='---------'){

                error('Debe especificar la pendiente del terreno','#condicion_terreno_set-0');
                return false;
            }

            val = $('#id_condicion_terreno_set-0-l_m_ladera').children('option').filter(":selected").text();

            if (val=='---------'){

                error('Debe especificar la localización del terreno','#condicion_terreno_set-0');
                return false;
            }
            else{

                return true;
            }
        }
        else{

            return true;
        }
    }

    /*
     Funcion que valida que si selecciono la opcion
     'base' o 'cima' se debe colocar el valor de pendiente_talud y separación del talud
     */
    function validar_base(){

        if ((base==1)){ // ladera se setea a uno cuando el usuario selecciona esta opcion o selecciona cima



            val = $('#id_condicion_terreno_set-0-pend_talud').children('option').filter(":selected").text();


            if (val=='---------'){

                //alert('Debe especificar la pendiente del talud en la sección: Condición Terreno');
                error('Debe especificar la pendiente del talud','#condicion_terreno_set-0');

                return false;
            }

            val = $('#id_condicion_terreno_set-0-sep_talud').children('option').filter(":selected").text();

            if (val=='---------'){

                //alert('Debe especificar la separación del talud en la sección: Condición Terreno');
                error('Debe especificar la separación del talud','#condicion_terreno_set-0');
                return false;
            }
            else{

                return true;
            }
        }
        else{

            return true;
        }
    }

    /*
     Funcion que alinea las opciones de turno de ocupacion
     */
    function alinear_opciones(referencia_div, excluir){

        $(referencia_div).find('input[type=checkbox]').each(function () {


            name = $(this).closest("div").attr("class");

            if (name.search(excluir) ==-1){
                $(this).closest("div").css( "width", "80px" );

                if (name.search('field-t_o_manana')!=-1)
                {
                    $('<label for="id_capacidad_ocupacion_set-__prefix__-t_o_manana" class="required" style="left:-120px; width: 140px;">Turno Ocupación: </label>').insertBefore($(this).closest("div"));



                }

            }
        });

    }

    /*
     Funcion que toma un mensaje y lo inserta en el div referenciado con el formato html
     de error de django.
     */
    function error(error, referencia_div){

        mensaje ='<ul class="errorlist"><li>'+error+'</li></ul>';

        $(mensaje).insertBefore($(referencia_div));

    }

    function mostrar_foto(){

        if ($(".field-foto_facha").find("a").attr("href") != undefined){

            file_path = $(".field-foto_facha").find("a").attr("href").split('/');
            len =   $(".field-foto_facha").find("a").attr("href").split('/').length -1;


            $('<img src="/media/'+file_path[len]+'"/> <br/>').insertBefore($(".field-foto_facha").find("a"));

        }

    }

    function link_archivo(){

        if ($(".field-pla_esca").find("a").attr("href") != null){

            file_path = $(".field-pla_esca").find("a").attr("href").split('/');
            len =   $(".field-pla_esca").find("a").attr("href").split('/').length -1;
            $('<br> <p class="required file-upload">Descargar el archivo: <a href="/media/'+file_path[len]+'">'+file_path[len]+' </a> </p> <br/>').insertAfter($("#id_anexo_set-0-pla_esca"));

        }


    }

    function ocultar_campos_iniciales(){

        //oculta la sepracion de edificio
        $('#id_irregularidad_set-0-sep_edif').closest("div").hide();

        // oculta los campos de info personal en el admin de usuarios.
        $("fieldset:contains('Información personal')").hide();

        // oculta el campo donde se especifica el otro uso
        opciones=["field-otro_uso"];
        desaparecer_opciones(opciones);

        // oculta campos de la seccion de condicion de terreno
        opciones=["field-pend_terr","field-l_m_ladera","field-pend_talud", "field-sep_talud"];
        desaparecer_opciones(opciones);

    }

    function capitalizacion_titulos_inline(){

        $('.inline-group h2').each(function () {


            val = $(this).html().toLowerCase();

            val2  = val[0].toUpperCase() + val.slice(1);

            $(this).html(val2);


        });

    }

    function asteriscos_rojos_campos_requeridos(){

        $('.required').each(function () {

            val = $(this).html();

            val2  = val + ' <span style="color:red;">*</span> ' ;

            $(this).html(val2);

        });

    }



    $(document).ready(function($) {


        mostrar_foto();
        link_archivo();
        ocultar_campos_iniciales();
        alinear_opciones('#capacidad_ocupacion_set-group .inline-related','__prefix__');
        capitalizacion_titulos_inline();
        asteriscos_rojos_campos_requeridos();

        //validacion visual  en el admin para la condicion del terreno.
        $('#id_condicion_terreno_set-0-forma_terr').change(function() {
            forma_terreno = $('#id_condicion_terreno_set-0-forma_terr').val();

            if (forma_terreno == 1){
                opciones=["field-pend_terr","field-l_m_ladera","field-pend_talud", "field-sep_talud"];
                desaparecer_opciones(opciones);
            }

            if (forma_terreno == 2){

                opciones=["field-pend_talud", "field-sep_talud"];
                desaparecer_opciones(opciones);
                opciones=["field-pend_terr","field-l_m_ladera"];
                $('label[for="id_condicion_terreno_set-0-pend_terr"]').html('Pendiente del terreno: <span style="color:red;">*</span>');
                $('label[for="id_condicion_terreno_set-0-pend_terr"]').attr('class', 'required');
                $('label[for="id_condicion_terreno_set-0-l_m_ladera"]').html('Localizada sobre la mitad superior de la ladera: <span style="color:red;">*</span>');
                $('label[for="id_condicion_terreno_set-0-l_m_ladera"]').attr('class', 'required');
                aparecer_opciones(opciones);
            }
            if ((forma_terreno == 3) || (forma_terreno == 4) ){

                opciones=["field-pend_terr","field-l_m_ladera"];
                desaparecer_opciones(opciones);
                opciones=["field-pend_talud", "field-sep_talud"];
                $('label[for="id_condicion_terreno_set-0-pend_talud"]').html('Pendiente del talud: <span style="color:red;">*</span>');
                $('label[for="id_condicion_terreno_set-0-pend_talud"]').attr('class', 'required');
                $('label[for="id_condicion_terreno_set-0-sep_talud"]').html('Separación del talud: <span style="color:red;">*</span>');
                $('label[for="id_condicion_terreno_set-0-sep_talud"]').attr('class', 'required');
                aparecer_opciones(opciones);
            }


        });

        // Si se selecciona opción otro uso, aparece el campo para especificar el uso.
        $('#id_uso_set-0-u_otros').change(function() {

            val = (this.checked ? "1" : "0");
            uso =val;
            if (val==0){

                opciones=["field-otro_uso"];
                desaparecer_opciones(opciones);

            }
            if(val==1){

                opciones=["field-otro_uso"];
                aparecer_opciones(opciones);

            }

        });

        // Si se selecciona adosamiento aparece el campo para especificar la separacion del edificio.
        $('#id_irregularidad_set-0-ados_los_l').change(function() {
            val = (this.checked ? "1" : "0");
            adosamiento =val;
            if(val==1)
                $('#id_irregularidad_set-0-sep_edif').closest("div").show();
            if((adosamiento2==0) && (adosamiento==0))
                $('#id_irregularidad_set-0-sep_edif').closest("div").hide();

        });
        // Si se selecciona adosamiento aparece el campo para especificar la separacion del edificio.
        $('#id_irregularidad_set-0-ados_los_c').change(function() {
            val = (this.checked ? "1" : "0");
            adosamiento2 =val;
            if(val==1)
                $('#id_irregularidad_set-0-sep_edif').closest("div").show();
            if((adosamiento2==0) && (adosamiento==0))
                $('#id_irregularidad_set-0-sep_edif').closest("div").hide();

        });


        // Define que condicion de terreno se seleccionada para que luego sea validada
        $('#id_condicion_terreno_set-0-forma_terr').change(function() {

            value = $(this).children('option').filter(":selected").text();

            ladera =0;
            base = 0;
            if (value =='Ladera'){

                ladera =1;
            }

            if (value =='Base'){

                base =1;
            }

            if (value =='Cima'){

                base =1;
            }

        });


        // validacion  del combo de los tipos estructurales
        $("#tipo_estructural_set-group").find('input[type=checkbox]').change(function() {

            $('#id_tipo_estructural_set-0-tipo_predomi').find('option').remove() ;

            $("#tipo_estructural_set-group").find('input[type=checkbox]').each(function () {

                valor_check = (this.checked ? "1" : "0");

                id_check = this.id;


                if (valor_check==1){


                    label =$('label[for='+id_check+']').text();
                    if (label.indexOf("(PCA)") >= 0){

                        $('#id_tipo_estructural_set-0-tipo_predomi').append('<option value="1">1. PCA</option>');

                    }

                    if (label.indexOf("(PCAP)") >= 0){

                        $('#id_tipo_estructural_set-0-tipo_predomi').append('<option value="2">2. PCAP</option>');

                    }

                    if (label.indexOf("(MCA2D)") >= 0){

                        $('#id_tipo_estructural_set-0-tipo_predomi').append('<option value="3">3. MCA2D</option>');

                    }

                    if (label.indexOf("(MCA1D)") >= 0){

                        $('#id_tipo_estructural_set-0-tipo_predomi').append('<option value="4">4. MCA1D</option>');

                    }

                    if (label.indexOf("(PA)") >= 0){

                        $('#id_tipo_estructural_set-0-tipo_predomi').append('<option value="5">5. PA</option>');

                    }

                    if (label.indexOf("(PAPT)") >= 0){

                        $('#id_tipo_estructural_set-0-tipo_predomi').append('<option value="6">6. PAPT</option>');

                    }

                    if (label.indexOf("(PAD)") >= 0){

                        $('#id_tipo_estructural_set-0-tipo_predomi').append('<option value="7">7. PAD</option>');

                    }

                    if (label.indexOf("(PAC)") >= 0){

                        $('#id_tipo_estructural_set-0-tipo_predomi').append('<option value="8">8. PAC</option>');

                    }

                    if (label.indexOf("(PRE)") >= 0){

                        $('#id_tipo_estructural_set-0-tipo_predomi').append('<option value="9">9. PRE</option>');

                    }

                    if (label.indexOf("(MMC)") >= 0){

                        $('#id_tipo_estructural_set-0-tipo_predomi').append('<option value="10">10. MMC</option>');

                    }

                    if (label.indexOf("(MMNC)") >= 0){

                        $('#id_tipo_estructural_set-0-tipo_predomi').append('<option value="11">11. MMNC</option>');

                    }

                    if (label.indexOf("(PMBC)") >= 0){

                        $('#id_tipo_estructural_set-0-tipo_predomi').append('<option value="12">12. PMBC</option>');

                    }

                    if (label.indexOf("(VB)") >= 0){

                        $('#id_tipo_estructural_set-0-tipo_predomi').append('<option value="13">13. VB</option>');

                    }

                    if (label.indexOf("(VCP)") >= 0){

                        $('#id_tipo_estructural_set-0-tipo_predomi').append('<option value="14">14. VCP</option>');

                    }

                }

            });

        });

        // Lamadas a las validaciones antes de enviar el formulario
        $('#inspeccion_form').submit(function()
        {

            // Validacion de " Al menos uno" para seccion uso
           if (!validar_al_menos_uno_seleccionado('#uso_set-group .inline-related','__prefix__')){

               alert('Se detectaron errores en la planilla');

               error('Debe seleccionar al menos una opción','#uso_set-0');

               return false;
           }

            // Validacion de " Al menos uno" para seccion tipo_estrcutural
           if (!validar_al_menos_uno_seleccionado('#tipo_estructural_set-group .inline-related','__prefix__')){

               alert('Se detectaron errores en la planilla');
               error('Debe seleccionar al menos una opción','#tipo_estructural_set-0');
               return false;
            }

            // Validacion de " Al menos uno" para seccion capacidad ubicacion
            if (!validar_al_menos_uno_seleccionado('#capacidad_ocupacion_set-group .inline-related','__prefix__')){
                alert('Se detectaron errores en la planilla');
                error('Debe seleccionar al menos una opción','#capacidad_ocupacion_set-0');
                return false;
            }


            if (!validar_uso_especifico()){

                return false;
            }

            if (!validar_separacion_edificio()){

                return false;
            }

            if (!validar_ladera()){

                return false;
            }

            if (!validar_base()){

                return false;
            }

        });

    });


})(django.jQuery);


$(document).ready(function(){
    $("#id_observacion_set-0-observacion").charCount(500);
});




