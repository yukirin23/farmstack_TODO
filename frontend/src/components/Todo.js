import axios from 'axios'
import React from 'react'

function TodoItem(props){
    const deleteTodoHandlers = (title) => {
        axios.delete('http://127.0.0.1:8000/api/todo/${title}')
        .then(res=> console.log(res.data))}

        return (
            <div>
                <p>
                {props.todo.title}
                    <span style={{ 'fontWeight':'bold, underline'}}>
                        </span>{props.todo.description}
                    <button onClick={() => deleteTodoHandlers(props.todo.title)}
                    className="btn btn-outline-danger my-2 mx-2" style={{'borderRadius':'50px'}}>
                        x
                    </button>
                    <hr></hr>
                </p>
            </div>
        )
}

export default TodoItem