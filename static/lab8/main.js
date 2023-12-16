function fillCourseList() {
    fetch('/lab8/api/courses/')
    .then(function (data) {
        return data.json();
    })
    .then(function(courses){
        let tbody = document.getElementById('course-list');
        thody.innerHTML='';
        for(let i = 0; i<courses.length;i++){
            tr = document.createElement('tr')

            let tdName=document.createElement('td')
            tdName.innerText=courses[i].name;

            let tdVideos=document.createElement('td')
            tdVideos.innerText=courses[i].videos;

            let tdPrice=document.createElement('td')
            tdPrice.innerText=courses[i].price || 'бесплатно';

            let editButton = document.createElement('button');
            editButton.innerText = 'редактировать';

            let delButton = document.createElement('button');
            delButton.innerText = 'удалить';
            delButton.onclick = function() {
                deleteCourse(i);
            };

            let tdAction=document.createElement('td')
            tdAction.append(editButton);
            tdAction.append(deltButton);


            tr.append(tdName);
            tr.append(tdVideos);
            tr.append(tdPrice);
            tr.append(tdAction);

            tbody.append(tr);

        }
    })
}
function deleteCoourse(num) {
    if(! confirm('Вы точно хотите удалить курс?'))
        return;
    
    fetch(`/lab8/api/courses/${num}`,{method:'DELETE'})
    .then(function(){
        fillCourseList();
    })
}