//Create Google Map instance
function initialize() {
    var mapOptions = {
        zoom: 13,
        center: new google.maps.LatLng(37.76487, -122.41948),
        mapTypeId: google.maps.MapTypeId.TERRAIN
    };

    var map             = new google.maps.Map(d3.select("#map").node(), mapOptions);
    var movie_select    = d3.select("#movie-input");

    var movie;
    var data;
    var overlay;

    // Load scene data
    d3.json("/js/rows.json", function(error, json) {
        // Bind movies to autocomplete form
        $(function() {
            var movies = _.uniq(_.flatten(_.map(json, function (d) { return d.title})));

            $("#movie-input").autocomplete({
                source: function(request, response) {
                    var results = $.ui.autocomplete.filter(movies, request.term);
                    return response(results.slice(0, 11));
                },
                select: update
            });
        });

        overlay = new google.maps.OverlayView()
        if (error)return console.warn(error);
        data = json
        movie = "";
        visualize(json, movie, overlay);
    });

    // update map after enter
    movie_select.on("input", function(d) {
        // exit nodes hack
        d3.selectAll("svg").remove();
        overlay = new google.maps.OverlayView()
        movie = (movie_select.node().value);
        visualize(data, movie, overlay);
        overlay.setMap(map);
    });

    // update map after autocomplete select
    var update = function (event, ui) {
        // exit nodes hack
        d3.selectAll("svg").remove();
        overlay = new google.maps.OverlayView()
        movie = (ui.item.label);
        visualize(data, movie, overlay);
        overlay.setMap(map);
    }
}

google.maps.event.addDomListener(window, 'load', initialize);
