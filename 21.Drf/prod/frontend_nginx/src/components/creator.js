import React from 'react';

const CreatorItem = ({creator}) => {
    return (
        <tr>
            <td>{creator.username}</td>
            <td>{creator.first_name}</td>
            <td>{creator.last_name}</td>
            <td>{creator.birthday_year}</td>
        </tr>
    )
}
const CreatorList = ({creators}) => {
    return (
        <table>
            <thead>
            <tr>
                <th>Username</th>
                <th>Имя</th>
                <th>Фамилия</th>
                <th>Год рождения</th>
            </tr>
            </thead>
            <tbody>
                {creators.map((creator) => <CreatorItem key = {creator.id} creator={creator}/>)}
            </tbody>
        </table>
    )
}

export default CreatorList