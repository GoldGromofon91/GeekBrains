import React from 'react';

const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>{todo.project}</td>
            <td>{todo.user}</td>
            <td>{todo.text}</td>
            <td>{todo.created_at}</td>
            <td>{todo.is_active}</td>
        </tr>
    )
}
const TodoList = ({items}) => {
    return (
        <table>
            <thead>
            <tr>
                <th>Проект</th>
                <th>Автор</th>
                <th>Содержание</th>
                <th>Дата создания</th>
                <th>Состояние</th>
            </tr>
            </thead>
            <tbody>
                {items.map((elem) => <TodoItem key = {elem.id} todo={elem}/>)}
            </tbody>
        </table>
    )
}

export default TodoList