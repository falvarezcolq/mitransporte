    var map;
     function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
          center: {lat: -16.77332601802906, lng: -65.64294355123906},
          zoom: 5,
        });
        var marker = new google.maps.Marker({
          position: {lat: -16.77332601802906, lng: -65.64294355123906},
          map: map,
        title: ''
        });
      }

      function setPositionForm(latitude,longitude){
        document.getElementById("id_latitude").value = latitude;
        document.getElementById("id_longitude").value = longitude;
      }

    function getPositionForm(){
        latitude =  document.getElementById("id_latitude").value;
        longitude =  document.getElementById("id_longitude").value;
        if ( latitude != "" && longitude !="" ) {
            return  latlng = {
            lat: parseFloat(latitude),
            lng: parseFloat(longitude)
            }
        }
        return false
    }

   function setMap(latitude,longitude) {
        latlng={lat: latitude, lng: longitude}
        map = new google.maps.Map(document.getElementById('map'), {
          center: latlng,
          zoom: 10,
        });

        var marker = new google.maps.Marker({
          position: latlng,
          map: map,
           title: 'NUEVO'
        });

      map.addListener("click",(mapsMouseEvent)=>{
        marker.setMap(map);
        marker.setPosition(mapsMouseEvent.latLng)

        console.log(mapsMouseEvent.latLng)
        setPositionForm(mapsMouseEvent.latLng.lat(),mapsMouseEvent.latLng.lng())
      })
  }


   function onGeoError(event)
   {
       alert("Error code " + event.code + ". " + event.message);
   }

   function onGeoSuccess(event)
   {

       LatLng = getPositionForm()
       if ( LatLng ){
           latitude = LatLng.lat
           longitude = LatLng.lng
       }else{
           latitude = event.coords.latitude
           longitude = event.coords.longitude
       }

       setPositionForm(latitude,longitude)
       setMap(latitude,longitude)
   }


   function getLocationConstant()
   {
       if(navigator.geolocation)
       {
           navigator.geolocation.getCurrentPosition(onGeoSuccess,onGeoError);
       } else {
           alert("Your browser or device doesn't support Geolocation");
       }
   }

 window.onload = function (){
    getLocationConstant()
 }
