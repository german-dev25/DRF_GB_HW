import React from 'react'


const ProjectItem = ({project}) => {
    return (
        <tr>
            <td>
                {project.name}
            </td>
            <td>
                {project.href_repository}
            </td>
            <td>
                {project.users}
            </td>
            <td>
                {project.is_done.toString()}
            </td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    return (
        <table>
            <th>
                Project Name
            </th>
            <th>
                Ссылка репозитория
            </th>
            <th>
                Участники проекта
            </th>
            <th>
                Готовность
            </th>
            {projects.map((project) => <ProjectItem project={project} />)}
        </table>
    )
}

export default ProjectList