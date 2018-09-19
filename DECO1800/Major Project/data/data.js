const j = jQuery
const e = (elem) => document.querySelector(elem)

const mineDataFromSLQ = () => {
    const data = {
        resource_id: '63fd8050-0bab-4c04-b837-b2ce664077bf', // the resource id
        limit: 100,
    }
    return new Promise((resolve, reject) => {
        j.ajax({
            url: 'https://data.gov.au/api/3/action/datastore_search',
            data: data,
            dataType: 'jsonp',
            cache: true,
            success: (data) => {
                resolve(data)
            }
        })
    })
}


const convictDataFromSLQ = () => {
    const data = {
        resource_id: '6ab35f9a-e476-4d29-84de-2e18d1e704c7', // the resource id
        limit: 100,
    }
    return new Promise((resolve, reject) => {
        j.ajax({
            url: 'https://data.gov.au/api/3/action/datastore_search',
            data: data,
            dataType: 'jsonp',
            cache: true,
            success: (data) => {
                resolve(data)
            }
        })
    })
}


// https: //data.gov.au/dataset/slq-photographs-1914-1918/resource/26b0b235-13f0-4132-ae47-5ccf3d1c8e89
const warDataFromSLQ = () => {
    const data = {
        resource_id: '26b0b235-13f0-4132-ae47-5ccf3d1c8e89', // the resource id
        limit: 100,
    }
    return new Promise((resolve, reject) => {
        j.ajax({
            url: 'https://data.gov.au/api/3/action/datastore_search',
            data: data,
            dataType: 'jsonp',
            cache: true,
            success: (data) => {
                resolve(data)
            }
        })
    })
}

const storeData = (key, data) => {
    // only store  useful data
    // change it to a string
    records = data.result.records
    window.localStorage.setItem(key, JSON.stringify(records))
}


/**
 * using promise to get data
 */
const getData = () => {
    mineDataFromSLQ()
        .then((data) => {
            storeData('mine', data)
            return convictDataFromSLQ()
        })
        .then((data) => {
            storeData('convict', data)
            return warDataFromSLQ()
        })
        .then((data) => {
            storeData('war', data)
        })
}


/**
 * using async & await to get data
 */
const getDataAsync = async() => {
    mineData = await mineDataFromSLQ()
    convictData = await convictDataFromSLQ()
    warData = await warDataFromSLQ()
    console.log(mineData, convictData, warData);
}


/**
 * test if they have been stored in local
 */
const testLocalStorage = () => {
    // only for the test
    mineData = window.localStorage.getItem('mine')
    warData = window.localStorage.getItem('war')
    convictData = window.localStorage.getItem('convict')
    const d = {
        mineData,
        warData,
        convictData,
    }
    console.log(d);
}


/**
 * init entrence
 */
const __main = () => {
    getData()
    getDataAsync()

    // testLocalStorage()
}

__main()