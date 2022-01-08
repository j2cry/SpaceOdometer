let socket = io();

$(document).ready(function () {
    let placemark;
    placemarksCollection = new YMaps.GeoObjectCollection();
    map = new YMaps.Map($("#yamap")[0]);
    map.setCenter(new YMaps.GeoPoint(37.64, 55.76), 10);
    map.enableScrollZoom({smooth: true});

    YMaps.Events.observe(map, map.Events.Click, function (map, mEvent) {
        placemarksCollection.removeAll();
        map.removeAllOverlays();

        placemark = new YMaps.Placemark(mEvent.getGeoPoint(), {draggable: true});
         placemark.setIconContent('');
        // placemark.setIconContent('my position');
        placemarksCollection.add(placemark);
        map.addOverlay(placemark);
    });


    $('#calculate').on('click', function() {
        latitude = (placemark === undefined) ? map.getCenter().getY() : placemark.getGeoPoint().getY()
        birthday = $('#birthday').val()

        if (!birthday) {
            resultItem = $('#result');
            resultItem.text('You must specify birthday first.');
            resultItem.addClass('error');
            return
        }
        socket.emit('calculate', {'latitude': latitude, 'birthday': birthday}, callback=function(mileage) {
            resultItem = $('#result');
            resultItem.removeClass('error');
            resultItem.addClass('success');
            resultItem.text('Your mileage in the Space relative to the Sun is ~' + mileage + ' km.\nMaybe it\'s time for maintenance?');
        });
    });

});