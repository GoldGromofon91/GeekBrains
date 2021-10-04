import React from 'react';
import {Link, useParams} from "react-router-dom";

const ProjectItem = ({project, deleteProject}) => {
    return (
        <tr>
            <td>
                <Link to={`/project/${project.id}/`}>
                    {project.name}
                </Link>
            </td>
            <td>{project.ref}</td>
            <td>{project.users}</td>
            <td>
                <button onClick={() => deleteProject(project.id)}>Delete</button>
            </td>
        </tr>
    )
}
const ProjectList = ({items, deleteProject}) => {
    return (
        <div className={"project-list"}>
            <table>
                <thead>
                <tr>
                    <th>Название проекта</th>
                    <th>Ссылка</th>
                    <th>Имя автора</th>
                    <th></th>
                </tr>
                </thead>
                <tbody>
                {items.map((elem) => <ProjectItem key={elem.id} project={elem} deleteProject={deleteProject}/>)}
                </tbody>
            </table>
            <Link to={'create'}>Create New Project</Link>
        </div>

    )
}

export default ProjectList