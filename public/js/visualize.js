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

