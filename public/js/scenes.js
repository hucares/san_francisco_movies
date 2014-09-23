//Create Google Map instance
function initialize() {
    var mapOptions = {
        zoom: 13,
        center: new google.maps.LatLng(37.76487, -122.41948),
        mapTypeId: google.maps.MapTypeId.TERRAIN
    };

    var map             = new google.maps.Map(d3.select("#map").node(), mapOptions);
    var movie_select    = d3.select("#movie-input");

    //Overlay nodes
    var movie;
    var data;
    var overlay;
    d3.json("/js/rows.json", function(error, json) {
        //bind movies to autocomplete form
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

    movie_select.on("input", function(d) {
        //exit hack
        d3.selectAll("svg").remove();

        overlay = new google.maps.OverlayView()
        movie = (movie_select.node().value);
        visualize(data, movie, overlay);
        overlay.setMap(map);
    });

    //autocomplete update
    var update = function (event, ui) {
        d3.selectAll("svg").remove();

        overlay = new google.maps.OverlayView()
        movie = (ui.item.label);
        visualize(data, movie, overlay);
        overlay.setMap(map);
    }

    var visualize = function(data, filter, overlay) {
        data = data.filter(function (d) { return d.title == filter; });

        overlay.onAdd = function() {
            var layer = d3.select(this.getPanes().overlayLayer).append("div")
            .attr("class", "stations");

            overlay.draw = function() {
                var projection  = this.getProjection(),
                padding     = 10;

                var marker = layer.selectAll("svg")
                .data(d3.entries(data))
                .each(transform)
                .enter().append("svg:svg")
                .each(transform)
                .attr("class", "marker");

                marker.append("svg:circle")
                .attr("r", 6.5)
                .attr("cx", padding)
                .attr("cy", padding);

                marker.append("svg:text")
                .attr("font-size", 10)
                .attr("x", padding + 10)
                .attr("dy", "2.0em")
                .text(function(d) { return d.value.location; });


                function transform(d) {
                    d = new google.maps.LatLng(d.value.lat, d.value.lng);
                    d = projection.fromLatLngToDivPixel(d);
                    return d3.select(this)
                    .style("left", (d.x - padding) + "px")
                    .style("top", (d.y - padding) + "px");
                }
            }
        }

    }

}

google.maps.event.addDomListener(window, 'load', initialize);


