let content = document.getElementById('content')
let url = 'http://127.0.0.1:8000/api/project/'
let getContent = ()=>{
    fetch(url)
    .then(response => response.json())
    .then((data=>{
        console.log(data)
        buildData(data)
    }))
}

let buildData = (project)=>{
    content.innerHTML = ''
    for(let i=0;i<project.length;i++){
        console.log(project[i])
        content.innerHTML += `
        <h2>${project[i].id}</h2>
        <p>${project[i].owner.user}</p>
        <p>${project[i].owner.name}</p>
        <p>${project[i].owner.email}</p>
        <p>${project[i].owner.username}</p>
        `
    }
}


getContent()