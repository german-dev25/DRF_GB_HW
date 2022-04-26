import React from 'react'


const TodoItem = ({todo}) => {
    return (
        <tr>
            <td>
                {todo.project}
            </td>
            <td>
                {todo.user}
            </td>
            <td>
                {todo.text}
            </td>
            <td>
                {todo.status}
            </td>
            <td>
                {todo.is_active.toString()}
            </td>
        </tr>
    )
}

const TodoList = ({todos}) => {
    return (
        <table>
            <th>
                Связанные проекты
            </th>
            <th>
                Создатель Todo
            </th>
            <th>
                Текст Todo
            </th>
            <th>
                Статус
            </th>
            <th>
                В работе
            </th>
            {todos.map((todo) => <TodoItem todo={todo} />)}
            {console.log(todos)}
        </table>
    )
}

export default TodoList