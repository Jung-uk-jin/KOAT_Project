var map = new naver.maps.Map(document.getElementById('map'), {
  zoom: 7,
  mapTypeId: 'normal',
  center: new naver.maps.LatLng(36.4203004, 128.317960)
});

naver.maps.Event.once(map, 'init', function(e) {
  map.data.setStyle(function(feature) {
      var mantle_properties = feature.geometryCollection[0].getRaw().mantle_properties;
      var styleOptions = {
          ...mantle_properties,
      };
      if (feature.getProperty('focus')) {
          styleOptions.fillOpacity = 0.6;
          styleOptions.fillColor = '#0f0';
          styleOptions.strokeColor = '#0f0';
          styleOptions.strokeWeight = 4;
          styleOptions.strokeOpacity = 1;
      }
      return styleOptions;
  });

  map.data.addGeoJson(gangwon, true);
  map.data.addGeoJson(gyeonggi, true);

  map.data.addListener('click', function(e) {
      var feature = e.feature;

      if (feature.getProperty('focus') !== true) {
          feature.setProperty('focus', true);
      } else {
          feature.setProperty('focus', false);
      }
  });

  map.data.addListener('mouseover', function(e) {
      var feature = e.feature;
      map.data.overrideStyle(feature, {
          fillOpacity: 1,
          strokeWeight: 10,
          strokeOpacity: 1
      });
  });

  map.data.addListener('mouseout', function(e) {
      map.data.revertStyle();
  });
});