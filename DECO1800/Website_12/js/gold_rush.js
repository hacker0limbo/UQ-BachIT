const mineDataFromLocal = (name) => {
    warData = window.localStorage.getItem(name)
    data = JSON.parse(warData)
    return data
}

data = mineDataFromLocal('mine')
console.log(data);


var instruction = document.querySelector('#Instructions')
for (let i = 0; i < 10; i++) {

    var html = `
        <div class="type-div">
        </div>
    `
    instruction.insertAdjacentHTML('beforeend', html)

}


var apps = document.querySelectorAll('.type-div')

for (let i = 0; i < apps.length; i++) {
    var d = data[i]
    var date = d['Date']
    var district = d['District']
    var name = d['Name']
    var remarks = d['Remarks']
    var year = d['Year']
    var app = apps[i]

    var year_sen = `Year: ${year}`
    var date_sen = `Date: ${date}`
    var name_sen = `Name: ${name}`
    var remarks_sen = `Remarks: ${remarks}`


    var typewriter = new Typewriter(app, {
        loop: true
    });

    typewriter.typeString(year_sen)
        .pauseFor(2000)
        .deleteAll()
        .typeString(date_sen)
        .pauseFor(2000)
        .deleteAll()
        .typeString(name_sen)
        .pauseFor(2000)
        .deleteAll()
        .typeString(remarks_sen)
        .pauseFor(2000)
        .deleteAll()
        .start();
}



$('#Instructions').slick({
    dots: true,
    infinite: true,
    speed: 10,
    slidesToShow: 1,
    adaptiveHeight: true
});



// map

var myMap = L.map('map').setView([-21, 148], 4);

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw", {
    maxZoom: 18,
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' + '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' + 'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: "mapbox.streets"
}).addTo(myMap);

$.each(data, function(recordKey, recordValue) {
    var recordLatitude = recordValue["Latitude"];
    if (recordLatitude) {
        var latLong = recordLatitude.split(",");
        var lat = latLong[0];
        var lng = latLong[1];
        var marker = L.marker([lat, lng]).addTo(myMap);
        marker.on("click", function(event) {
            $("#marker-details").fadeOut("slow", function() {
                $(this).html("<h2>" + recordValue["Name Of Mine"] + "</h2><p>" + recordValue["Remarks"] + "</p>");
                $(this).fadeIn();
            });

        });
    }
});