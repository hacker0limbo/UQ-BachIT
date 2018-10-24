function mineDataFromLocal(name) {
    mineData = window.localStorage.getItem(name)
    data = JSON.parse(mineData)
    console.log('mine', data);
    return data
}


function iterateRecords(data) {

    console.log(data);

    $.each(data, function(recordKey, recordValue) {

        var recordName = recordValue["Name"];
        var recordYear = recordValue["Year"];
        var recordArea = recordValue["Geo-subject"];
        var recordRemarks = recordValue["Remarks"];

        if (recordName && recordYear && recordArea && recordRemarks) {

            $("#Instructions").append(
                $('<section class="miningData">').append(
                    $('<h2>').text(recordName),
                    $('<h3>').text(recordYear),
                    $('<p>').text(recordArea),
                    $('<p>').text(recordRemarks)
                )
            );

        }

    });

}


data = mineDataFromLocal('mine')
iterateRecords(data)