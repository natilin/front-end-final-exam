const BASE_URL = 'http://localhost:5001'

const getData = async (additionalUrl = '') => {
    const response = await fetch(`${BASE_URL}/${additionalUrl}`, {
        headers: {
            'Content-Type': 'application/json'
        }
    })
    return await response.json()
}

const postData = async (additionalUrl, body) => {
    const response = await fetch(`${BASE_URL}/${additionalUrl}`, {
        method: 'POST',
        body: JSON.stringify(body),
        headers: {
            'Content-Type': 'application/json'
        }
    })

    return await response.json()
}


const getImage = async () => {
    const userChoice = [...document.getElementsByClassName('submit-value')]
        .reduce((obj, n) => n.value === '' ? obj : ({ ...obj, [n.id]: n.value }), {})
    console.log(userChoice);
    
    const querySelection = document.getElementById("query_type").value
    const { map } = await postData(querySelection, userChoice)
    mapContainer = document.getElementById("main")
    mapContainer.innerHTML = map
}

(async () => {
    const { map } = await getData("default_map")
    document.getElementById("main").innerHTML = map

    document.getElementById("query_type").addEventListener('change', ({ target: { value } }) => {
        ids = [...document.getElementById('query_type')].map(x => x.value)
        ids.filter(id => id !== 'average-death-map').forEach(id => {
            document.getElementById(id).style['display'] = id === value ? 'block' : 'none'
        });
    })
})()