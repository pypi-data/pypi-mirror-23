var API_URL = window.location.origin,
    MAP_INIT_LOCATION = [-17.8037954, -63.2561974],
    MAP_INIT_ZOOM = 3;

var make_icon = function(color) {
    var iconMappings = {
        'rouge': {
            iconUrl: 'img/marker-icon-red.png',
            iconSize:     [25, 41],
            iconAnchor:   [12, 40],
            popupAnchor:  [0, -30],
            shadowUrl: 'img/marker-shadow.png',
            shadowSize:   [35, 16],
            shadowAnchor: [8, 10]
        },
        'jaune': {
            iconUrl: 'img/marker-icon-yellow.png',
            iconSize:     [25, 41],
            iconAnchor:   [12, 40],
            popupAnchor:  [0, -30],
            shadowUrl: 'img/marker-shadow.png',
            shadowSize:   [35, 16],
            shadowAnchor: [8, 10]
        },
        'vert': {
            iconUrl: 'img/marker-icon-green.png',
            iconSize:     [25, 41],
            iconAnchor:   [12, 40],
            popupAnchor:  [0, -30],
            shadowUrl: 'img/marker-shadow.png',
            shadowSize:   [35, 16],
            shadowAnchor: [8, 10]
        }
    };
    var IconClass = null;
    if (color === 'bleu' || !color) {
        IconClass = L.Icon.Default;
    } else {
        IconClass = L.Icon.extend({options: iconMappings[color]});
    }
    return new IconClass();
};

var formatPopup = function(msg, action) {
    var buttonLabel = (action === 'Modifier') ? action : 'Ajouter un spot';
    return `
    <div>
        ${msg}
    </div>
    <div class="popup-form">
        <button onclick="app.onClickNewModal('${action}')" class="pure-button-primary pure-button">
            ${buttonLabel}
        </button>
    </div>
    `;
};

var app = new Vue({
  el: '#vue-app',
  data: {
    current_step: {},
    colors: ['bleu', 'rouge', 'jaune', 'vert'],
    mymap: null,
    action: 'default',
    markers: [],
    popup: L.popup({maxWidth: 600, maxHeight: 400, className: "popup-html"})
  },
  mounted: function() {
    this.init();
  },
  methods: {
    init: function() {
        autosize(document.querySelectorAll('textarea'));
        this.initMap();
        this.fetchSteps();
    },
    initMap: function() {
        this.mymap = L.map('mapid').setView(MAP_INIT_LOCATION, MAP_INIT_ZOOM);
        L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
            maxZoom: 18,
            id: 'mapbox.streets',
        }).addTo(this.mymap);
        this.mymap.on('click', this.onMapClick);
    },
    fetchSteps: function() {
        $.ajax({
            type: "GET",
            url: `${API_URL}/steps/`,
            dataType: "json",
            success: data => {
                this.resetMarkers();
                this.addMarkers(data.steps);
            },
            failure: (errMsg) => {console.log(errMsg)}
        });
    },
    resetMarkers: function() {
        this.markers.forEach(marker => marker.remove());
        this.markers = [];
        this.current_step = {};
    },
    addMarkers: function(steps) {
        steps.forEach(step => {
            var marker = L.marker([step.lat, step.lng], {
                draggable: true,
                icon: make_icon(step.color),
            }).addTo(this.mymap);
            marker.step = step;
            var that = this;

            marker.on('click', function(e) {
                that.current_step = this.step;
            });

            marker.on('dragend', function(e) {
                var latlng = this.getLatLng();
                that.current_step = this.step;
                that.current_step.lat = latlng.lat;
                that.current_step.lng = latlng.lng;
                that.action = 'Modifier';
                that.save();
            });

            marker.bindPopup(L.popup({
                maxWidth: 600,
                maxHeight: 400,
                className: "popup-html"
            }).setContent(formatPopup(step.content, 'Modifier')));
            this.markers.push(marker);
        });
    },
    remove: function() {
        if (!confirm("Êtes-vous sûr ?"))
            return;

        $.ajax({
            type: "DELETE",
            url: `${API_URL}/step/${this.current_step.eid}`,
            dataType: "json",
            success: data => {this.fetchSteps();},
            failure: errMsg => {console.log(errMsg)}
        });
        $('#myModal').modal('hide');
    },
    save: function() {
        var step = {
            "content": this.current_step.content,
            "lat": this.current_step.lat,
            "lng": this.current_step.lng,
            "color": this.current_step.color
        };
        var edit = (this.action === 'Modifier');
        var http_method = edit ? 'PUT' : 'POST',
            http_url = `${API_URL}/step${edit ? '/' + this.current_step.eid : ''}`;
        $.ajax({
            type: http_method,
            url: http_url,
            data: JSON.stringify({"step": step}),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: data => {this.fetchSteps();},
            failure: errMsg => {console.log(errMsg)}
        });
        $('#myModal').modal('hide');
        this.popup.remove();
    },
    onClickNewModal: function(action) {
        if (action === 'Ajouter') {
            this.current_step.color = 'bleu';
        }
        this.action = action;
        $('#myModal').modal('show');
    },
    onMapClick: function(e) {
        this.current_step = {
            lat: e.latlng.lat,
            lng: e.latlng.lng
        };
        var floatFormat = new Intl.NumberFormat("fr-FR", {
            maximumFractionDigits: 5,
        });
        var lat = floatFormat.format(this.current_step.lat),
            lng = floatFormat.format(this.current_step.lng);
        var msg = `Latitude: <code>${lat}</code>, Longitude: <code>${lng}</code>`
        this.popup
            .setLatLng(e.latlng)
            .setContent(formatPopup(msg, 'Ajouter'))
            .openOn(this.mymap);
    }
  }
});

window.app = app;
