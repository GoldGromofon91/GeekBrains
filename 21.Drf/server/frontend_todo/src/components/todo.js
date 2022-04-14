import React from 'react';
import {Link} from "react-router-dom";

const TodoItem = ({todo, deleteTodo}) => {
    return (
        <tr>
            <td>{todo.project}</td>
            <td>{todo.user.username}</td>
            <td>{todo.text}</td>
            <td>{todo.created_at}</td>
            <td>{todo.is_active}</td>
            <td>
                <button onClick={() => deleteTodo(todo.id)}>Delete</button>
            </td>
        </tr>
    )
}
const TodoList = ({items, deleteTodo}) => {
    return (
        <div className={"todo-list"}>
            <table>
                <thead>
                <tr>
                    <th>Проект</th>
                    <th>Автор</th>
                    <th>Содержание</th>
                    <th>Дата создания</th>
                    <th>Состояние</th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {items.map((elem) => <TodoItem key={elem.id} todo={elem} deleteTodo={deleteTodo}/>)}
                </tbody>
            </table>
            <Link to={'create'}>Create New Todo</Link>
        </div>
    )
}

export default TodoList