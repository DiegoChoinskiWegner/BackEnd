const form = document.querySelector('#to-do-form')
const taskTitleInput = document.querySelector('#task-title-input')
const toDoListUl = document.querySelector('#to-do-list')
const buttonAddTask = document.querySelector('#add-task-button')

// Create tasks array
let tasks = []

function renderTasksToHtml(taskTitle, done=false) {
    // Create element and childs whith, checkbox, name and remove button
    const li = document.createElement('li')
    // Checkbox 
    const input = document.createElement('input')
    input.setAttribute('type', 'checkbox')
    input.addEventListener('change', (event) => {
        const liToToogle = event.target.parentElement

        liToToogle.classList.toggle('done')

        const done = event.target.checked
        const spanToToggle = liToToogle.querySelector('span')

        if (done){
            spanToToggle.style.textDecoration = 'line-through'
        } else {
            spanToToggle.style.textDecoration = 'none'
        }

        tasks = tasks.map((task) => {
            if(task.title === spanToToggle.innerText){
                return {
                    title: task.title,
                    done: !task.done
                }
            }
            return task

          })

        localStorage.setItem('tasks', JSON.stringify(tasks))
    })
    input.checked = done


    // Task name
    const span = document.createElement('span')
    span.innerText = taskTitle

    if (done){
        span.style.textDecoration = 'line-through'
    }

    //Remove button
    const buttonRemoveTask = document.createElement('button')
    buttonRemoveTask.innerText = 'Remover'
    buttonRemoveTask.addEventListener('click', (event) => {
        const liToRemove = event.target.parentElement

        const titleToRemove = liToRemove.querySelector('span').innerText

        tasks = tasks.filter((task) => task.title !== titleToRemove)

        toDoListUl.removeChild(liToRemove)

        localStorage.setItem('tasks', JSON.stringify(tasks))
    })

    //Append the elements in list
    li.appendChild(input)
    li.appendChild(span)
    li.appendChild(buttonRemoveTask)



    //Append li's in html
    toDoListUl.appendChild(li)

}    

window.onload = () => {
    const tasksOnLocalStorage = localStorage.getItem('tasks')

    if (!tasksOnLocalStorage) return
    
    tasks = JSON.parse(tasksOnLocalStorage)

    tasks.forEach((task) => {
        renderTasksToHtml(task.title, task.done)
    })
}

form.addEventListener('submit', (event) => {
    event.preventDefault()

    const taskTitle = taskTitleInput.value

    // Verify if the name of task have least 3 character
    if(taskTitle.length < 3) {
        alert("Sua tarefa precisa ter pelo menos 3 Caracteres!")
        return;
    }

    // function to verify if the task alredy exist.
    function taskTitleExists(taskTitle) {
        return tasks.some(task => task.title === taskTitle);
    }

    // If task not exist, create than in array.
    if (taskTitleExists(taskTitle) == false){
        tasks.push({
            title:taskTitle,
            done:false
        })
        localStorage.setItem('tasks', JSON.stringify(tasks))
    } else {
        alert("Tarefa já existente!");
        return;
    }

    // Add itens on HTML
    renderTasksToHtml(taskTitle)

    taskTitleInput.value = ''


})


