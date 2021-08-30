import React from 'react';

const CreatorItem=({creator})=> {
    return (
        <tr>
            <td>{creator.username}</td>
            <td>{creator.first_name}</td>
            <td>{creator.last_name}</td>
            <td>{creator.birthday_year}</td>
        </tr>
    )
}
const CreatorList = ({creators})=> {
    return(
        <table>
            <th>Имя</th>
            <th>Фамилия</th>
            <th>Год рождения</th>
            {creators.map((creator)=> <CreatorItem creator={creator} />)}
        </table>
    )
}

export default CreatorList