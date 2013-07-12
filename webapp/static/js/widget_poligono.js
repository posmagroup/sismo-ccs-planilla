(function($) {




    $(document).ready(function(){



        $.get('/mapa/',function(data){



            $(data).insertAfter($("#calendarbox0"));


        });






    });



})(django.jQuery);
/*
(function($) {

    var lon = 5;
    var lat = 40;
    var zoom = 5;
    var map, layer;

    function init(poligonos_db){

        var bounds = new OpenLayers.Bounds(
            728722.3849999998, 1161408.387,
            730852.7980000003, 1163163.4190000005
        );

        var options = {
            maxExtent: bounds,

            projection: "EPSG:2202"//,
            //units: 'm'
        };

        //map = new OpenLayers.Map( 'map');
        map = new OpenLayers.Map( 'map', options);
       layer = new OpenLayers.Layer.WMS( "OpenLayers WMS",
            "http://vmap0.tiles.osgeo.org/wms/vmap0",
            {layers: 'basic'} );
        map.addLayer(layer);
        map.setCenter(new OpenLayers.LonLat(lon, lat), zoom);
        var featurecollection = {
            "type": "FeatureCollection",
            "features": [
                {"geometry": {
                    "type": "GeometryCollection",
                    "geometries": [
                        {
                            "type": "LineString",
                            "coordinates":
                                [[11.0878902207, 45.1602390564],
                                    [15.01953125, 48.1298828125]]
                        },
                        {
                            "type": "Polygon",
                            "coordinates":
                                [[[11.0878902207, 45.1602390564],
                                    [14.931640625, 40.9228515625],
                                    [0.8251953125, 41.0986328125],
                                    [7.63671875, 48.96484375],
                                    [11.0878902207, 45.1602390564]]]
                        },
                        {
                            "type":"Point",
                            "coordinates":[15.87646484375, 44.1748046875]
                        }
                    ]
                },
                    "type": "Feature",
                    "properties": {}}
            ]
        };
        var geojson_format = new OpenLayers.Format.GeoJSON();
        var vector_layer = new OpenLayers.Layer.Vector();

        //vector_layer.addFeatures(geojson_format.read(featurecollection));
        vector_layer.addFeatures(geojson_format.read(poligonos_db));
        map.addLayer(vector_layer);

    }







$(document).ready(function(){
OpenLayers.Style(OpenLayers.Util.applyDefaults({
                    externalGraphic: "/static/img/marker-green.png",
                    graphicOpacity: 1,
                    rotation: -45,
                    pointRadius:

                        $.get('/database_polygon');


        $('<div id="map" class="smallmap"> </div>  <div id="status"></div>').insertAfter($("#anexo_set-group"));


        //init(poligonos_bd);





//another_try


        var map, selectControl;
        OpenLayers.Feature.Vector.style['default']['strokeWidth'] = '2';
        function init2(poligonos_bd){
            map = new OpenLayers.Map('map');
            var wmsLayer = new OpenLayers.Layer.WMS(
                "OpenLayers WMS",
                "http://vmap0.tiles.osgeo.org/wms/vmap0",
                {layers: 'basic'}
            );

            // allow testing of specific renderers via "?renderer=Canvas", etc
            var renderer = OpenLayers.Util.getParameters(window.location.href).renderer;
            renderer = (renderer) ? [renderer] : OpenLayers.Layer.Vector.prototype.renderers;

            var vectors1 = new OpenLayers.Layer.Vector("Vector Layer 1", {
                    renderers: renderer,
                    styleMap: new OpenLayers.StyleMap({
                        "default": new  10
                }, OpenLayers.Feature.Vector.style["default"])),
                "select": new OpenLayers.Style({
                    externalGraphic: "/static/img/marker-blue.png"
                })
            })
        });
        var vectors2 = new OpenLayers.Layer.Vector("Vector Layer 2", {
            renderers: renderer,
            styleMap: new OpenLayers.StyleMap({
                "default": new OpenLayers.Style(OpenLayers.Util.applyDefaults({
                    fillColor: "red",
                    strokeColor: "gray",
                    graphicName: "square",
                    rotation: 45,
                    pointRadius: 15
                }, OpenLayers.Feature.Vector.style["default"])),
                "select": new OpenLayers.Style(OpenLayers.Util.applyDefaults({
                    graphicName: "square",
                    rotation: 45,
                    pointRadius: 15
                }, OpenLayers.Feature.Vector.style["select"]))
            })
        });
        var geojson_format = new OpenLayers.Format.GeoJSON();
        var vector_layer = new OpenLayers.Layer.Vector();


        //vector_layer.addFeatures(geojson_format.read(poligonos_bd));
       // map.addLayer(vector_layer);

        var vectors3 = new OpenLayers.Layer.Vector("KML", {
            strategies: [new OpenLayers.Strategy.Fixed()],
            protocol: new OpenLayers.Protocol.HTTP({
                url: "/static/poligonos.kml",
                format: new OpenLayers.Format.KML({
                    extractStyles: true,
                    extractAttributes: true,
                    maxDepth: 2
                })
            })
        })




        map.addLayers([wmsLayer, vectors1, vectors2,vectors3]);
        map.addControl(new OpenLayers.Control.LayerSwitcher());

        selectControl = new OpenLayers.Control.SelectFeature(
            [vectors1, vectors2,vector_layer],
            {
                clickout: true, toggle: false,
                multiple: false, hover: false,
                toggleKey: "ctrlKey", // ctrl key removes from selection
                multipleKey: "shiftKey" // shift key adds to selection
            }
        );

        map.addControl(selectControl);
        selectControl.activate();
        map.setCenter(new OpenLayers.LonLat(0, 0), 3);
        vectors1.addFeatures(createFeatures());
        vectors2.addFeatures(createFeatures());

        vectors1.events.on({
            "featureselected": function(e) {
                showStatus("selected feature "+e.feature.id+" on Vector Layer 1" );
            },
            "featureunselected": function(e) {
                showStatus("unselected feature "+e.feature.id+" on Vector Layer 1");
            }
        });
        vectors2.events.on({
            "featureselected": function(e) {
                showStatus("selected feature "+e.feature.id+" on Vector Layer 2 ");
            },
            "featureunselected": function(e) {
                showStatus("unselected feature "+e.feature.id+" on Vector Layer 2");
            }
        });
        vector_layer.events.on({
            "featureselected": function(e) {
                showStatus("selected feature "+e.feature.id+" on Vector Layer 2 ");
            },
            "featureunselected": function(e) {
                showStatus("unselected feature "+e.feature.id+" on Vector Layer 2");
            }
        });
    }

    function createFeatures() {
        var extent = map.getExtent();
        var features = [];
        for(var i=0; i<10; ++i) {
            features.push(new OpenLayers.Feature.Vector(
                new OpenLayers.Geometry.Point(extent.left + (extent.right - extent.left) * Math.random(),
                    extent.bottom + (extent.top - extent.bottom) * Math.random()
                )));
        }
        return features;
    }

    function showStatus(text) {
        document.getElementById("status").innerHTML = text;
    }



    init2(poligonos_bd);



//another_try





















});


})(django.jQuery,poligonos_bd);
*/
