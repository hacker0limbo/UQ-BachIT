const e = jQuery

const loadPage = () => {
    e('.flipbook').turn({
        // Width

        width: 1000,

        // Height

        height: 600,

        // Elevation

        elevation: 50,

        // Enable gradients

        gradients: true,

        // Auto center this flipbook

        autoCenter: true

    });

}

loadPage()