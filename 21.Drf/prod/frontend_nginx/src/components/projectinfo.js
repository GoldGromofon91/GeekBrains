import React from 'react';
import {useParams} from "react-router-dom";

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>{project.name}</td>
            <td>{project.ref}</td>
            <td>{project.users}</td>
        </tr>
    )
}
const ProjectInfo = ({items}) => {
    let {id} = useParams();
    let getProject = items.filter((elem) => elem.id === +id);
    return (
        <table>
            <thead>
            <tr>
                <th>Название проекта</th>
                <th>Ссылка</th>
                <th>Имя автора</th>
            </tr>
            </thead>
            <tbody>
                {getProject.map((elem) => <ProjectItem key={elem.id} project={elem}/>)}
            </tbody>
        </table>
    )
}

export default ProjectInfo