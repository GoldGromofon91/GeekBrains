import React from "react";

class ProjectCreateForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            projectName: "",
            authorId: 1
        }
    }

    handlerOnInput(event) {
        this.setState({
            [event.target.name]: event.target.value
        });
    }

    handlerOnSubmitForm(event) {
        console.log(event.target.value)
        this.props.projectCreate(this.state.projectName,this.state.authorId)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event) => this.handlerOnSubmitForm(event)}>
                <input type="text" name={"projectName"} placeholder={"Project Name"} onChange={(event) => this.handlerOnInput(event)}/>
                <select  name="authorId"
                        onChange={(event) => this.handlerOnInput(event)}>
                    {this.props.creators.map((author) => (
                        <option value={author.id} key={author.id}>
                            {author.username}
                        </option>
                    ))}
                </select>
                <input type="submit" value="Create"/>
            </form>
        )
    }
}

export default ProjectCreateForm