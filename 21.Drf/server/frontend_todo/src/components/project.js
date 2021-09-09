import React from 'react';
import {Link, useParams} from "react-router-dom";

const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                <Link to={`/project/${project.id}/`}>
                    {project.name}
                </Link>
            </td>
            <td>{project.ref}</td>
            <td>{project.users}</td>
        </tr>
    )
}
const ProjectList = ({items}) => {
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
                {items.map((elem) => <ProjectItem key = {elem.id} project={elem}/>)}
            </tbody>
        </table>
    )
}

export default ProjectList